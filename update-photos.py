#!/usr/bin/env python3
"""Run this after adding or removing pictures in the photos folder.
It writes photos/photos.json, the list the website reads to build the Photos tab.
    python3 update-photos.py
"""
import json, re, pathlib
folder = pathlib.Path(__file__).resolve().parent / "photos"
exts = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"}
natural = lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]
names = sorted((p.name for p in folder.iterdir() if p.suffix.lower() in exts), key=natural)
(folder / "photos.json").write_text(json.dumps(names, indent=2))
print(f"{len(names)} photos listed in photos/photos.json")
