from PIL import Image,ImageDraw
import numpy as np
back = np.array(Image.open('evil1.jpg'))
odd = back.copy()
even = back.copy()
for i in range(back.shape[0]):
    for j in range(back.shape[1]):
        if (i+j)%2 == 0:
            for k in range(3):
                even[i][j][k] = 0
        else:
            for k in range(3):
                odd[i][j][k] = 0
Image.fromarray(odd).show()
Image.fromarray(even).show()
print('evil')
