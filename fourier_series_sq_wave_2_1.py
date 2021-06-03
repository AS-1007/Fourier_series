import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square
L=1
x=np.arange(-L,L,0.001)
y=square(2*np.pi*x)

plt.plot(x,y,'r--')
plt.title("fourier series for square wave ")
plt.show()