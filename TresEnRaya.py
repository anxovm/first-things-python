import random
from funciones import condicionVictoria, campo, TurnoJugador, TurnoMaquina


campo()
count = 0
while count != 9:
    if condicionVictoria() == 1:
        break
    TurnoJugador()
    count = count+1
    TurnoMaquina()
    count = count+1




