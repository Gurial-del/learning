jugador1 = input("Jugador 1: ")
jugador2 = input("Jugador 2: ")
piedra = "piedra"
tijeras = "tijeras"
papel = "papel"
gano = "gano"

if jugador1 == jugador2:
    print("Empate")
elif jugador1 == piedra and jugador2 == tijeras:
    print(jugador1 + " " + gano)
elif jugador1 == tijeras and jugador2 == papel:
    print(jugador1 + " " + gano)
elif jugador1 == papel and jugador2 == piedra:
    print(jugador1 + " " + gano)
else:
    print(jugador2 + " " + gano) 