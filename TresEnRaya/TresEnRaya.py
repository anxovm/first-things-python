import random
from funciones import condicionVictoria, campo, TurnoJugador, TurnoMaquina
#Todas las funciones estan explicadas en el fichero de funciones

#Primero se comprueba quien empieza primero con cara o cruz
#En el caso de que se gana en cara o cruz, el jugador empieza
#sino empieza la maquina
moneda=("cara","cruz")
monedaFliped = random.choice(moneda)

#1
campo()

print("Hay que decidir quien empieza, tu o la maquina")
eleccion = input("Elige cara o cruz: ")
if eleccion == monedaFliped:
    print("Has ganado, tu empiezas")

#Ahora se eligue que tipo de marca usar

    marca = input("X o O? ")
    if marca == "X":
        marcaMaquina = "O"
    else:
        marcaMaquina = "X"

#El contador count se usar para contar todos los movimientos
#tanto del jugador como de la maquina
    
    count = 0

#Creo un bucle que se repitira hasta que se llene el tablero, en caso de
#que se llene y nadie ganase, seria un empate

    while count != 9:
        #4
        if condicionVictoria(marca,marcaMaquina) == 1:
            break
        #2
        TurnoJugador(marca)
        count = count+1
        #3
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
        #4
        if condicionVictoria(marca, marcaMaquina) == 1:
            break
        #3
        TurnoMaquina(marcaMaquina)
        count = count+1
        #2
        TurnoJugador(marca)
        count = count+1




