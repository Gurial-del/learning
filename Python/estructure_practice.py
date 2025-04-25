'''
EJERCICIO:
* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
* - Utiliza operaciones de inserción, borrado, actualización y ordenación.
*
* DIFICULTAD EXTRA (opcional):
* - Crea una agenda de contactos por terminal.
* - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
* - Cada contacto debe tener un nombre y un número de teléfono.
* - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
* los datos necesarios para llevarla a cabo.
* - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
*   (o el número de dígitos que quieras)
* - También se debe proponer una operación de finalización del programa.
'''



def create_contact(name = 'sinnombre', phone = 'sinnumero'):
    name = str(input('What is the name of the contact?'))
    phone = int(input('What is the phone number of the contact?'))
    return name, phone

contacto = {}
another_contact = 'yes'    
while another_contact.lower() == 'yes':
    name, phone = create_contact()
    contacto[name] = phone
    another_contact = input('Do you want to create another contact? (yes/no)')

print(contacto.items())