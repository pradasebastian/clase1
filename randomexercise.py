import os
import random

x = random.randint(1, 10)
print(x)

isActive=True
while isActive:
  os.system("clear")
  print("Bienvenidos al minijuegos de adivinar un número entre 1 y 10")

  numero= int(input("Ingrese el numero que cree que es el numero aleatorio: "))

  if numero == x:
    print("\nFelicidades, adivinaste el numero")
    isActive=False
    input()
  else:
    print(f"\nlo siento, intenta de nuevo")
    input()