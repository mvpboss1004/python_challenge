
with open('evil2.gfx', 'rb') as f:
    content = f.read()
for i in range(5):
    with open('sub%d.jpg'%i, 'wb') as f:
        f.write(content[i::5]) 
