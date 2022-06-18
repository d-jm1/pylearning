"""类的概念,有点类似Java"""

from unicodedata import name


class User:

    def __init__(self,fullname,birthday): #类初始化
        self.name = fullname
        self.birthday = birthday
        name_splits = fullname.split(' ') #split方法：按空格切分数据
        self.first_name = name_splits[0]
        self.last_name = name_splits[-1]

    pass

user1 = User("monkey D luffy",'2022-03-04')
print(user1.name+"\n"+user1.first_name+"\n"+
user1.last_name+"\n"+user1.birthday)#测试测试
"""
user1 = User()
user1.first_name = 'William'
user1.last_name = 'Mace'
user1.age = 18
print(user1.first_name,user1.last_name,user1.age)
"""
