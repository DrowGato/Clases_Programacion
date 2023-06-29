#Escribir un programa que le pregunte al usuario su nombre y edad,
#y luego calcule y imprima cuantos años tendra en 20 años.
#El programa debe imprimir una cadena de las siguientes forma:

#"hola mi nombre es [Nombre], tengo [edad] años y en 20 años tendre [total] años"

#INICIAR RETO

nombre = input ("¿cual es tu nombre?\n")
edad =input ("cual es tu edad?\n")
total = 20 + int(edad)

print(f"hola mi nombre es {nombre}, tengo {edad} años y en 20 años tende {total} años ")