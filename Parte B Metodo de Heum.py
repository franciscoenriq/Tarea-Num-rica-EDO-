#Importamos las librerias necesarias
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

# para delta t= 1 :
N= 240
#Donde N corresponde a el total de subintervalos a considerar

x=np.linspace(inicio,final,N+1)
h= (final-inicio)/N
y=np.zeros(N+1)
#Valores que indican en el enunciado para las ecuaciones

R=0.1
CeCw=0.27
gama1=1
gama2=0.164
a=0.612
#delta para la ecuacion con retardo 
d=5
#aplicamos las condiciones iniciales pedidas
for i in range(d):
    y[i]=1
#definimos nuestro delta a utilizar como se dice a continuacion
#para que sea conciso con los diferentes valores de N que como ya
#se a dicho dependen de nuestro delta tiempo
delta=int(d/h)
#definimos este yprima para poder programar la edo con retardo
#en teoria no lp vamos a utilizar pero lo necesitamos definir
#para que python no tire error
yprima=np.zeros(N+1)
#definimos la edo con retardo 
def f(x,y,yprima):
    ec = R*y-a*gama1*CeCw*yprima
    return ec

def heum(h,x,y,yprima):
    ytongo = y + h*f(x,y,yprima)
    ec= f(x,y,yprima) + f(x+h, ytongo,yprima)
    return ec*(h/2.0)
for i in range(len(x)-1):
    y[i+1] = y[i] + heum(h,x[i],y[i],y[i-delta])
plt.plot(x,y,"-")
plt.show()



