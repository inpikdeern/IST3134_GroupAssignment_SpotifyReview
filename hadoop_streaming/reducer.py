#!/usr/bin/env python3
import sys

counts = {"positive": 0, "negative": 0, "neutral": 0}

for line in sys.stdin:
    sentiment, count = line.strip().split("\t")
    counts[sentiment] += int(count)

for sentiment, total in counts.items():
    print(f"{sentiment}\t{total}")
