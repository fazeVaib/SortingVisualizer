import random

def generateData(n=100):
    colors = ['lightslategray', ] * n
    y = [random.randint(1, 250) for i in range(0, n)]
    return y, colors
