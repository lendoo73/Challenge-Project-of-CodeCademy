from random import uniform, seed
import numpy as np

seed(1)

blue_x = []
blue_y = []

red_x = []
red_y = []

#First Blue Column
for i in range(50):
    blue_x.append(uniform(2, 4))
    blue_y.append(uniform(0, 8))

#Horizontal Blue
for i in range(25):
    blue_x.append(uniform(4, 8))
    blue_y.append(uniform(5, 6))

#Left Red
for i in range(30):
    red_x.append(uniform(0,1.9))
    red_y.append(uniform(0, 10))

#Red above blue column
for i in range(15):
    red_x.append(uniform(2, 4))
    red_y.append(uniform(8.1, 10))

#Red below blue horizontal
for i in range(25):
    red_x.append(uniform(4.1,10))
    red_y.append(uniform(0, 4.9))

#Red above blue horizontal
for i in range(25):
    red_x.append(uniform(4.1,10))
    red_y.append(uniform(6.1, 10))

#Smaller blue column
for i in range(10):
    blue_x.append(uniform(6.3, 6.8))
    blue_y.append(uniform(0, 6))


all_x = blue_x + red_x
all_y = blue_y + red_y

points = np.array(list(zip(all_x, all_y)))

labels = np.array([0] * len(blue_x) + [1] * len(red_x))
