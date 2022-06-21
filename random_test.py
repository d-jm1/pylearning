from matplotlib import pyplot as plt
import random




#开赌开赌,梭哈加卡^-^~~
def give_an_number():
    number = random.randint(1,100)
    # print("-"*5 )
    if number >=51:
#         print("you won the game!~~\nthe number is:{}\n\
# play more to be a rich man~~".format(number))
        return True
    else:
        # print("you lost the game!\nthe number is:{}".format(number))
        return False

# x = 0
# while(x < 100):
#     result = give_an_number()
#     print(result)plt.xlabel("counts")
    plt.ylabel("founds")
    plt.title("there are nothing to say!")
    plt.show()
#     x += 1    
def a_fool(founds,wager,game_counts):
    currently_game_counts = 0
    x = []
    y = []

    while(currently_game_counts <= game_counts):
        if give_an_number():
            founds += wager
        else:
            founds -= wager
            # if founds < wager:
            #     print("get out of the game.\ncause you do not have founds(${}) enough,赌可以,你女儿挺漂亮得嘛(>_<)!".format(founds))
            #     return False
        x.append(currently_game_counts)
        y.append(founds)
        currently_game_counts += 1
    plt.plot(x,y)
    print(founds)
    return True
n = 0
while(n < 100):
    a_fool(100000,1000,10000)
    n += 1
plt.xlabel("counts")
plt.ylabel("founds")
plt.title("there are nothing to say!")
plt.show()



# def random_walk_V2(n):
#     x,y = 0,0
#     for i in range(n):
#         dx,dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
#         x += dx
#         y += dy
#     return (x,y)

# walk_times = 50
# walk_step = 100
# how_far = 0
# call_taxi_times = 0
# for i in range(walk_times):
#     one_walk = random_walk_V2(walk_step)
#     how_far = abs(one_walk[0])+abs(one_walk[1])
#     if (how_far >= 20):
#         print("you will need a texi to go back home!\nwhere you are is:{}".format(one_walk))
#         call_taxi_times += 1
#     else:
#         print("you can go home by your foot!\nwhere you are is:{}".format(one_walk))
# print("the times of you call taxi to go home is:{}".format(call_taxi_times))


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