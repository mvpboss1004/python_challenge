from re import findall
with open('equality.txt') as f:
    print(''.join(findall('[^A-Z][A-Z]{3}(?P<small>[a-z])[A-Z]{3}[^A-Z]', f.read())))