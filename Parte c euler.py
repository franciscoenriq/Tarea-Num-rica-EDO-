#Importamos las librerias necesarias
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
#Anotamos los valores de las contantes que nos da el enunciado
r=0.1
R=0.1
CeCw=0.27
gama1=1
gama2=0.164
alfa=0.612
#definimos los valores que recorre el eje x 
inicio=0
final=240
N=48000

#Establemos estos valores como vectores , como ya se ha hecho en partes anteriores
x=np.linspace(inicio,final,N+1)
h= (final-inicio)/N
y=np.zeros(N+1)
w=np.zeros(N+1)
#condiciones iniciales 
y[0]=1
w[0]=-1
#definimos las dos funciones a calcular 
def f1(x,y,w):
    return R*y+gama2*CeCw*w
def f2(x,y,w):
    return -r*w-alfa*y
#aplicamos el paso de euler para el sistema de ecuaciones 
for i in range(len(x)-1):
    y[i+1]=y[i]+h*f1(x[i],y[i],w[i])
    w[i+1]=w[i]+h*f2(x[i],y[i],w[i])


plt.plot(x,y,"-")
plt.show()








        
                
                
