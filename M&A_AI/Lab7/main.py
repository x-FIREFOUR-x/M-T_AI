import math

countPerson = 10
countGenerations = 10
startRange = range(-4, 1)
crossChance = 0.99
mutationChance = 0.1

def func1(x):
    return math.cos(x/2) + math.sin(x/4) * math.sin(math.cos(x+1))

def func1(x, y):
    return x * math.cos(abs(y))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
