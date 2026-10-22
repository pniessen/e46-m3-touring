#!/usr/bin/env python3
"""Measure lines quickly:  python3 mw.py CLASS "line one" "line two" ...  (mono parts in [brackets])"""
import sys
sys.dont_write_bytecode = True
import ckit
cls, lines = sys.argv[1], sys.argv[2:]
for _ in range(2):
    res = [(ckit.tm_width(cls, ckit.M(s)), s) for s in lines]
    if not ckit.measure_missing():
        break
for w, s in res:
    print(f"{w:7.1f}  {s}")
