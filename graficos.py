#import paendas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
plt.xlim(0,180)
plt.ylim(0,60)
plt.title("Primeiro Grafico")
data1= [10,20,30,40,50]
x = 10*np.array(range(len(data1)))
print("valor d eX:", x)
plt.plot(x,data1, 'go') #green
plt.plot(x,data1, 'k:', color = 'orange') #linha pontilhada
plt.grid()
'''
x = y = (1,2,3,4)

# example variable error bar values
yerr = 0


# First illustrate basic pyplot interface, using defaults where possible.
#plt.figure()
plt.errorbar(x, y,yerr=1)
plt.title("Simplest errorbars, 0.2 in x, 0.4 in y")



plt.show()
