#!/usr/bin/env python3
import sys
import csv

# Keyword sets for sentiment classification
POSITIVE_WORDS = {"good", "great", "awesome", "fantastic", "love", "amazing", "excellent", "best", "enjoy", "like"}
NEGATIVE_WORDS = {"bad", "terrible", "awful", "worst", "hate", "boring", "poor", "dislike", "bug", "issue"}

def classify_sentiment(text):
    text = text.lower()
    pos = sum(word in text for word in POSITIVE_WORDS)
    neg = sum(word in text for word in NEGATIVE_WORDS)
    if pos > neg:
        return "positive"
    elif neg > pos:
        return "negative"
    else:
        return "neutral"

reader = csv.reader(sys.stdin)
for row in reader:
    if len(row) < 5 or row[4].lower() == "review_text":
        continue
    text = row[4]
    sentiment = classify_sentiment(text)
    print(f"{sentiment}\t1")
