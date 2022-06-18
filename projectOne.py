"""类的概念,有点类似Java"""

from tkinter import Y
from unicodedata import name
import datetime #导入时间库函数

class User:

    def __init__(self,fullname,birthday): #类初始化函数
        self.name = fullname
        self.birthday = birthday
        name_splits = fullname.split(' ') #split方法：按空格切分数据
        self.first_name = name_splits[0]
        self.last_name = name_splits[-1]
    
    def age(self):#年龄计算函数
        today = datetime.date(2022,6,18) #datetime.date(2022,6,18)自定义时间
        years = int(self.birthday.split("-")[0])
        months = int(self.birthday.split("-")[1])
        days = int(self.birthday.split("-")[2])
        birth_data = datetime.date(years,months,days)
        Age = (today - birth_data).days/365
        return int(Age)

user1 = User("monkey D luffy",'2000-03-04') #生日20000304，可采用列表切片获取年月日
print(user1.name+"\n"+user1.first_name+"\n"+
user1.last_name+"\n"+user1.birthday)
print("Age:"+str(user1.age()))#测试测试
"""
user1 = User()
user1.first_name = 'William'
user1.last_name = 'Mace'
user1.age = 18
print(user1.first_name,user1.last_name,user1.age)
"""
