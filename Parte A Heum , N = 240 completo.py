import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
# tenemos un tiempo inicial de 0 meses y uno
#final de 240 meses que corresponde a 20 años
inicio = 0
final = 240
#para delta igual 1 tenemos
N=240
#para esta parte del codigo se define de la misma manera que en para el metodo de euler
#calculamos eje x, eje y inicialmente con puros 0 para posteriormente ser rellenados
# a medida que el metodo se implementa

x=np.linspace(inicio,final,N+1)
h= (final-inicio)/N
y=np.zeros(N+1)
#condicion inicial
y[0] = 1
#edo a resolver 
def f(x,y):
    ec = -0.06524*y
    return ec
#paso del metetodo de heum 
def heum(h,x,y):
    ytongo = y + h*f(x,y)
    ec= f(x,y) + f(x+h, ytongo)
    return ec*(h/2.0)
#implementamos el algoritmo
for i in range(len(x)-1):
    y[i+1] = y[i] + heum(h,x[i],y[i])
    
#Calculamos la solcion analitica
    
y2=np.zeros(N+1)
def funcion(x):
    ec = 1/(np.exp(0.06524*x))
    return ec
for i in range(len(x)):
    y2[i]=funcion(x[i])
#implementamos los graficos correspondientes 
blue_patch=mpatches.Patch(color = "blue",label="Solucion Analitica")
red_patch=mpatches.Patch(color="red",label="Metodo de Heum")
plt.plot(x,y2,color="blue")
plt.plot(x,y,color="red")
plt.title("Solcucion Analitica v/s Metetodo de Heum")
plt.legend(handles=[red_patch,blue_patch])
plt.xlabel("X")
plt.ylabel("Y")    
plt.show()

