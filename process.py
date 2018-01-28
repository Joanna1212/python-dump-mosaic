import pickle  
import matplotlib.image as mping
import numpy as np
import util
import os
import sys

# lena = mping.imread('.\\assets\\thumb\\c10-p4-12.jpg')
# # lena2 = mping.imread('2.jpg')
# # lena1 = mping.imread('1.jpg')
# vec = util.extract_vectors(lena)
# print(vec)
# vec1 = util.extract_vectors(lena1)
# vec2 = util.extract_vectors(lena2)
# print(util.count_distance(vec,vec1))
# print(util.count_distance(vec,vec2))

fileList = []
dir = '.\\assets\\thumb'
def GetFileList(dir,fileList):
    newDir = dir
    if os.path.isfile(dir):         # 如果是文件则添加进 fileList
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):   # 如果是文件夹
            newDir = os.path.join(dir, s)
            GetFileList(newDir, fileList)
    return fileList
fileList = GetFileList(dir,fileList)
data = []
with open('dic.pkl', 'wb') as f:
    for item in fileList:
        print(item)
        lena = mping.imread(item)
        vec = util.extract_vectors(lena)
        dic = {'data': vec, 'path': item}
        data.append(dic)
    pickle.dump(data, f)
# 反序列化