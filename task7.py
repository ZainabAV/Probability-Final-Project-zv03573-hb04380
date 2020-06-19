##TASK 7 step size discrete, angle continuous

#importing libraries
import random
import matplotlib.pyplot as plt
import math
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import colors
import numpy as np
from matplotlib.ticker import PercentFormatter

r=100 #defined radius = 100 units

def task7(t, r): 
    LST = []
        
    
    x_new=y_new=0 ##initializing position at (0,0)
    while(t<1000): ##random walk in 1000 seconds
        theta = random.uniform(0,360) ##angle continuous 0-2*pi
        theta = math.radians(theta)
        step = (random.randrange(0,11,5))/10 ###step size is discrete 0,0.5 or 1
        #print('step: ', step)
        #print('theta: ', theta)
        Pos = (x_new,y_new)
        x = x_new
        y = y_new
        x_new=step*math.cos(theta) + x_new
        y_new=step*math.sin(theta) + y_new
        
        Pos=(x_new,y_new)
        
        #print(Pos) #current position
        D1 = ((x_new)**2 + (y_new)**2)**0.5
        
        D2 = ((x)**2 + (y)**2)**0.5
        #print(D1,D2,D2-D1)

        if D1 > r:    # if Distance from centre greater than radius
            #print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            a = D1 - D2
            b = r - D2
            c = a - b
            #print(a,b,c)
            x_new=b*math.cos(theta) + x
            y_new=b*math.sin(theta) + y
            A = bounce(x_new,y_new,c,theta) 
            x_new = A[0]
            y_new = A[1]
        t+=1
        Pos=(x_new,y_new)
        LST.append(Pos)
    return LST
        #print(Pos)
                
def bounce(x_new,y_new,c,theta):
    x_new=c*math.cos(theta+math.pi) + x_new
    y_new=c*math.sin(theta+math.pi) + y_new
    Z= [x_new,y_new]
    return Z

       
##print(task7(0, r))
                
#print(math.radians(180))
fig, ax = plt.subplots(figsize=(7,7))
fig = plt.gcf()

ax = fig.gca()
circle = plt.Circle((0,0), r, color='green', fill=False)
ax.add_artist(circle)
# plt.savefig("circle.png")

LST = task7(0,r)


xdata, ydata = [], []
ln, = plt.plot(xdata, ydata, color='green')

# initialization function 
def init(): 
    # creating an empty plot/frame 
    ax.set_xlim((-200,200))
    ax.set_ylim((-200,200))
    ax.set_title("TASK 7- DISCRETE STEP SIZE AND CONTINUOUS ANGLE")
    ln.set_data([], []) 
    return ln,

# animation function 
def animate(i):
    xdata.append(LST[int(i)][0])
    ydata.append(LST[int(i)][1])
    ln.set_data(xdata, ydata)
    return ln, 

# call the animator
ani = FuncAnimation(fig, animate, frames=np.linspace(0, len(LST)-1, num=len(LST)), interval=20,
                        init_func=init, blit=True, repeat=False) 
plt.show()
