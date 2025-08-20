import os
os.system("cls")
opcion = int(input("Elige una opcion (1-3):"))

match opcion:
    case 1:
        print("Has elegido la opción 1")
    case 2:
        print("Has elegido la opción 2")
    case 3:
        print("Has elegido la opción 3")
    case _:
        print("opcion no valida")
        