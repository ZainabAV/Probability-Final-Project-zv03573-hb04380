#importing libraries
import random
import matplotlib.pyplot as plt
import math
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import colors
import numpy as np
from matplotlib.ticker import PercentFormatter


#TASK 1

def task1(steps,Pos,L,R):   #L = left probability, R = right probability

    for i in range(steps):
        a = random.randint(L,R)
        if a <= -1:
            Pos = Pos - 1
        if a >= 1:
            Pos = Pos + 1     
    return Pos

def avgPos(n): ##for plotting
    X = []
    Y = 0
    for i in range(n):
        a = task1(1000,0,-1,1)
        X.append(a)
        Y = Y + a
    Y = Y//n

    print('avg Pos =',Y)    
    plt.hist(X,bins = 10)
    plt.title('TASK 1')
    plt.xlabel('Final positions')
    plt.ylabel('Frequency')

    plt.show()

print(task1(100,0,-1,1))    
print(avgPos(1000))

