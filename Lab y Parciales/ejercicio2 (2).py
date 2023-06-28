a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]
###A###
d = a + b + c
print(d)
###B###
print("pregunta B")
d.insert(-1,20)
print("Agregar el número 20 en la penúltima posición de la lista",d)
###C###
print("pregunta c")
d.sort(reverse=True)
print("orden de la lista decendente",d)
###D###
print("pregunta D")
d.extend([4,5,6])
print(" Insertar la lista [4,5,6] en la última posición de la lista ordenada",d)
###E###
print("pregunta E")
sum_d=sum(d)
print("La suma de todos los numeros son",sum_d)
###F###
print("pregunta F")
avg_d = sum_d/len(d)
print("el promedio simple de la lista es",avg_d)