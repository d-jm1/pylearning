import random

def random_walk(n):
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(["w","s","a","d"])
        if step == "w":
            y += 1
        elif step =="s":
            y -= 1
        elif step == "a":
            x -= 1
        else:
            x += 1
    return (x,y)
for p in range(20):
    one_step = random_walk(10)
    print(one_step)