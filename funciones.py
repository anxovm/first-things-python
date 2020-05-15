import random

#se crea una matriz que contendra el tablero de juego

tablero = [["1", " | ", "2", " | ", "3"],
           ["-", "-", "-", "-", "-", "-", "-"],
           ["4", " | ", "5", " | ", "6"],
           ["-", "-", "-", "-", "-","-", "-"],
           ["7", " | ", "8", " | ", "9"]]

#La funcion campo se utiliza para mostrar el tablero

def campo():
    for x in range(len(tablero)):
        for y in range(len(tablero[x])):
            print(tablero[x][y], end=" ")
        print()

#La funcion TurnoJugador recibe la marca elegida por el jugador (X o O)
#el funcionamiento de esta es mirar que en el lugar que se quiere colocar la marca
#no hay otra ya puesta
def TurnoJugador(marca):
    primer_mov = input("Introduce una posicion: ")
    if primer_mov == "1" and tablero[0][0] != "X" and tablero[0][0] != "O":
        tablero[0][0] = marca 
    elif primer_mov == "2" and tablero[0][2] != "X" and tablero[0][2] != "O":
        tablero[0][2] = marca
    elif primer_mov == "3" and tablero[0][4] != "X" and tablero[0][4] != "O":
        tablero[0][4] = marca
    elif primer_mov == "4" and tablero[2][0] != "X" and tablero[2][0] != "O":
        tablero[2][0] = marca
    elif primer_mov == "5" and tablero[2][2] != "X" and tablero[2][2] != "O":
        tablero[2][2] = marca
    elif primer_mov == "6" and tablero[2][4] != "X" and tablero[2][4] != "O":
        tablero[2][4] = marca
    elif primer_mov == "7" and tablero[4][0] != "X" and tablero[4][0] != "O":
        tablero[4][0] = marca
    elif primer_mov == "8" and tablero[4][2] != "X" and tablero[4][2] != "O":
        tablero[4][2] = marca
    elif primer_mov == "9" and tablero[4][4] != "X" and tablero[4][4] != "O":
        tablero[4][4] = marca
    campo()

#Para el turno de la maquina se usa una tupla que contiene los numeros de 1 al 9
#con random.choice eligue un numero aleatoria y mira si puede colocar la marca en ese numero
#en el caso de que no pueda se rompe el bucle y se eligue otro numero aleatorio

def TurnoMaquina(marcaMaquina):
    print("Turno de la maquina: ")
    num_aleatorio = ("1","2","3","5","6","7","8","9")
    segundo_mov = random.choice(num_aleatorio)
    while True:
        if segundo_mov == "1" and tablero[0][0] != "X" and tablero[0][0] != "O":
            tablero[0][0] = marcaMaquina
            break
        elif segundo_mov == "2" and tablero[0][2] != "X" and tablero[0][2] != "O":
            tablero[0][2] = marcaMaquina
            break
        elif segundo_mov == "3" and tablero[0][4] != "X" and tablero[0][4] != "O":
            tablero[0][4] = marcaMaquina
            break
        elif segundo_mov == "4" and tablero[2][0] != "O" and tablero[2][0] != "O":
            tablero[2][0] = marcaMaquina
            break
        elif segundo_mov == "5" and tablero[2][2] != "X" and tablero[2][2] != "O":
            tablero[2][2] = marcaMaquina
            break
        elif segundo_mov == "6" and tablero[2][4] != "X" and tablero[2][4] != "O":
            tablero[2][4] = marcaMaquina
            break
        elif segundo_mov == "7" and tablero[4][0] != "X" and tablero[4][0] != "O":
            tablero[4][0] = marcaMaquina
            break
        elif segundo_mov == "8" and tablero[4][2] != "X" and tablero[4][2] != "O":
            tablero[4][2] = marcaMaquina
            break
        elif segundo_mov == "9" and tablero[4][4] != "X" and tablero[4][4] != "O":
            tablero[4][4] = marcaMaquina
            break
        else:
            segundo_mov = random.choice(num_aleatorio)
    campo()

#La funcion condicionVicoria comprueba si alguna de las dos marcas
#cumple con los requisitos de ganar en el tres en raya
#comprobando todos los tres en raya posibles

def condicionVictoria(marca, marcaMaquina):
        if ((tablero[0][0] == marca and 
        tablero[0][2] == marca and 
        tablero[0][4] == marca) 
        or (tablero[2][0] == marca and 
            tablero[2][2] == marca and 
            tablero[2][4] == marca) 
            or (tablero[4][0] == marca and 
                tablero[4][2] == marca and 
                tablero[4][4] == marca) 
                or (tablero[0][0] == marca and 
                    tablero[2][0] == marca and 
                    tablero[4][0] == marca)
                    or (tablero[0][2] == marca and
                        tablero[2][2] == marca and
                        tablero[4][2] == marca)
                        or (tablero[0][4] == marca and
                            tablero[2][4] == marca and
                            tablero[4][4] == marca)
                            or (tablero[0][0] == marca and 
                                tablero[2][2] == marca and
                                tablero[4][4] == marca)
                                or (tablero[0][4] == marca and
                                    tablero[2][2] == marca and
                                    tablero[4][0] == marca)):
            print("Enhorabuena, has ganado")
            return 1
        if ((tablero[0][0] == marcaMaquina and 
        tablero[0][2] == marcaMaquina and 
        tablero[0][4] == marcaMaquina) 
        or (tablero[2][0] == marcaMaquina and 
            tablero[2][2] == marcaMaquina and 
            tablero[2][4] == marcaMaquina) 
            or (tablero[4][0] == marcaMaquina and 
                tablero[4][2] == marcaMaquina and 
                tablero[4][4] == marcaMaquina) 
                or (tablero[0][0] == marcaMaquina and 
                    tablero[2][0] == marcaMaquina and 
                    tablero[4][0] == marcaMaquina)
                    or (tablero[0][2] == marcaMaquina and
                        tablero[2][2] == marcaMaquina and
                        tablero[4][2] == marcaMaquina)
                        or (tablero[0][4] == marcaMaquina and
                            tablero[2][4] == marcaMaquina and
                            tablero[4][4] == marcaMaquina)
                            or (tablero[0][0] == marcaMaquina and 
                                tablero[2][2] == marcaMaquina and
                                tablero[4][4] == marcaMaquina)
                                or (tablero[0][4] == marcaMaquina and
                                    tablero[2][2] == marcaMaquina and
                                    tablero[4][0] == marcaMaquina)):
            print("Vaya, has perdido...")
            return 1