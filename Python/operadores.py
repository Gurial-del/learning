#vamos a imprimir todos los operadores

#suma 
print(f"Esta es la suma de 5 + 4 = {5 + 4}")

#resta
print(f"Esta es una resta de 7 - 3 = {7 - 3}")

#multiplicacion
print(f"Esta es una multiplicacion de 150 * 70 = {150 * 70}")

#Division
print(f"Esta es una division de 955 / 12 = {955 / 12}")

#Division entera. No regresa los puntos decimales INT
print(f"Esta es una division entera de 955 // 12 = {955 // 12}")

#Modulo. Regresa los numeros sobrantes de la division
print(f"Esta es un modulo de 955 % 12 = {955 % 12}")

#Exponenciacion
print(f"Esta es la exponenciacion de dos numeros 9 elevado a 5 es: {9 ** 5}")

#Ahora vamos a ver operadores de comparacion, nos devuelve un valor booleano
#Mayor que 
print(f"5 es mayor que 3: {5 > 3}")

#Menor que
print(f"12 es menor que 47: {12 < 47}")

#Mayor o igual que
print(f"7 es igual que 7: { 7>= 7} y 20 es mayor que 7: {20 >= 7}")

#Menor o igual que
print(f"7 es igual que 7: { 7<= 7} y 5 es menor que 7: {5 <= 7}")

#Igual que
print(f"8 es igual que 8: {8 == 8}")

#Diferente que
print(f"11 es diferente de 15: {11 != 15}")

#Operadores de identidad. Busca en la memoria
number = 5
number = 6 * 4
my_new_number = number
print(f'my number is my_new_number: {number is my_new_number}')
print(f'my number is not my_new_number: {number is not my_new_number}')

#operadores de asignacion
number += 5 
print(f'number =+ 5: {number}') #suma y asigna
number -= 5
print(f'number =- 5: {number}') #resta y asigna
number *= 5
print(f'number =* 5: {number}') #multiplica y asigna
number /= 5
print(f'number =/ 5: {number}') #divide y asigna
number //= 5
print(f'number =// 5: {number}') #divide entero y asigna
number %= 5
print(f'number %= 5: {number}') #modulo y asigna
number **= 5
print(f'number **= 5: {number}') #exponenciacion y asigna

#operadores logicos
#and
print(f'6 > 5 y 3 < 23 es: {6 > 5 and 3 < 23}') #ambas condiciones deben ser verdaderas
#or
print(f'20 < 4 o 3 > 2 es: {20 < 4 or 3 > 2}') #una de las condiciones debe ser verdadera
#not
print(f'not 5 > 3 es: {not 5 > 3}') #invierte el valor booleano

#operadores de pertenencia
print(f''' 'u' in 'curso' es: {'u' in 'curso'} ''') #busca si el caracter esta en la cadena

#condicionales 
my_string = 'Hola caca'

if my_string == 'Hola cara de bola':
    print('Hola cara de bola')
elif my_string == 'Hola caca':
    print('Hola caca')
else:
    print('No es igual')

#Iterativas 
for i in range(11):
    print(i)

i = 0

while i <= 10:
    print (i)
    i += 1

#manejo de excepciones
try: # En caso de que agreguemos algo de otro codigo para que no pete por completo
    print(5/0)
except:     #Si ha caido en error, se maneja la excepcion
    print('Se ha detectado un error')
finally: #Aqui es como un finalizado de un try catch
    print('Ha finalizado el manejo de excepciones')

for i in range(10,56):
    if i % 2 == 0 and i != 16 and i != i% 3 == 0 and i == 10 or 55:
        print(i)
    

    