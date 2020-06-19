#importing libraries
import random
import matplotlib.pyplot as plt
import math
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import colors
import numpy as np
from matplotlib.ticker import PercentFormatter

#TASK 4

def task4(steps,Pos,prob):
    
    for i in range(steps):
        a = random.randint(0,1)
        if a <=prob:
            Pos = Pos - np.random.uniform(0,1)
        if a >prob:
            Pos = Pos + np.random.uniform(0,1)
##        print("a: ", a)
##        print("Pos: ", Pos)
##        print("__")
    return Pos

def avgPosT4(n): ##plotting
    X = []
    Y = 0
    for i in range(n):
        a = task4(1000,0,0.5)
        X.append(a)
        Y = Y + a
    Y = Y//n

    print('avg Pos =',Y)    
    plt.hist(X,bins = 10)
    plt.title('TASK 4 - STEP SIZE CONTINUOUS RV')
    plt.xlabel('Final positions')
    plt.ylabel('Frequency')

    plt.show()

print(task4(1000,0,0.5))    
print(avgPosT4(1000))
