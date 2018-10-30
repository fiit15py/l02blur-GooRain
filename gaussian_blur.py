# -*- coding: utf-8 -*-

from PIL import Image
from math import pi, log, exp
import numpy as np
import sys

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

def process(filename, r):
    # должна обрабатывать файл filename гауссовым размытием в квадрате [-r, +r] x [-r, +r] 
    # и записывать результат в <filename>.gaussblurred.png
    img = Image.open(filename)
    img.load()

    dx, dy = np.meshgrid(np.arange(-r, +r + 1, 1.), np.arange(-r, +r + 1, 1.0))
    sigma = 0.38 * r
    gauss_dist = np.exp( -(dx * dx + dy * dy)/(2 * sigma ** 2) ) / (2 * pi * sigma ** 2)
    coeff = gauss_dist / np.sum(gauss_dist)

    # код сюда ....
    w, h = img.size
    a = np.array(img.getdata(), dtype = np.uint8).reshape(w, h)
    b = np.zeros((w, h), dtype = np.uint8)
    startH = r
    startW = r
    endH = h - r
    endW = w - r
    total = h * w
    iteration = 0
    # [ ? ? ? ? ? ? ?]  x = -r, -r + 1, -r + 2, 0, r - 2, r - 1, r = range(-r, r + 1)
    # [ ? ? ? ? ? ? ?]
    # [ ? ? ? ? ? ? ?]
    # [ ? ? ? ? ? ? ?]
    # [ ? ? ? X ? ? ?]  X[i, j] = ?[i - x, j - y] * coeff
    # [ ? ? ? ? ? ? ?]
    # [ ? ? ? ? ? ? ?]
    # [ ? ? ? ? ? ? ?]
    # [ ? ? ? ? ? ? ?]  
    
    for i in range(startW, endW):
        for j in range(startH, endH):
            iteration += 1
            for x in range(-r, r + 1):
                for y in range(-r, r + 1):
                        b[i,j] += a[i + x, j + y] * coeff[r + x, r + y]
                        # print(b[i,j])
                        # printProgressBar(iteration, total, length = 75)
        printProgressBar(iteration, total, length = 75)

    newimg = Image.fromarray(b)
    newimg.save(filename[:-4] + 'gaussblurred-goorain.png')
    print("Success!")

if __name__=='__main__':
    # Запускать с командной строки с аргументом <имя файла>, например: python gauss.py darwin.png
    if len(sys.argv) > 2:
        process(sys.argv[1], int(sys.argv[2]))
    else:
        print("Args{ [0] = filename [1] = radius }.\n")
