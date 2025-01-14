square = [x**2 for x in range(1,11)]
print('cuadrados:', square)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) * 32 for temp in celsius]
print(fahrenheit)

evens = [x for x in range(1,21) if x%2 == 1]
print(evens) 

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
#lo siguiente es una compresion list
transposed = [[row[i] for row in matrix] for i in range (len(matrix[0]))] 
print(matrix)
print(transposed)

transposed = []
for i in range (len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
        transposed.append(transposed_row)

        #es lo mismo que lo de arriba pero sin compresion list

lista = [1,2,3,4,5]
doble = [doub * 2 for doub in lista]
print(doble)

palabras = ["sol", "mar", "montaña", "rio", "estrella"]
#bien = [y.capitalize() for y in palabras if len(y) > 3] 
#print(bien)

filtered_words = [word.capitalize() for word in palabras if len(word) > 3 ]
print(filtered_words)

numeros = [1,2,3,4,5]

prima = [1,2,3,4,5]
beta = [u * 2 for u in prima ]
print(beta)

GranPalabra = [ e.capitalize() for e in palabras if len(e) > 3]
print(GranPalabra)

datos = ['juan', 30, 'ingeniero']
tipos = ['nombre', 'edad','ocupacion']

diky = [{tipos[i]: datos[i]} for i in range(len(datos))]
print(diky)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

tarapuesta = [[row[i] for row in matriz] for i in range(len(matriz[0]))]
print(tarapuesta)
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

madril = [pepe['nombre'] for pepe in personas if pepe['ciudad'] == 'Madrid']
print(madril)

parimpa = [1,2,3,4,5,6,7,8,9,10]
per = [e *2 if e % 2 == 0 else e for e in parimpa] 
print(per)   