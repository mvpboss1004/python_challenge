from PIL import Image
import numpy as np
mozart = np.array(Image.open('mozart.gif').convert('RGB'))
align = [0] * mozart.shape[0]
for i in range(mozart.shape[0]):
    cum = 0
    for j in range(mozart.shape[1]):
        if (mozart[i][j]==[255,0,255]).all():
            cum += 1
            if cum>=5:
                align[i] = j
                break
        else:
            cum = 0
straight = np.zeros(mozart.shape, dtype='uint8')
for i in range(mozart.shape[0]):
    for j in range(mozart.shape[1]):
        straight[i][j] = mozart[i][(j+align[i])%mozart.shape[1]]
Image.fromarray(straight).show()        
            
