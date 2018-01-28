import pickle  
import matplotlib.image as mping
import numpy as np
import util
import os
import sys
import scipy.misc

with open('dic.pkl','rb') as f:
    data = pickle.load(f)

lena = mping.imread('input.jpg')
print(lena.shape)
row = int(np.floor(lena.shape[0]/20))
col = int(np.floor(lena.shape[1]/20))
print(row)
print(col)

output = np.zeros((row*20,col*20,3))
for i in range(row):
    for j in range(col):
        grid = np.ones((20,20,3))
        for m in range(20):
            for n in range(20):
                grid[m][n] = lena[i*20+m][n+j*20]
        #替换
        max_name = ''
        max_distance = 0
        for item in data:
            origin_vector = util.extract_vectors(grid)
            distance = util.count_distance(item['data'],origin_vector)
            if distance>max_distance:
                max_distance = distance
                max_name = item['path']
        subtitude_image = mping.imread(max_name)
        for m in range(20):
            for n in range(20):
                output[i*20+m][n+j*20] = subtitude_image[m][n]
scipy.misc.imsave('output.jpg', output)
    