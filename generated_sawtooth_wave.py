import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
L=1
x=np.arange(-L,L,0.001)
xp=4*x
y=lambda xp:xp%(2*L)-L
plt.plot(xp,y(xp),'r--')
plt.title("generated sawtooth wave ")
plt.show()