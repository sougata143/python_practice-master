import matplotlib.pyplot as plt
import numpy as np

# compute the x and y  coordinates for points on a sine curve
x = np.arange(0, 3*np.pi, 0.15)
y = np.sin(x)
plt.title("sine wave form")

#plot the points using matplotlib
plt.plot(x,y)
plt.show()