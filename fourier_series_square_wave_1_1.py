#𝒇(𝒙) = {
#𝟎, −𝑳 ≤ 𝒙 ≤ 𝟎
#𝟏, 𝟎 ≤ 𝒙 ≤ L
#f(x) has period 2L

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square
L=1
x=np.arange(-L,L,0.001)
y=square(x)
plt.plot(x,y,'r--')

plt.title("fourier series for square wave ")
plt.show()


