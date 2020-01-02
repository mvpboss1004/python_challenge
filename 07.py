import numpy as np
from PIL import Image
img = np.array(Image.open('oxygen.png'))
code = []
for i in range(img.shape[1]):
    grey = img[48][i][0]
    if grey==img[48][i][1] and grey==img[48][i][2]:
        if not code or grey!=code[-1][0] or code[-1][1]>=8:
            code.append([grey,1])
        else:
            code[-1][1] += 1
    else:
        break
print(''.join([chr(c[0]) for c in code]))

