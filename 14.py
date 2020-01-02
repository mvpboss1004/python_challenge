from PIL import Image
import numpy as np
wire = np.array(Image.open('wire.png'))
flag = np.zeros((100,100), dtype='uint8')
italy = np.zeros((100,100,3), dtype='uint8')
dir_vec = [(0,1), (1,0), (0,-1), (-1,0)]
u = 0
v = -1
d = 0
for idx in range(wire.shape[1]):
    for k in range(4):
        d0 = (d+k)%4
        vec = dir_vec[d0]
        u0 = u + vec[0]
        v0 = v + vec[1]
        if 0<=u0<100 and 0<=v0<100 and flag[u0][v0]==0:
            u = u0
            v = v0
            d = d0
            flag[u0][v0] = 1
            italy[u0][v0] = wire[0][idx]
            break
Image.fromarray(italy).show()