# input

import random

def adivina_el_numero():
    numerosecreto = random.randint(1, 100)
    intentos = 0
    print("He elegido un número entre 1 y 100. ¡Intenta adivinarlo!")


    while True:

        
        usu = int(input("Ingresa tu adivinanza: "))

        
        if usu < numerosecreto :
            print("el numero es mas alto ¡Inténtalo de nuevo!")
        elif usu > numerosecreto:
            print("el numero es mas bajo ¡Inténtalo de nuevo!")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        intentos=0+1

adivina_el_numero()


