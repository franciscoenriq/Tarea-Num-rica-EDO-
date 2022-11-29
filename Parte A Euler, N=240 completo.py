#Importamos las bibliotecas necesarias 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# tenemos un tiempo inicial de 0 meses y uno
#final de 240 meses que corresponde a 20 años
inicio = 0
final = 240
# si tenemos 240 meses,que corresponde a nuestro eje de las x
#tendriamos una subdivision de 240 partes si consideramos un h
# de un mes.Bajo esta logica caluclaremos los delta t que nos piden
#-----------------------------------------------------------------

# para delta t= 1 :
N= 240
#Calculamos mediante el metodo de euler
#Definimos nuestro eje x a partir de las subdivisiones que nos piden
# y a su vez lo hacemos para el eje y el cual contendra solamnete 0
# para que se vaya llenando con los resultados calculados a traves del
#metodo
x=np.linspace(inicio,final,N+1)
#h corresponde al largo del cada subintervalo 
h= (final-inicio)/N
y=np.zeros(N+1)
#Condicion inicial que nos piden 
y[0] = 1
#definimos nuestra edo a resolver 
def f(x,y):
    ec = -0.06524*y
    return ec
#implemnetamos metodo de euler 
for i in range(len(x)-1):
    y[i+1]=y[i]+h*f(x[i],y[i])
    
#ahora vamos a graficar la soluccion analitica
#Definimos y2 como nuestro vector para ir rellenando
#la solucion analitica    
#los resultados de  la funcion
    
y2=np.zeros(N+1)
def funcion(x):
    ec = 1/(np.exp(0.06524*x))
    return ec
for i in range(len(x)):
    y2[i]=funcion(x[i])

#Creamos los graficos , agregamos leyendas , diferente color para cada solucion
#y titulo     
blue_patch=mpatches.Patch(color = "blue",label="Solucion Analitica")
red_patch=mpatches.Patch(color="red",label="Metodo de Euler")
plt.plot(x,y2,color="blue")
plt.plot(x,y,color="red")
plt.title("Solcucion Analitica v/s Metetodo de Euler")
plt.legend(handles=[red_patch,blue_patch])
plt.xlabel("X")
plt.ylabel("Y")    
plt.show()
#calculamos error
Error= np.linalg.norm(y2-y)
Errormax=np.linalg.norm(y2-y,ord=np.inf)
print("El error en norma 2 es:",Error)
print("El error en norma del maximo es:",Errormax)
