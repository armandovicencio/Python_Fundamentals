# 1.Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]




biggie_size = [- 1, 3, 5, -5]

newlist = [x if x < 0  else "big" for x in biggie_size]

print(newlist)


# 2. Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives([- 1, 1, 1,1 ]) cambia la lista original a [-1, 1, 1, 3] y la devuelve
# Ejemplo: count_positives([1, 6, -4, -2, -7, -2]) cambia la lista a [1, 6, -4, -2, -7, 2] y la devuelve

def countPositives(arr):

    count = 0

    for num in range(len(arr)):
        if arr[num] > 0:
            count = count + 1

    arr[len(arr) - 1] = count

    print(arr)
    return arr


countPositives([1, 6, -4, -2, -7, -2])


# 3. Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7

suma = 0
for i in [1, 2, 3, 4]:
    suma = suma + i
print(f"{suma}")

#4. Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

lista=([1,2,3,4])
suma = 0
for i in [1, 2, 3, 4]:
    suma = suma + i
print(suma/len(lista))


# 5. Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0

list=([37,2,1, -9])
print(len(list))
print(len([]))


# 6. Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. 
# Si la lista está vacía, haga que la función devuelva False.


lista=([1,2,3,4,89])

print(min([int(num) for num in lista]))


# 7. Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False
lista=([1,2,3,4,89])

print(max([int(num) for num in lista]))

# 8. Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, 
# promedio, mínimo, máximo y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) 
# debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}

def UltimateAnalyze(arr):

    total = 0
    minimum = arr[0]
    maximum = arr[0]
    count = 0

    if arr == []:
        return False

    for num in range(len(arr)):
        total = total + arr[num]
        count = count + 1

        if arr[num] < minimum:
            minimum = arr[num]
        elif arr[num] > maximum:
            maximum = arr[num]

    average = total / count
    summary = {"Total": total, "Average": average,
               "Minimum": minimum, "Maximum": maximum, "Length": count}

    print(summary)
    return summary
UltimateAnalyze([1, 2, 3, 4, 5, 6, 7, 8, 9])

# 9. Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos.
#  Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

reverse_list =([37,2,1, -9])

reverse_list.reverse()
print(reverse_list)
