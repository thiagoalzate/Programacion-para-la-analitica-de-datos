#Santiago Alzate Quiceno

import pandas as pd
import matplotlib.pylab as plt
import os
import numpy as np
import seaborn as sns
 
file = "file:///Users/santiagoalzate/Desktop/PROGRAMACION%20PARA%20LA%20ANALITICA%20DE%20DATOS/Wine/winequality-red.csv"
file2 = "file:///Users/santiagoalzate/Desktop/PROGRAMACION%20PARA%20LA%20ANALITICA%20DE%20DATOS/Wine/winequality-white.csv"

headers = ["Fixed acidity", "volatile acidity", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "ph", "sulphates", "alcohol", "quiality"]

df1 = pd.read_csv(file, sep=";" )
df2 = pd.read_csv(file2, sep=";")

#df  = pd.merge(df1, df2)
df1.head()
df2.head()

#A continuacion despues de leer los archivos se procede a generar la cabeza de la tabla

print(df1.dtypes)
print(df2.dtypes)

#Con la funcion dtypes podemos observar que tipo de dato tenemos en cada columna para poder saber que tipo de analisis hacerle

df1.tail() 
df1.info() 
df1.describe() 
df2.tail() 
df2.info() 
df2.describe()

#Con estas funciones lo que buscamos es obtener mas informacion acerca de los datos, mostrandonos un poco acerca de la desviacion estandar
# tambien si existen datos nulos en el dataset y la cantidad de estos

df1.isnull().sum() 
df1['residual sugar'].value_counts() 
df1.duplicated().sum() 
df2.isnull().sum() 
df2['residual sugar'].value_counts() 
df2.duplicated().sum()

#Con estas funciones buscamos hacerle una limpieza al dataset observando cuantos valores nulos hay, cuantos datos duplicados hay
#Como no tenemos datos nulos no es necesario hacer una limpieza en estos sectores

df1.corr()
df2.corr()

#En este caso buscamos correlaciones entre las varialbles

fix_aci = df1["fixed acidity"]
print(fix_aci)
prom = fix_aci.mean()
print(prom)
fix_aci2 = df2["fixed acidity"]
print(fix_aci2)
prom2 = fix_aci2.mean()
print(prom2)

#Aca podemos observar que el segun el promedio de los dos tipos de vino, que el rojo tiene un promedio mayor al blanco en cuanto a fixed acidity

ph = df1["pH"]
print(ph)
prom_ph = ph.mean()
print(prom_ph)
ph2 = df2["pH"]
print(ph2)
prom_ph2 = ph2.mean()
print(prom_ph2)

#Aca podemos observar que el pH que mantienen ambos tipos de vino es muy similar, pero que el rojo tiene el pH un poco mas por encima que el blanco

sug = df1["residual sugar"]

prom_sug = sug.mean()
print(prom_sug)
sug2 = df2["residual sugar"]

prom_sug2 = sug2.mean()
print(prom_sug2)

#Podemos observar que el vino blanco tiene bastante mas cantidad de azucar residual que el vino rojo, teniendo esta casi el doble que el rojo

plt.hist(df1['residual sugar']) 
plt.scatter(df1['volatile acidity'], df1['fixed acidity']) 
plt.bar(df1['alcohol'], df1['quality']) 

plt.hist(df2['residual sugar']) 
plt.scatter(df2['volatile acidity'], df2['fixed acidity']) 
plt.bar(df2['alcohol'], df2['quality']) 

#En estas graficas podemos comparar la relacion que tiene la volatile acidity con la fixed acidity como la relacion entre la calidad del vino con la cantidad de alcohol que tiene








