#numpy 介绍
"""numpy数据处理,矩阵计算(based on c language),pandas复杂数据处理,matplotlib数据可视化"""
import numpy as np
v = np.array(list(range(1,11))) #made a mistake cause someone named the file numpy.py...
m = np.array([list(range(1,11)),list(range(10,0,-1))])
print(v)
print("------------------------------------------------")
print(m)
print("------------------------------------------------")
print(type(v))