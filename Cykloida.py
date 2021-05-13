import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

print("Podaj parametry odpowiednich krzywych:")
print("1. Normalnej cykloidy:")
r1 = float(input("Podaj promień koła: "))
print("Współrzędne środka okręgu")
x0_0=float(input("x0= "))
y0_0=float(input("y0= "))
print("2. Epicykloidy na elipsie:")
a1 = float(input("Długość promienia osi x elipsy: "))
b1 = float(input("Długość promienia osi y elipsy: "))
r2 = float(input("Długość promienia koła toczącego: "))
print("Współrzędne środka elipsy")
x0_1=float(input("x0= "))
y0_1=float(input("y0= "))
print("2. Hipocykloidy na elipsie:")
a2 = float(input("Długość promienia osi x elipsy: "))
b2 = float(input("Długość promienia osi y elipsy: "))
r3 = float(input("Długość promienia koła toczącego: "))
print("Współrzędne środka okręgu")
x0_2=float(input("x0= "))
y0_2=float(input("y0= "))

def circle(x0=0.,y0=1.,color='r',r=1.):
    t=np.arange(0,2*np.pi,1./100)
    x=np.cos(t)*r+x0
    y=np.sin(t)*r+y0
    plt.plot(x,y,color=color)

def prosta(x0=0.,y0=0.,color='g'):
    d=np.arange(x0,x0+7,0.1)
    x=d+x0
    y=np.zeros((x.shape))+y0
    plt.plot(x,y,color=color)

def krzywa_prostej(x0=0.,y0=1.,color='y',r=1.):
    t=np.arange(0,2*np.pi,1./100)
    x=t-np.sin(t) + x0
    y=1-np.cos(t) + y0 - r 
    plt.plot(x,y,color=color)

plt.figure(figsize=(12,5))
plt.subplot(131)
plt.axis('equal')
circle(x0_0,y0_0,'r',r=r1)
krzywa_prostej(x0_0,y0_0,r=r1)
prosta(x0_0,y0_0-r1)

def elipsa(x0=0.,y0=1.,color='g',a=2.,b=1.):
    t=np.arange(0,2*np.pi,1./100)
    x=np.cos(t)*a+x0
    y=np.sin(t)*b+y0
    plt.plot(x,y,color=color)

def krzywa_elipsy(x0=0.,y0=0.,color='m',r=1.,a=2.,b=1.):
    t=np.arange(0,2*np.pi,1./100)
    x=(a+r)*np.cos(t) - r * np.cos( ((a+r)/r) * t) + x0
    y=(b+r)*np.sin(t) - r * np.sin( ((b+r)/r) * t) + y0
    plt.plot(x,y,color=color)

plt.subplot(132)
plt.axis('equal')
elipsa(x0_1,y0_1,a=a1,b=b1)
krzywa_elipsy(x0_1,y0_1,r=r2,a=a1,b=b1)

def krzywa_elipsy2(x0=0.,y0=0.,color='r',r=1.,a=2.,b=1.):
    t=np.arange(0,2*np.pi,1./100)
    x=(a-r)*np.cos(t) + r * np.cos( ((a-r)/r) * t) + x0
    y=(b-r)*np.sin(t) - r * np.sin( ((b-r)/r) * t) + y0
    plt.plot(x,y,color=color)

plt.subplot(133)
plt.axis('equal')
elipsa(x0_2,y0_2,a=a2,b=b2)
krzywa_elipsy2(x0_2,y0_2,r=r3,a=a2,b=b2) 

plt.show()
