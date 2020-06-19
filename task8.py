##TASK 8 

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

def task8(t, r): 
    LST = []
    LST2 = []
    P1 = SETPOS(1)
    P2 = SETPOS(1)

    x_new = P1[0]
    y_new = P1[1]

    x2_new = P2[0]
    y2_new = P2[1]
    
    

    while True:
        theta = random.uniform(0,360) ##angle continuous 0-2*pi
        theta = math.radians(theta)
        step = (random.uniform(0, 1)) ##step size continuous 0-1
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
            Pos=(x_new,y_new)

##for second random point
        theta2 = random.uniform(0,360) ##angle continuous 0-2*pi
        theta2 = math.radians(theta2)
        step2 = (random.uniform(0, 1)) ##step size continuous 0-1
        #print('step: ', step)
        #print('theta: ', theta)
        Pos2 = (x2_new,y2_new)
        x2 = x2_new
        y2 = y2_new
        x2_new=step2*math.cos(theta2) + x2_new
        y2_new=step2*math.sin(theta2) + y2_new
        
        Pos2=(x2_new,y2_new)
        
        #print(Pos) #current position
        D3 = ((x2_new)**2 + (y2_new)**2)**0.5
        
        D4 = ((x2)**2 + (y2)**2)**0.5
        #print(D1,D2,D2-D1)


        if D3 > r:    # if Distance from centre greater than radius
            #print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            a = D3 - D4
            b = r - D4
            c = a - b
            #print(a,b,c)
            x2_new=b*math.cos(theta2) + x2
            y2_new=b*math.sin(theta2) + y2
            B = bounce(x2_new,y2_new,c,theta2)
            x2_new = B[0]
            y2_new = B[1]
            Pos2=(x2_new,y2_new)



        DISTANCE = ((x_new-x2_new)**2+(y_new-y2_new)**2)**0.5
        if DISTANCE < 1:
            break
        
        LST.append(Pos)
        LST2.append(Pos2)
    return LST,LST2
        #print(Pos)
                
def bounce(x_new,y_new,c,theta):
    x_new=c*math.cos(theta+math.pi) + x_new
    y_new=c*math.sin(theta+math.pi) + y_new
    Z= [x_new,y_new]
    return Z


def SETPOS(P):
    
    XC = random.randint(-100,100)
    XY = random.randint(-100,100)
    D = ((XC)**2 +(XY)**2)**0.5
    while D > 100:
        print(D)
        XC = random.randint(-100,100)
        XY = random.randint(-100,100)
        D = ((XC)**2+(XY)**2)**0.5
    return [XC,XY]    


#print(task5(1,100))


       
##print(task5(0, r))
                
#print(math.radians(180))
fig, ax = plt.subplots(figsize=(7,7))
fig = plt.gcf()


ax = fig.gca()
circle = plt.Circle((0,0), r, color='blue', fill=False)
ax.add_artist(circle)
# plt.savefig("circle.png")

a = task8(0,r)
LST = a[0]
LST2 = a[1] 



xdata, ydata = [], []
xdata2, ydata2 = [], []
ln, = plt.plot(xdata, ydata, color='blue')
ln2, = plt.plot(xdata2, ydata2, color='red')


# initialization function 
def init(): 
    # creating an empty plot/frame 
    ax.set_xlim((-200,200))
    ax.set_ylim((-200,200))
    ax.set_title("TASK 8- CONTINUOUS STEP SIZE AND ANGLE")
    ln.set_data([], []) 
    ln2.set_data([], [])
    return ln,ln2,


# animation function 
def animate(i):
    xdata.append(LST[int(i)][0])
    ydata.append(LST[int(i)][1])
    ln.set_data(xdata, ydata)
    xdata2.append(LST2[int(i)][0])
    ydata2.append(LST2[int(i)][1])
    ln2.set_data(xdata2, ydata2)
    return ln,ln2,
   


# call the animator
ani = FuncAnimation(fig, animate, frames=np.linspace(0, len(LST)-1, num=len(LST)), interval=20,
                        init_func=init, blit=True, repeat=False) 
ani = FuncAnimation(fig, animate, frames=np.linspace(0, len(LST2)-1, num=len(LST2)), interval=20,
                        init_func=init, blit=True, repeat=False)                        
plt.show()
