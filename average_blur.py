from PIL import Image
from math import pi, log, exp
import numpy as np

def average_blur(img, r):
    w, h = img.size
    a = np.array(img.getdata(), dtype=np.uint8).reshape(h, w)
    b = np.zeros((h,w), dtype=np.uint8)
    for i in range(r, h - r):
        for j in range(r, w - r):
            s = 0.
            for x in range(-r, r):
                for y in range(-r, r):
                    s+=a[i+x,j+y]
            b[i,j] = s / (2*r+1)**2
    return Image.fromarray(b)

img = Image.open('darwin.png')
img.load()

print("Image size is", img.size)
print("Image mode is", img.mode)

print("getdata[1]=", img.getdata()[1])
a = np.array(img, dtype=np.uint8).reshape(img.size[::-1])
print("a[0,1]=", a[0,1])

b = a[900:1150, 900:1100]
pic = Image.fromarray(b)

blur_np(pic,16).show()