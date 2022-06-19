'''从kaggle网站下载并导入关于diabetes的csv文件以学习pandas库'''
import pandas as pd

# pd.set_option("display.max_rows",1000) # code多行同时写快捷键 alt+shift、alt 
# pd.set_option("display.max_columns",100)

# pd.read_csv("/home/djm/workplace/python/diabetes.csv") # download csv file from https://www.kaggle.com/datasets/mathchi/diabetes-data-set
cols_name = ["user1","user2","user3","user4","user5","user6","user7","user8","user9"]
df = pd.read_csv('python/diabetes.csv',dtype=str) #emmmmmm 相对路径总是从编辑的文件路径出发...然后报错...
df1 = pd.read_csv('python/diabetes.csv',index_col= 0,header=None,names= cols_name) #指定第x行第y列为index header ,name指定header名[不可同名，会报错]
# print(df.head()) #打印头五行数据
# print(df1)
# print(type(df))                 #dateframe（整张表） 和 series（某一列） 数据类型 [i have already forgot the password of MySQL...]
# print(type(df["Pregnancies"]))  

# print(df["Pregnancies"])        #打印Prenancies列数据
# print(df.Pregnancies)           #打印Prenancies列数据,不能为pandas已经定义的关键字和数字
# print(df.Pregnancies+df.BMI)    #Series类型数据相加
# print(df.Pregnancies + ',' + df.BMI)#series分隔显示(dtype 必须为str...看见报错就烦死了)
# df["new series"] = df.Pregnancies + ',' + df.BMI #添加新列数据
# print(df)