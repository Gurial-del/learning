import random


def jugar():
    print("Que le parece si jugamos un jueo? Ser llamado {}, el juego se llama adivina el numero" .format(nombre))
    random_number = random.randint(1, 100)
    input_number = int(input('Ingrese un numero entre 1 y 100:'))
    
    while input_number != random_number:
        if input_number < random_number:
            print('El numero es mayor')
        else:
             print('El numero es menor')
        input_number = int(input('Ingrese un numero entre 1 y 100:'))
    print('Felicidades, has adivinado el numero')

nombre = input('Ingrese su nombre:')
#siempre el input son de tipo str
edad = int(input('Ingrese su edad:'))
print('Buenos dias', nombre, 'de', edad, 'años de edad')

print('Buenos dias {} de {} años de edad'.format(nombre, edad))

jugar()

while True:
    seguir = input('Desea jugar de nuevo? (s/n)')
    if seguir == 's':
        jugar()
    else:
        break