import random
from re import X

from more_itertools import random_combination

def random_walk_V2(n):
    x,y = 0,0
    for i in range(n):
        dx,dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return (x,y)

for i in range(10):
    one_walk = random_walk_V2(100)
    print(one_walk)


# def random_walk(n):
#     x = 0
#     y = 0
#     for i in range(n):
#         step = random.choice(["w","s","a","d"])
#         if step == "w":
#             y += 1
#         elif step =="s":
#             y -= 1
#         elif step == "a":
#             x -= 1
#         else:
#             x += 1
#     return (x,y)
# for p in range(20):
#     one_step = random_walk(10)
#     print(one_step)