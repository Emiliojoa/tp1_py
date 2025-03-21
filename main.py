import random

def ram_num():
    numero_loco = random.randint(1, 100)
    intentos = 0
    adivinado = False  # variable que nos ayudara a saber si el numero fue adivinado

    print("Hola, soy un numero loco, adivina cual es el numero que estoy pensando")

    while not adivinado:
        try:
            intento = int(input("Ingresa un numero: "))
            intentos += 1
            if intento == numero_loco:
                adivinado = True
                print("Felicidades, adivinaste el numero en {} intentos".format(intentos))
            elif intento < numero_loco:
                print("El numero es mayor")
            else:
                print("El numero es menor") ## a partir de aca use chat porque me tiraba error y no enetendia el porque
        except ValueError:
            print("Ingresa un numero valido")
                
if __name__ == "__main__":
    ram_num()