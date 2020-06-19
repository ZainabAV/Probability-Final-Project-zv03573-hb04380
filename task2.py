#importing libraries
import random
import matplotlib.pyplot as plt
import math
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import colors
import numpy as np
from matplotlib.ticker import PercentFormatter


# TASK 2

# assuming it takes 1 second for a person to take each step and they both move at same time and they move each second
# they can rest at one place for 1 second and then move when the next value comes
# P1 = starting position of first person , L1,R1 = probability to move left or right of first person  
# P2 = starting position of second , L2,R2 = probability to move left or right of second person  
# x = number of seconds passed

def task2(P1,L1,R1,P2,L2,R2):    
    x = 0 ##time passed
    while P1 != P2:
        a = random.randint(L1,R1)
        b = random.randint(L2,R2)
        if a <= -1:
            P1 = P1 - 1
        if a >= 1:
            P1 = P1 + 1
        if b <= -1:
            P2 = P2 - 1
        if b >= 1:
            P2 = P2 + 1
        x = x + 1        
    return x
print(task2(0,-1,1,10,-1,1)) ##starting 10 units apart

def task2plot(n): ##plotting
    X = []
    Y = 0

    for i in range(n):
        a = task2(0,-1,1,10,-1,1)
        X.append(a)
        Y =  Y + a
    Y = Y//n
    print('avg Time =',Y)    
    plt.hist(X,bins = 10)
    plt.title('TASK 2')
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.show()
print(task2plot(50)) ##n is the input number this can be increased for a better avg value
