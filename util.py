import pickle
import matplotlib.image as mping
import numpy as np
import math


def decidedistrict(num):
    if num>=0 and num <=63:
        return 0
    elif num>63 and num <=127:
        return 1
    elif num>127 and num <=191:
        return 2
    elif num>191 and num <=255:
        return 3
    else:
        print('Error!')

def extract_vectors(lena):
    color_array = np.zeros((4,4,4))
    for i in range(lena.shape[0]):
        for j in range(lena.shape[1]):
            pixel = lena[i][j]
            if pixel.shape == ():
                num1 = decidedistrict(pixel)
                num2 = decidedistrict(pixel)
                num3 = decidedistrict(pixel)
            else:
                num1 = decidedistrict(pixel[0])
                num2 = decidedistrict(pixel[1])
                num3 = decidedistrict(pixel[2])
            color_array[num1][num2][num3] += 1
    color_array = np.reshape(color_array,64)
    return color_array

def count_distance(vec1,vec2):
    vec1_transpose = np.transpose(vec1)
    vec2_transpose = np.transpose(vec2)
    vec1_mo = math.sqrt(np.sum(np.multiply(vec1,vec1_transpose)))
    vec2_mo = math.sqrt(np.sum(np.multiply(vec2,vec1_transpose)))
    return np.sum(np.multiply(vec2,vec1_transpose))/(vec1_mo*vec2_mo)

# a = np.array([[1],[2]])
# b = np.array([1,2])
# print(np.dot(b,a))
