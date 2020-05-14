import random
from funciones import condicionVictoria, campo, TurnoJugador, TurnoMaquina

moneda=("cara","cruz")
monedaFliped = random.choice(moneda)
campo()
print("Hay que decidir quien empieza, tu o la maquina")
eleccion = input("Elige cara o cruz: ")
if eleccion == monedaFliped:
    print("Has ganado, tu empiezas")
    marca = input("X o O? ")
    if marca == "X":
        marcaMaquina = "O"
    else:
        marcaMaquina = "X"
    count = 0
    while count != 9:
        if condicionVictoria(marca,marcaMaquina) == 1:
            break
        TurnoJugador(marca)
        count = count+1
        TurnoMaquina(marcaMaquina)
        count = count+1
else:
    print("Has perdido, empieza la maquina")
    marca = input("X o O? ")
    if marca == "X":
        marcaMaquina = "O"
    else:
        marcaMaquina = "X"
    count = 0
    while count != 9:
        if condicionVictoria(marca, marcaMaquina) == 1:
            break
        TurnoMaquina(marcaMaquina)
        count = count+1
        TurnoJugador(marca)
        count = count+1




