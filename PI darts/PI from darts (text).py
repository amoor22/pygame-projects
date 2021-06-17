import random, math
def throw(num):
    inside = 0
    outside = 0
    for i in range(num):
        x = random.random()
        y = random.random()
        if math.sqrt((x ** 2) + (y ** 2)) < 1:
            inside += 1
        outside += 1
    return (inside / outside) * 4
print(throw(1000000))