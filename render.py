#!/usr/bin/env python3
"""Render entry.png — GLOBAL DEPARTURES board, 21 Nov 2026. Deterministic."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
WHITE = (255, 255, 255)
INK = (17, 17, 17)
GREY = (105, 105, 100)
LGREY = (240, 240, 236)
MGREY = (210, 210, 205)
RED = (200, 30, 30)
TEAL = (0, 110, 105)
AMBER = (176, 110, 0)

SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
MONO_B = "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf"
MONO = "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"

def f(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)
MX = 34                      # side margin
CW = W - 2 * MX              # content width

def tw(text, font):
    return d.textlength(text, font=font)

def fit(text, path, size, maxw, minsize=12):
    s = size
    while s > minsize and tw(text, f(path, s)) > maxw:
        s -= 1
    return f(path, s)

def dotted(y, x0=MX, x1=W - MX, color=MGREY):
    x = x0
    while x < x1:
        d.line([(x, y), (min(x + 5, x1), y)], fill=color, width=2)
        x += 10

# ---------------------------------------------------------------- masthead
y = 20
small = f(MONO_B, 15)
d.text((MX, y), "TERMINAL W  ·  WORLD NEWS", font=small, fill=INK)
r = "PLEASE CHECK YOUR GATE →"
d.text((W - MX - tw(r, small), y), r, font=small, fill=RED)
y += 26
# red flap block + title
d.rectangle([MX, y + 4, MX + 18, y + 58], fill=RED)
title = f(SANS_B, 57)
d.text((MX + 30, y), "GLOBAL DEPARTURES", font=title, fill=INK)
sub = "THE WORLD, BOARDING NOW"
d.text((W - MX - tw(sub, f(MONO_B, 17)), y + 22), sub, font=f(MONO_B, 17), fill=TEAL)
y += 60
dateline = f(MONO_B, 19)
d.text((MX, y), "SATURDAY 21 NOVEMBER 2026", font=dateline, fill=INK)
mid = "25 FLIGHTS  ·  6 CONTINENTS"
d.text(((W - tw(mid, f(MONO, 15))) / 2, y + 2), mid, font=f(MONO, 15), fill=GREY)
rt = "ONE IMAGE, ONE DAY"
d.text((W - MX - tw(rt, dateline), y), rt, font=dateline, fill=INK)
y += 24

# ---------------------------------------------------------------- column bar
d.rectangle([MX, y, W - MX, y + 26], fill=INK)
cb = f(MONO_B, 14)
for txt, x in [("TIME", MX + 10), ("FROM", MX + 84), ("DESTINATION — TODAY'S STORY", MX + 210)]:
    d.text((x, y + 5), txt, font=cb, fill=WHITE)
st = "STATUS"
d.text((W - MX - 10 - tw(st, cb), y + 5), st, font=cb, fill=WHITE)
y += 26

# ---------------------------------------------------------------- hero rows
HEROES = [
    ("06:10", "HAG", "THE HAGUE", "WORLD COURT: MYANMAR COMMITTED GENOCIDE",
     "Landmark ruling on the Rohingya — Myanmar calls it unfair", "VERDICT IN", RED),
    ("07:45", "SZX", "SHENZHEN", "TRUMP, XI & PUTIN MEET FACE TO FACE",
     "First three-way summit ends in peace words, few hard results", "BOARDING", TEAL),
    ("09:20", "AYT", "ANTALYA", "CLIMATE TALKS STALL AT THE FINAL GATE",
     "COP31 draft drops 'fossil fuels' — bloc of nations demands more", "NO DEAL YET", RED),
    ("11:05", "KBP", "KYIV", "FRESH RUSSIAN BARRAGE BATTERS CITIES",
     "Kryvyi Rih: 2 dead, 42 hurt — hours after the peace declaration", "UNDER FIRE", RED),
    ("12:40", "WAW", "WARSAW", "RUSSIAN MISSILE DOWN ON POLISH SOIL",
     "Warsaw calls the crash a deliberate provocation by Moscow", "ALERT", AMBER),
]
HH = 49
for i, (tm, code, city, head, detail, status, sc) in enumerate(HEROES):
    if i % 2 == 0:
        d.rectangle([MX, y, W - MX, y + HH], fill=LGREY)
    d.text((MX + 10, y + 8), tm, font=f(MONO_B, 21), fill=INK)
    d.rectangle([MX + 84, y + 9, MX + 84 + 52, y + 33], outline=INK, width=2)
    d.text((MX + 84 + 8, y + 12), code, font=f(MONO_B, 17), fill=INK)
    d.text((MX + 146, y + 12), city, font=f(MONO_B, 14), fill=GREY)
    hf = fit(head, SANS_B, 24, 596)
    d.text((MX + 230, y + 4), head, font=hf, fill=INK)
    d.text((MX + 230, y + 28), detail, font=f(SANS, 15), fill=GREY)
    sf = f(MONO_B, 15)
    d.text((W - MX - 10 - tw(status, sf), y + 8), status, font=sf, fill=sc)
    y += HH
    dotted(y - 1)

# ---------------------------------------------------------------- compact gates
GATES = [
    ("GATE A · AFRICA", [
        ("13:15", "LAD", "Angola buys a slice of the diamond giant De Beers", "DEAL DONE", TEAL),
        ("14:00", "GOM", "Scientists decode rare Ebola strain spreading in Congo", "TRACKING", AMBER),
        ("14:35", "TUN", "Tunisia jails veteran rights defender for five years", "SENTENCED", RED),
        ("15:10", "JHB", "581 women killed in a single South African quarter", "COUNTED", RED),
    ]),
    ("GATE B · ASIA", [
        ("15:45", "DAC", "Arson flares again amid Bangladesh's political unrest", "UNREST", RED),
        ("16:20", "ULN", "Mongolia's president quits — early election looms", "RESIGNED", AMBER),
        ("16:55", "JKT", "Jakarta & Beijing talk up South China Sea cooperation", "TALKS", TEAL),
    ]),
    ("GATE C · EUROPE", [
        ("17:30", "CPH", "Denmark expels envoy over alleged plot to kill rapper", "EXPELLED", RED),
        ("18:05", "BRU", "Britain & EU stitch closer with three new deals", "SIGNED", TEAL),
        ("18:40", "PAR", "Europe's youth march together over cost of living", "MARCHING", AMBER),
    ]),
    ("GATE D · NORTH AMERICA", [
        ("19:15", "ATL", "US measles tally nears 6,000 — worst in decades", "SPREADING", RED),
        ("19:50", "NYC", "19½ years for plot to kill Sikh leader in New York", "JAILED", INK),
        ("20:25", "NYSE", "AI sell-off tips Wall Street into correction", "DOWN 3.7%", RED),
        ("21:00", "BOS", "Judge challenges freeze on refugees' green cards", "IN COURT", AMBER),
        ("21:35", "LAX", "GTA VI finally lands — critics are thrilled", "LANDED", TEAL),
    ]),
    ("GATE E · SOUTH AMERICA", [
        ("22:10", "BSB", "Bolsonaro back in hospital with stomach pain", "ADMITTED", AMBER),
        ("22:45", "EZE", "Argentina's Senate backs disability rights, 71–0", "PASSED", TEAL),
        ("23:20", "BAQ", "Boca meet Mineiro in heavyweight cup final today", "MATCHDAY", TEAL),
    ]),
    ("GATE F · OCEANIA", [
        ("23:45", "RAR", "Record November cyclone fades over Cook Islands", "WEAKENING", AMBER),
        ("23:59", "SUV", "Drought emergencies declared in Fiji and Tonga", "DRY SPELL", RED),
    ]),
]
RH = 23
GH = 19
for gname, rows in GATES:
    d.rectangle([MX, y, W - MX, y + GH], fill=INK)
    d.text((MX + 10, y + 3), gname, font=f(MONO_B, 13), fill=WHITE)
    note = f"{len(rows)} DEPARTURES"
    d.text((W - MX - 10 - tw(note, f(MONO, 12)), y + 4), note, font=f(MONO, 12), fill=WHITE)
    y += GH
    for tm, code, head, status, sc in rows:
        d.text((MX + 10, y + 4), tm, font=f(MONO, 15), fill=GREY)
        d.text((MX + 84, y + 3), code, font=f(MONO_B, 16), fill=INK)
        hf = fit(head, SANS, 19, CW - 84 - 78 - 165)
        d.text((MX + 162, y + 2), head, font=hf, fill=INK)
        sf = f(MONO_B, 13)
        d.text((W - MX - 10 - tw(status, sf), y + 5), status, font=sf, fill=sc)
        y += RH
        dotted(y - 1)

# ---------------------------------------------------------------- footer
y += 6
foot = "SOURCES: REUTERS · AP · AFP · UN NEWS · THE HINDU · RNZ PACIFIC · METSERVICE · PANA  —  REPORTING OF 20–21 NOV 2026"
ff = fit(foot, MONO, 13, CW)
d.text(((W - tw(foot, ff)) / 2, y), foot, font=ff, fill=GREY)
y += 20
foot2 = "NEXT BOARD TOMORROW 00:00  ·  THANK YOU FOR FLYING THE NEWS"
d.text(((W - tw(foot2, f(MONO_B, 13))) / 2, y), foot2, font=f(MONO_B, 13), fill=INK)
print("final y:", y + 18)

img.save("/home/hatch/workspace/makefun/news-image-20261121-entry/entry.png", optimize=True)
print("saved")
