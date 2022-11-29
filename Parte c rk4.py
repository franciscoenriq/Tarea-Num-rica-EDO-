import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
#definimos los valores que recorre el eje x 
r=0.1
R=0.1
CeCw=0.27
gama1=1
gama2=0.164
alfa=0.612
#Valores que recorrera el eje x
inicio=0
final=240
N=48000
#Establemos estos valores como vectores , como ya se ha hecho en partes anteriores
x=np.linspace(inicio,final,N+1)
h= (final-inicio)/N
y=np.zeros(N+1)
w=np.zeros(N+1)
#Condiciones iniciales 
y[0]=1
w[0]=-1
#definimos las dos funciones a considerar
def f1(x,y,w):
    return R*y+gama2*CeCw*w
def f2(x,y,w):
    return -r*w-alfa*y
#Definimos el paso RK4 
def pasork4_1(h,x,y,w):
    g1_1=f1(x,y,w)
    g1_2=f1(x + (h/2),y + (h/2)*g1_1,w + (h/2)*g1_1)
    g1_3=f1(x + (h/2),y + (h/2)*g1_2,w + (h/2)*g1_2)
    g1_4=f1(x + h,y + h*g1_3,w + h*g1_3)
    return (h/6)*(g1_1+(2*g1_2)+(2*g1_3)+g1_4)
def pasork4_2(h,x,y,w):
    g2_1=f2(x,y,w)
    g2_2=f2(x + (h/2),y + (h/2)*g2_1,w + (h/2)*g2_1)
    g2_3=f2(x + (h/2),y + (h/2)*g2_2,w + (h/2)*g2_2)
    g2_4=f2(x + h,y + h*g2_3,w + h*g2_3)
    return (h/6)*(g2_1+(2*g2_2)+(2*g2_3)+g2_4)
#Aplicamos RK4 para el sistema de ecuaciones 

for i in range(len(x)-1):
    y[i+1]=y[i]+pasork4_1(h,x[i],y[i],w[i])
    w[i+1]=w[i]+pasork4_2(h,x[i],y[i],w[i])
    
        
plt.plot(x,y,"-")
plt.show()
