import os
os.system("cls")

frutas=input("Elige una fruta (Manzana, Pera, Mango):").lower()

match frutas:
    case "Manzana":
        print("la manzana cuesta 3000 pesos")
    case "Pera":
        print("La pera cuesta 2500")
    case "Mango":
        print("el mango cuesta 3200")
    case _:
        print("opcion no valida")