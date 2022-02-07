# Cambia el valor 10 en x a 15.
#  Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x = [ [5,2,3], [10,8,9] ] 
x[1][0]= 15
print (x)

# Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
# students[0] = {'first_name': 'Michael', 'last_name': 'Bryant'}
# print(students)

students[0] = ({'first_name':  'Michael','last_name': 'Bryant'})
print (students)


# En el directorio sports_directory, cambia 'Messi' a 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}


x= sports_directory.values()
print(x)
sports_directory ['soccer'] = 'Andres', 'Ronaldo', 'Rooney'
print(x)

# Camba el valor 20 en z a 30

z = [ {'x': 10, 'y': 20} ]
z[0]=  {'x': 10,'y': 30}
print (z)


# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


    # 3. Obtén valores de una lista de diccionarios
def iterateDict(dict):
    for student in students:
        for key, val in student.items():
            print(key, " - ", val)

iterateDict(students)

# 4. Itera a través de un diccionario con valores de listas

def iterateDictionary2(first_name, students):
    for student in students:
        for val in student.items():
            print(val)


def iterateDict2(lookup, dict):
    for student in students:
        print(student[lookup])

iterateDict2('first_name', students)






dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printDojoInfo(list):
    for key in dojo:
        print(len(dojo[key]))
        print(key)
        for val in dojo[key]:
            print(val)

printDojoInfo(dojo)







