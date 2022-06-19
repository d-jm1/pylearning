#numpy 介绍
"""numpy数据处理,矩阵计算(based on c and ?? language),pandas复杂数据处理,matplotlib数据可视化"""
import imp
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# c = np.zeros((2,10)) #2行 10列的0
# d = np.ones((5,7)) #5行 7列的1
# f = np.full((3,89),3) #3行 89列的3
# g = np.eye(10) #10 * 10 的单位矩阵
# h = np.random.random((2,3)) #2*3 随机数矩阵
# print(c,d,f,g,h)

# a = np.array([[1,2,3],[5,6,7],[9,10,11]])
# b = a[1:,1:3] #array 的切分类似于 list的切分,a，b存在关联关系(类似list)，相应数据同时变化。
# b = np.array([b[1,1:3],b[2,1:3]]) #另一种切分，a、b不关联 indexing脱关联
# b = a[[0,0,1,1,2,2],[1,2,1,2,1,2]] #另一种切分方法 列表1为行，列表2为列
# b = [0,2,0,1] 
# a[np.arange[3],b] += 100 #array a 个别数据增加100
# print(a[np.arange(3),b]) #依次每行取第b个数(自动迭代)
# print(a)
# print(b)

# 矩阵的布尔判断
# a = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
# b = (a > 7)
# print(b) #输出为布尔类型的array
# print(a[b]) #输出满足b条件的a中的值，以array形式显示 同 print(a[a>7])

# array的四则运算 与数学坐标向量的四则运算一致 np.add(+) np.subtract(-) np.multiply(*) np.devide(/) np.sqrt(开方)
# 矩阵 点乘(dot product/inner product)[https://en.wikipedia.org/wiki/Dot_product] numpy.dot
# a = np.array([[1,2,3],[4,5,6],[1,1,1]])
# b = np.array([[7,8,9],[10,11,12],[1,1,1]])
# print(a.dot(b))
# print(np.dot(a,b))
# print(np.sum(a)) #计算和
# print(np.sum(a,axis = 1)) #axis = 0 列和 axis = 1 行和
# print(a.T) #行列转换

# boardcasting 自动补全？ 3*4的array 与1*4 的array计算时，自动将 1*4 转变为3 * 4的array（根据已有数据补全） 自定义：for i in range(len(a)): c[i,:] = a[i,:]+b
# c = np.empty_like(a) 生成与a相同的 x*y 的矩阵（内部数据是随机数） ones_like(),zeros_like 


# from pytest import yield_fixture
# v = np.array(list(range(1,11))) #made a mistake cause someone named the file numpy.py...
# m = np.array([list(range(1,11)),list(range(10,0,-1))],dtype=float) #dtype(int char float double complex虚数 bool)修改数据类型
# # print(v)
# # print("------------------------------------------------")
# # print(m)
# # print("------------------------------------------------")
# # print(type(v))
# # print("------------------------------------------------")
# # print(m.shape) #显示数据的行数，列数
# # print(np.shape(v)) 
# # print("------------------------------------------------")
# # print(m.size)
# # print(np.size(v))
# # print("------------------------------------------------")
# # print(v.dtype) #显示数据类型
# m[0,0] = 1900 #同类型数据，可替换
# '''m[0,0]="my name is ??" 此时由于数据类型不一致出现报错'''
# print(m)