import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth
from scipy.integrate import quad
from math import* # import all function from math
x=np.arange(-np.pi,np.pi,0.001)
y=sawtooth(x)
#define fuction
fc=lambda x:sawtooth(x)*cos(i*x)
fs=lambda x:sawtooth(x)*sin(i*x)

n=50
An=[]
Bn=[]
sum=0
for i in range(n):
 an=quad(fc,-np.pi,np.pi)[0]*(1.0/np.pi)
 An.append(an)

for i in range(n):
 bn=quad(fs,-np.pi,np.pi)[0]*(1.0/np.pi)
 Bn.append(bn)

for i in range(n):
 if i==0.0:
    sum = sum+(An[i]/2)
 else:
    sum=sum+(An[i]*np.cos(i*x)+Bn[i]*np.sin(i*x))

print("sum=", sum)
plt.plot(x,sum,'g')
plt.plot(x,y,'r--')
plt.title("fourier series for sawtooth wave n=50")
plt.show()

