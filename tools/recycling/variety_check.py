#!/usr/bin/env python3
"""Check a demo storyboard for variety (graphics-pipeline.md, Guided walkthrough rule 6).

Usage: python3 variety_check.py storyboard.md [more.md ...]

Each file holds one markdown table per card. Required columns (case insensitive):
Screen, Target type, Position. Rows are the steps, in order. A line starting with
"## " before a table names the card; "complex" in that heading (or 5 or more steps)
makes it a complex demo.

Rules checked:
  * complex demo: at least 3 distinct screens, and at least 3 screen changes
  * at most 2 steps whose target type is "primary button", and only in the last 3 steps
  * no 3 steps in a row with the same target type
  * at least 3 different target types
  * targets in at least 3 different positions
Exit code 0 when every card passes, 1 otherwise.
"""
import re, sys

PRIMARY = {"primary button", "button", "primary"}

def parse(path):
    cards, name, rows, head = [], "card", [], None
    def flush():
        nonlocal rows, head, name
        if head and rows:
            cards.append((name, head, rows))
        rows, head = [], None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("## "):
            flush(); name = line[3:].strip(); continue
        if line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            if head is None:
                head = [c.lower() for c in cells]
            else:
                rows.append(cells)
        else:
            if head and rows:
                flush()
    flush()
    return cards

def col(head, *names):
    for n in names:
        for i, h in enumerate(head):
            if n in h:
                return i
    return None

def check(name, head, rows):
    ic, it, ip = col(head, "screen"), col(head, "target type", "type"), col(head, "position")
    if None in (ic, it, ip):
        return [f"{name}: table needs Screen, Target type and Position columns"]
    screens = [r[ic].lower() for r in rows]
    types = [r[it].lower() for r in rows]
    poss = [r[ip].lower() for r in rows]
    n = len(rows)
    complex_ = n >= 5 or "complex" in name.lower()
    problems = []
    changes = sum(1 for a, b in zip(screens, screens[1:]) if a != b)
    if complex_:
        if len(set(screens)) < 3:
            problems.append(f"only {len(set(screens))} distinct screens, a complex demo needs at least 3")
        if changes < 3:
            problems.append(f"only {changes} screen changes, need at least 3")
    prim = [i for i, t in enumerate(types) if t in PRIMARY]
    if len(prim) > 2:
        problems.append(f"{len(prim)} primary button clicks, the limit is 2")
    if any(i < n - 3 for i in prim):
        problems.append("a primary button click comes before the last 3 steps")
    for i in range(n - 2):
        if types[i] == types[i + 1] == types[i + 2]:
            problems.append(f"steps {i+1} to {i+3} all target a '{types[i]}'")
            break
    if len(set(types)) < 3:
        problems.append(f"only {len(set(types))} target types, need at least 3")
    if len(set(poss)) < 3:
        problems.append(f"targets sit in only {len(set(poss))} positions, need at least 3")
    return [f"{name}: {p}" for p in problems]

def main(paths):
    bad = 0
    for p in paths:
        cards = parse(p)
        if not cards:
            print(f"{p}: no storyboard table found"); bad += 1; continue
        for name, head, rows in cards:
            probs = check(name, head, rows)
            if probs:
                bad += 1
                for x in probs: print("FAIL |", x)
            else:
                types = {r[col(head,'target type','type')].lower() for r in rows}
                print(f"PASS | {name}: {len(rows)} steps, {len({r[col(head,'screen')].lower() for r in rows})} screens, {len(types)} target types")
    print("RESULT:", "FAIL" if bad else "PASS")
    return 1 if bad else 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1:]))
