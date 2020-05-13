import random
tablero = [["1", " | ", "2", " | ", "3"],
           ["-", "-", "-", "-", "-", "-", "-"],
           ["4", " | ", "5", " | ", "6"],
           ["-", "-", "-", "-", "-","-", "-"],
           ["7", " | ", "8", " | ", "9"]]

def campo():
    for x in range(len(tablero)):
        for y in range(len(tablero[x])):
            print(tablero[x][y], end=" ")
        print()


def TurnoJugador():
    primer_mov = input("Introduce una posicion: ")
    if primer_mov == "1" and tablero[0][0] != "X" and tablero[0][0] != "O":
        tablero[0][0] = "X" 
    elif primer_mov == "2" and tablero[0][2] != "X" and tablero[0][2] != "O":
        tablero[0][2] = "X"
    elif primer_mov == "3" and tablero[0][4] != "X" and tablero[0][4] != "O":
        tablero[0][4] = "X"
    elif primer_mov == "4" and tablero[2][0] != "X" and tablero[2][0] != "O":
        tablero[2][0] = "X"
    elif primer_mov == "5" and tablero[2][2] != "X" and tablero[2][2] != "O":
        tablero[2][2] = "X"
    elif primer_mov == "6" and tablero[2][4] != "X" and tablero[2][4] != "O":
        tablero[2][4] = "X"
    elif primer_mov == "7" and tablero[4][0] != "X" and tablero[4][0] != "O":
        tablero[4][0] = "X"
    elif primer_mov == "8" and tablero[4][2] != "X" and tablero[4][2] != "O":
        tablero[4][2] = "X"
    elif primer_mov == "9" and tablero[4][4] != "X" and tablero[4][4] != "O":
        tablero[4][4] = "X"
    campo()

def TurnoMaquina():
    print("Turno de la maquina: ")
    num_aleatorio = ("1","2","3","5","6","7","8","9")
    segundo_mov = random.choice(num_aleatorio)
    while True:
        if segundo_mov == "1" and tablero[0][0] != "X" and tablero[0][0] != "O":
            tablero[0][0] = "O"
            break
        elif segundo_mov == "2" and tablero[0][2] != "X" and tablero[0][2] != "O":
            tablero[0][2] = "O"
            break
        elif segundo_mov == "3" and tablero[0][4] != "X" and tablero[0][4] != "O":
            tablero[0][4] = "O"
            break
        elif segundo_mov == "4" and tablero[2][0] != "O" and tablero[2][0] != "O":
            tablero[2][0] = "X"
            break
        elif segundo_mov == "5" and tablero[2][2] != "X" and tablero[2][2] != "O":
            tablero[2][2] = "O"
            break
        elif segundo_mov == "6" and tablero[2][4] != "X" and tablero[2][4] != "O":
            tablero[2][4] = "O"
            break
        elif segundo_mov == "7" and tablero[4][0] != "X" and tablero[4][0] != "O":
            tablero[4][0] = "O"
            break
        elif segundo_mov == "8" and tablero[4][2] != "X" and tablero[4][2] != "O":
            tablero[4][2] = "O"
            break
        elif segundo_mov == "9" and tablero[4][4] != "X" and tablero[4][4] != "O":
            tablero[4][4] = "O"
            break
        else:
            segundo_mov = random.choice(num_aleatorio)
    campo()


def condicionVictoria():
        if ((tablero[0][0] == "X" and 
        tablero[0][2] == "X" and 
        tablero[0][4] == "X") 
        or (tablero[2][0] == "X" and 
            tablero[2][2] == "X" and 
            tablero[2][4] == "X") 
            or (tablero[4][0] == "X" and 
                tablero[4][2] == "X" and 
                tablero[4][4] == "X") 
                or (tablero[0][0] == "X" and 
                    tablero[2][0] == "X" and 
                    tablero[4][0] == "X")
                    or (tablero[0][2] == "X" and
                        tablero[2][2] == "X" and
                        tablero[4][2] == "X")
                        or (tablero[0][4] == "X" and
                            tablero[2][4] == "X" and
                            tablero[4][4] == "X")
                            or (tablero[0][0] == "X" and 
                                tablero[2][2] == "X" and
                                tablero[4][4] == "X")
                                or (tablero[0][4] == "X" and
                                    tablero[2][2] == "X" and
                                    tablero[4][0] == "X")):
            print("Enhorabuena, has ganado")
            return 1