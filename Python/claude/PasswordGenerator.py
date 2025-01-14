import random
import string
import re

def generar_contrasena_segura(longitud=12):
    """
    Genera una contraseña segura con los siguientes criterios:
    - Longitud mínima de 12 caracteres
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un número
    - Al menos un carácter especial
    - Evita secuencias y patrones comunes
    """
    if longitud < 12:
        longitud = 12

    # Definir los conjuntos de caracteres
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    numeros = string.digits
    especiales = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Lista de patrones a evitar
    patrones_prohibidos = [
        r'123', r'abc', r'qwerty', r'password', r'admin',
        r'(.)\1\1'  # Tres caracteres repetidos
    ]

    while True:
        # Asegurar al menos un carácter de cada tipo
        contrasena = [
            random.choice(minusculas),
            random.choice(mayusculas),
            random.choice(numeros),
            random.choice(especiales)
        ]
        
        # Completar el resto de la contraseña
        caracteres_restantes = longitud - len(contrasena)
        todos_caracteres = minusculas + mayusculas + numeros + especiales
        
        for _ in range(caracteres_restantes):
            contrasena.append(random.choice(todos_caracteres))
        
        # Mezclar la contraseña
        random.shuffle(contrasena)
        contrasena = ''.join(contrasena)
        
        # Verificar que no contiene patrones prohibidos
        contiene_patron = False
        for patron in patrones_prohibidos:
            if re.search(patron, contrasena.lower()):
                contiene_patron = True
                break
        
        # Verificar todos los requisitos
        if (not contiene_patron and
            any(c in especiales for c in contrasena) and
            any(c in numeros for c in contrasena) and
            any(c in mayusculas for c in contrasena) and
            any(c in minusculas for c in contrasena)):
            return contrasena

def verificar_fortaleza_contrasena(contrasena):
    """
    Verifica la fortaleza de una contraseña y devuelve un diccionario con el análisis
    """
    analisis = {
        'longitud': len(contrasena) >= 12,
        'tiene_mayuscula': any(c.isupper() for c in contrasena),
        'tiene_minuscula': any(c.islower() for c in contrasena),
        'tiene_numero': any(c.isdigit() for c in contrasena),
        'tiene_especial': any(c in string.punctuation for c in contrasena),
        'tiene_secuencias': bool(re.search(r'123|abc|qwerty', contrasena.lower())),
        'tiene_repeticiones': bool(re.search(r'(.)\1\1', contrasena))
    }
    return analisis

# Ejemplo de uso
if __name__ == "__main__":
    contrasena = generar_contrasena_segura(16)
    print(f"Contraseña generada: {contrasena}")
    
    analisis = verificar_fortaleza_contrasena(contrasena)
    print("\nAnálisis de fortaleza:")
    for criterio, cumple in analisis.items():
        print(f"{criterio}: {'✓' if cumple else '✗'}")