# Básico : imprime todos los enteros del 0 al 150.

for i in range(151):
    print(i)

# Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000

count = 5
while count < 1000:
    print(count)
    count += 5


# Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. 
count = 0
while count < 100:
    count += 1
    if count % 5 == 0:
        print("Coding")
    else: print(count)
   
# Si es divisible por 10, imprima "Coding Dojo".
count = 0
while count < 100:
    count += 1
    if count % 10 == 0:
        print ("CodingDojo")
        count += 1
    else: print(count)

# ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
suma = 0
for i in range(1,500000):
    if i % 2 != 0:
        suma += i
        print(suma)

# Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
i=0
for i in range(2018,0, i-4):
    print (i)
# Contador flexible : establece tres variables: lowNum, highNum, mult.
# Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. 
# Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
lowNum=2 
highNum=9 
mult=3 
for i in range(lowNum,highNum+1):  
 if i% mult==0:  
  lowNum+=1  
  print(i)  

# BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000?

start = 1
end = 1000
  
for i in range(start, end+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i) 



        