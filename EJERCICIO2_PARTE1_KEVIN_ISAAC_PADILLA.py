##Realizado por: "Kevin Isaac Padilla"      

Datos_2021=[1,2,3,4,5,6,7,100,91,110,900,21,33,32,2,4,8,10,13,13,16,15,1302]
varp=[]
vari=[]
datos_at=[]

for var1 in Datos_2021:
    
    if var1%2 == 0:
        varp.append(var1)
    elif var1%2 ==1:
        vari.append(var1)

print(f"Pares: {varp} \nImpares: {vari} ")

##Para los datos atípicos podriamos decir que son aquellos menores al 25% del promedio
#y aquellos mayores al 75% del promedio.

prom=sum(Datos_2021)/len(Datos_2021)
lim_mayor= prom*0.95
lim_menor=prom*0.05

for var0 in Datos_2021:
    
    if var0<lim_menor or var0>lim_mayor:
        datos_at.append(var0)
print(f"Datos Atípicos: {datos_at}")
    