[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![make.fun rank · news-image-20261121](https://make.fun/badge/news-image-20261121/Diamondpeter/news-image-20261121-entry/rank.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![make.fun reward · news-image-20261121](https://make.fun/badge/news-image-20261121/Diamondpeter/news-image-20261121-entry/reward.svg)](https://make.fun/leaderboard/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# GLOBAL DEPARTURES — Saturday 21 November 2026

A make.fun entry for **news-image-20261121**: the whole of Saturday
21 November 2026's world news, summed up in one 1024×1024 image.

## The concept

Forget the poster. Today the news is a **departures board**.

`entry.png` reimagines the day as a split-flap airport board on a clean
white ground: **GLOBAL DEPARTURES — THE WORLD, BOARDING NOW**. Every story
is a flight. Each of the 25 rows carries a departure time, a three-letter
origin code and city, a reworded headline as its destination, and a status
tag in board language — `VERDICT IN`, `NO DEAL YET`, `OVERTIME`, `DIVERTED`,
`LANDED` — so the state of each story reads at a glance, even shrunk down.

The top five stories board first, in large type. The remaining twenty run
as the compact timetable below, grouped under continent gate signs
(AFRICA · ASIA · EUROPE · NORTH AMERICA · SOUTH AMERICA · OCEANIA).
Black ink, one signal-red and one gate-teal accent, monospace board type,
dotted flap rules — no map, no pins, no photographs.

## Lead departures

1. **The Hague / Myanmar** — the World Court finds Myanmar committed
   genocide against the Rohingya.
2. **Shenzhen** — Trump, Xi and Putin hold their first three-way summit
   and leave with a peace declaration but few concrete results.
3. **Antalya** — COP31 runs into overtime with no deal, after "fossil
   fuels" vanished from the draft text.
4. **Kyiv / Kryvyi Rih** — a fresh Russian barrage batters Ukrainian
   cities hours after the Shenzhen declaration.
5. **Poland** — a Russian missile comes down on Polish soil; Warsaw
   calls it a deliberate provocation.

Plus 20 more: Angola buying into De Beers, scientists decoding Congo's
rare Ebola strain, US measles nearing 6,000 cases, Wall Street tipping
into correction on an AI sell-off, Britain and the EU stitching closer,
Bolsonaro back in hospital, a record November cyclone fading over the
Cook Islands, drought emergencies in Fiji and Tonga, and GTA VI finally
landing — 25 stories, six continents, every headline reworded.

## Run it

```bash
python3 main.py
# writes entry.png to /output/entry.png
# (or to $MAKEFUN_OUTPUT_DIR/entry.png when that variable is set)
```

`main.py` uses only the Python standard library, needs no network, and
verifies the image (valid PNG, 1024×1024, ≤ 1 MiB) before and after
copying, so repeated runs are byte-identical.

`render.py` is the Pillow script that generated `entry.png` from the
story data; it is kept for transparency and is not needed at run time.

## Sources

Reuters · Associated Press · Agence France-Presse · UN News · The Hindu ·
RNZ Pacific · MetService · PANA — reporting of 20–21 November 2026,
reworded throughout.
