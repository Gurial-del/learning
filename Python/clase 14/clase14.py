numbers = {1:'uno', 2:'dos', 3:'tres'}
print([2])
informacion = {'nombre': 'carla', 'apellido': 'gutierrez', 'altura': 1.71, 'edad': 27}
print(informacion)
print(informacion['nombre'])
claves = informacion.keys()
print(claves)
print(type(claves))
values = informacion.values()
print(values)
pares = informacion.items()
print(pares)

informacion = {'Ricardo':{'apellido': 'gutierrez', 'altura': 1.71, 'edad': 27},
               'Angela':{'apellido': 'Angulo', 'altura': 1.63, 'edad': 23}
                  }
print(informacion['Angela'])
