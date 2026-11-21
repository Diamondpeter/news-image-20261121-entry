#!/usr/bin/env python3
"""make.fun entry: news-image-20261121 — GLOBAL DEPARTURES.

Copies the bundled entry.png to the output directory.
Honours $MAKEFUN_OUTPUT_DIR, defaulting to /output.
Standard library only; no network.
"""

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1024 * 1024  # 1 MiB
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def png_dimensions(path: Path) -> tuple[int, int]:
    """Read width/height from the PNG IHDR chunk; raise ValueError if invalid."""
    with path.open("rb") as fh:
        header = fh.read(24)
    if len(header) < 24 or not header.startswith(PNG_SIGNATURE):
        raise ValueError("not a PNG file (bad signature)")
    if header[12:16] != b"IHDR":
        raise ValueError("not a PNG file (missing IHDR chunk)")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check_image(path: Path, label: str) -> str | None:
    """Return an error string, or None if the image passes every check."""
    if not path.is_file():
        return f"{label} is missing: {path}"
    size = path.stat().st_size
    if size == 0:
        return f"{label} is empty: {path}"
    if size > MAX_BYTES:
        return f"{label} is {size} bytes, over the 1 MiB limit: {path}"
    try:
        width, height = png_dimensions(path)
    except (OSError, ValueError) as exc:
        return f"{label} is not a valid PNG: {exc}"
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        return (
            f"{label} is {width}x{height}, expected "
            f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}: {path}"
        )
    return None


def main() -> int:
    source = Path(__file__).resolve().parent / "entry.png"

    problem = check_image(source, "source image")
    if problem is not None:
        return fail(problem)

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        return fail(f"cannot create output directory {out_dir}: {exc}")
    dest = out_dir / "entry.png"

    try:
        shutil.copyfile(source, dest)
    except OSError as exc:
        return fail(f"cannot copy {source} to {dest}: {exc}")

    problem = check_image(dest, "written image")
    if problem is not None:
        return fail(problem)

    source_hash = sha256_of(source)
    dest_hash = sha256_of(dest)
    if source_hash != dest_hash:
        return fail(
            f"verification failed: written file differs from source "
            f"(source sha256 {source_hash}, written sha256 {dest_hash})"
        )

    width, height = png_dimensions(dest)
    print(
        f"OK: wrote {dest} — PNG {width}x{height}, "
        f"{dest.stat().st_size} bytes (limit {MAX_BYTES}), "
        f"sha256 {dest_hash}, byte-identical to source."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
