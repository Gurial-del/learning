to_do = ['Dirigirnos al hotel', 'ir a almorzar', 'visitar el museo',
         'volver al hotel']
print(to_do)
numbers = [1,2,3,4, 499, 109, 49,234,235565,1235]

print(numbers)
print(type(numbers))
mix = ['hola',1,2,3,4, ['uno1', 2 ,3]]
print(mix)
print(len(mix))
print('primer elemento', mix[0])
print(mix[0:3])
mix.append(False)#append agrega a la lista
print(mix)
mix.insert(1,['ss', '55'])
print(mix)
print('mayor', max(numbers)) #max me da el numero mayor de la lista
print('menor', min(numbers)) #min me da el numero menor de la lista
del numbers[-1] #elimina segun la posicion 
print(numbers)

a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[2]
print(a)
print(b)
print(id(a))
print(id(b))
c = a[:]
del a[1]
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))