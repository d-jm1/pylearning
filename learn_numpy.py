#numpy 介绍
"""numpy数据处理,矩阵计算(based on c and ?? language),pandas复杂数据处理,matplotlib数据可视化"""
import numpy as np
from pytest import yield_fixture
v = np.array(list(range(1,11))) #made a mistake cause someone named the file numpy.py...
m = np.array([list(range(1,11)),list(range(10,0,-1))],dtype=float) #dtype(int char float double complex虚数 bool)修改数据类型
# print(v)
# print("------------------------------------------------")
# print(m)
# print("------------------------------------------------")
# print(type(v))
# print("------------------------------------------------")
# print(m.shape) #显示数据的行数，列数
# print(np.shape(v)) 
# print("------------------------------------------------")
# print(m.size)
# print(np.size(v))
# print("------------------------------------------------")
# print(v.dtype) #显示数据类型
m[0,0] = 1900 #同类型数据，可替换
'''m[0,0]="my name is ??" 此时由于数据类型不一致出现报错'''
print(m)