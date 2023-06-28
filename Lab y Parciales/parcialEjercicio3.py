
temp_min = {9, 5, 2, 7, 6, 1}
temp_max = {12, 14, 11, 10, 15, 9}
####A####
if 9 in temp_min & temp_max:
    print("la temperatura 9°C si esta en unos de los sets")
else:
    print("la temperatura 9°C no esta en el sets")

#####B####
if (6 in temp_min | temp_max) or (17 in temp_min | temp_max):
    print("si hay la temperatura  6°C y 17°C está en alguno de los sets")
else:
    print("no hay temperatura  6°C y 17° en los sets")

####C####


temp_min = {9, 5, 2, 7, 6, 1}
temp_max = {12, 14, 11, 10, 15, 9}
for temp in temp_min:
    temp_min.remove(temp)
    temp_min.add(temp **4  )
 
for temp in temp_max:
    temp_max.remove(temp)
    temp_max.add(temp **4  )
print("todas las temperaturas del minimo fueron elevadas a 4 son :", temp_min)
print("todas las temperaturas del maximo fueron elevadas a 4 son :", temp_max)

#####D

temp_min = {9, 5, 2, 7, 6, 1}
temp_max = {12, 14, 11, 10, 15, 9}

temp_combi = temp_min | temp_max

print(" la combinacion de las 2 temperaturas es :",temp_combi )