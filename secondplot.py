import numpy as np
import matplotlib.pyplot as plt

def f(x,a,b,c):
    return a*x**2+b*x+c

xlist = np.linspace(-10,10,num=1000)
ylist = f(xlist,3,1,4)
plt.figure(num=0,dpi=120)

plt.plot(xlist,ylist,label="f(x)")
plt.plot(xlist,ylist**(1/2),label="f(x)**1/2")
plt.title("Plotting Example")
plt.xlabel("Distance /  ft")
plt.ylabel("Height /  ft")
plt.legend()
plt.show()




