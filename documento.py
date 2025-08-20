import os
os.system("cls")

peso=float(input("Ingrese su peso: "))
altura=float(input("Ingrese su altura: "))
imc=peso/(altura**2) #imc es el indice de masa corporal

if imc < 18.5:
    print(f"Usted tiene bajo peso y su imc es: {imc:.2f}")
elif imc >= 18.5 and imc < 24.9:
    print(f"Usted tiene un peso normal y su imc es: {imc:.2f}")
elif imc >= 24.9 and imc < 29.9:
    print(f"Usted tiene sobrepeso y su imc es: {imc:.2f}")
else:
    print(f"Usted tiene obesidad y su imc es: {imc:.2f}")