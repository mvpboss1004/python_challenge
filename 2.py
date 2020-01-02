from collections import defaultdict
with open('ocr.txt') as f:
    text = f.read()
ocr = defaultdict(int)
for c in text:
    ocr[c] += 1
print(ocr)