#sirve para organizar el codigo
#funciones basicas
#Funciones definidas por el usuario

#simple

def greet():
    print('Hola python')

greet()
# Con retorno
def return_greet():
    return 'Hola pytsshon'

print(return_greet())

#Con argumentos. Es necesario pasarle un argumento para que funcione
def arg_greet(name):
    print( f'Hola {name}')

arg_greet('Ricardo')

def arg_greet_double(greet, name):
    print(f'{greet} {name}')

arg_greet_double('Hallo', 'Ricardo')

#Con argumentos predeterminados, de esta forma al no agregar un valor, se imprime el que le hemos dado por default
def default_arg_greet_double(greet, name='Kakaroto'):
    print(f'{greet} {name}')

default_arg_greet_double('Hallo', 'Ricardo')

#Ahora si queremos darle los valores de forma desordenada, podemos llamarlos por su nombre
default_arg_greet_double(name='Ricardo', greet='Hallo')

#Con argumentos y return (return y print son diferentes, el return es para devolver un valor, el print es para imprimir por pantalla)

def default_arg_greet_double(greet, name='Kakaroto'):
    return(f'{greet} {name}')

print(default_arg_greet_double(name='Angela', greet='Hallo'))

#con retorno de varios valores una tupla
def multiple_return():
    return 'hola', 'ricardo'
#Estamos asignando los valores de la tupla a las variables name y greet 
name, greet = multiple_return()
print(greet)
print(name)
