import random
from re import X

from more_itertools import one, random_combination

def random_walk_V2(n):
    x,y = 0,0
    for i in range(n):
        dx,dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return (x,y)

walk_times = 50
walk_step = 100
how_far = 0
call_taxi_times = 0
for i in range(walk_times):
    one_walk = random_walk_V2(walk_step)
    how_far = abs(one_walk[0])+abs(one_walk[1])
    if (how_far >= 20):
        print("you will need a texi to go back home!\nwhere you are is:{}".format(one_walk))
        call_taxi_times += 1
    else:
        print("you can go home by your foot!\nwhere you are is:{}".format(one_walk))
print("the times of you call taxi to go home is:{}".format(call_taxi_times))


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