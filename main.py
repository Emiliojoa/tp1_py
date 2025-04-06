import random

def ram_num():
    numero_loco = random.randint(1, 100)
    intentos = 0
    adivinado = False  # variable que nos ayudara a saber si el numero fue adivinado

    print("Hola, soy un numero loco, adivina cual es el numero que estoy pensando")

    while not adivinado:
            intento = int(input("Ingresa un numero: "))
            intentos += 1
            if intento == numero_loco:
                adivinado = True
                print(f"Felicidades, adivinaste el numero en {intentos} intentos")
            elif intento < numero_loco:
                print("El numero es mayor")
            else:
                print("El numero es menor") ## a partir de aca use chat porque me tiraba error y no enetendia el porque

print(ram_num())##gracias

