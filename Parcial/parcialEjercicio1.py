###PaLINDROMO####
def palindromo(palabra):
    return palabra == palabra[::-1]

palabra = input("ingrese una palabra: ")
if palindromo(palabra):
    print(f"{palabra} si es un palindromo")
else:
    print(f"{palabra} no es un palindromo")