diccionario={}

cantAlumnos=int(input("ingrese la cantidad de alumnos: "))
for i in range(cantAlumnos):
    nombre=input("ingrese el nombre del alumno: ")
    listanotas = []
    nota=int(input("ingrese la nota :"))

    while nota>0:
        listanotas.append(nota)
        nota=int(input("ingrese la nota :"))

    suma=0
    for i in range(len(listanotas)):
        suma=suma+listanotas[i]
    promedio=suma/len(listanotas)
    diccionario[nombre]=promedio

for key in diccionario:
    print(key, ":", diccionario[key])
