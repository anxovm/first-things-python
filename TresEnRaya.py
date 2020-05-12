import random
tablero = [["1", " | ", "2", " | ", "3"],
           ["-", "-", "-", "-", "-", "-", "-"],
           ["4", " | ", "5", " | ", "6"],
           ["-", "-", "-", "-", "-","-", "-"],
           ["7", " | ", "8", " | ", "9"]]

for x in range(len(tablero)):
        for y in range(len(tablero[x])):
            print(tablero[x][y], end=" ")
        print()

def campo():
    global tablero
    for x in range(len(tablero)):
        for y in range(len(tablero[x])):
            print(tablero[x][y], end=" ")
        print()

primer_mov = input("Introduce una posicion: ")

if primer_mov == "1":
    tablero[0][0] = "X"
    campo()
elif primer_mov == "2":
    tablero[0][2] = "X"
    campo()
elif primer_mov == "3":
    tablero[0][4] = "X"
    campo()
elif primer_mov == "4":
    tablero[2][0] = "X"
    campo()
elif primer_mov == "5":
    tablero[2][2] = "X"
    campo()
elif primer_mov == "6":
    tablero[2][4] = "X"
    campo()
elif primer_mov == "7":
    tablero[4][0] = "X"
    campo()
elif primer_mov == "8":
    tablero[4][2] = "X"
    campo()
elif primer_mov == "9":
    tablero[4][4] = "X"
    campo()
input(" ")
print("Turno de la maquina: ")
num_aleatorio = ("1","2","3","5","6","7","8","9")
segundo_mov = random.choice(num_aleatorio)
if segundo_mov == "1" and tablero[0][0] != "X":
    tablero[0][0] = "O"
    campo()
elif segundo_mov == "2" and tablero[0][2] != "X":
    tablero[0][2] = "O"
    campo()
elif segundo_mov == "3" and tablero[0][4] != "X":
    tablero[0][4] = "O"
    campo()
elif segundo_mov == "4" and tablero[2][0] != "O":
    tablero[2][0] = "X"
    campo()
elif segundo_mov == "5" and tablero[2][2] != "X":
    tablero[2][2] = "O"
    campo()
elif segundo_mov == "6" and tablero[2][4] != "X":
    tablero[2][4] = "O"
    campo()
elif segundo_mov == "7" and tablero[4][0] != "X":
    tablero[4][0] = "O"
    campo()
elif segundo_mov == "8" and tablero[4][2] != "X":
    tablero[4][2] = "O"
    campo()
elif segundo_mov == "9" and tablero[4][4] != "X":
    tablero[4][4] = "O"
    campo()