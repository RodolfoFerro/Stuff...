# Author: Rodolfo Ferro
# Email: ferro@cimat.mx
# Script: Plotting the Batman logo 
# Based on the section of extra credit from: http://nob.cs.ucdavis.edu/classes/ecs010-2012-04/homework/hw3.html

import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return 2 * np.sqrt((-np.abs(np.abs(x)-1)) * np.abs(3 - np.abs(x))/((np.abs(x)-1)*(3-np.abs(x)))) * \
            (1 + np.abs(np.abs(x)-3)/(np.abs(x)-3))*np.sqrt(1-(x/7)**2)+(5+0.97*(np.abs(x-0.5)+np.abs(x+0.5))-\
            3*(np.abs(x-0.75)+np.abs(x+0.75)))*(1+np.abs(1-np.abs(x))/(1-np.abs(x)))

def f2(x):
    return (-3) * np.sqrt(1-(x/7)**2) * np.sqrt(np.abs(np.abs(x)-4)/(np.abs(x)-4))

def f3(x):
    return np.abs(x/2) - 0.0913722*x**2 - 3 + np.sqrt(1-(np.abs(np.abs(x)-2)-1)**2)

def f4(x):
    return (2.71052 + 1.5 - 0.5*np.abs(x) - 1.35526 * np.sqrt(4-(np.abs(x)-1)**2)) *\
           np.sqrt(np.abs(np.abs(x)-1)/(np.abs(x)-1))+0.9

# We define our intervals for each function
x1_1 = np.linspace(-7,-3,500)
x1_2 = np.linspace(-1,1,500)
x1_3 = np.linspace(3,7,500)
x2_1 = np.linspace(-7,-4,500)
x2_2 = np.linspace(4,7,500)
x3   = np.linspace(-4,4,500)
x4_1 = np.linspace(-3,-1,500)
x4_2 = np.linspace(1,3,500)

plt.figure()  # Create a plt fig
c = 'b'       # Set the color of the logo

# Plot the function for our predefined intervals
plt.plot(x1_1,f1(x1_1),'%s-'%c,linewidth=2)
plt.plot(x1_2,f1(x1_2),'%s-'%c,linewidth=2)
plt.plot(x1_3,f1(x1_3),'%s-'%c,linewidth=2)
plt.plot(x2_1,f2(x2_1),'%s-'%c,linewidth=2)
plt.plot(x2_2,f2(x2_2),'%s-'%c,linewidth=2)
plt.plot(x3,f3(x3),'%s-'%c,linewidth=2)
plt.plot(x4_1,f4(x4_1),'%s-'%c,linewidth=2)
plt.plot(x4_2,f4(x4_2),'%s-'%c,linewidth=2)

plt.xlim([-8,8])  # X-Axis limits
plt.ylim([-6,6])  # Y-Axis limits
plt.grid()        # Plot grid
#plt.axis('off')  # No axis
plt.show()
