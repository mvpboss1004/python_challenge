import pickle
with open('banner.p','rb') as f:
    hint = pickle.load(f)
print(hint)
for line in hint:
    text = ''
    for seg in line:
        text += seg[0]*seg[1]
    text += '\n'
    print(text)