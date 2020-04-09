import numpy as np
import matplotlib.pyplot as plt

 
x = np.linspace(-6,6,1000)

T = 2  #Taking the value of T in the question as 2

l = np.sqrt(1/(3*T*T)) #The value at which phase becomes Maximum

y = np.arctan(3*x*T) - np.arctan(x*T) #Phase
y_max = np.arctan(3*T*l)-np.arctan(l*T) #Max Value of Phase

print ("The maximum value of phase Of transfer function occurs at",l,) 
print ("The maximum value is ",y_max)

plt.text(l,y_max,'Maximum Value(0.28,0.52)')

plt.scatter(l,y_max,color="Red")

plt.xlabel('Angular frequency')
plt.ylabel('Phase')
plt.grid()
plt.plot(x,y)
plt.show()
