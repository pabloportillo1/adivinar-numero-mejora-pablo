import random

def start_game():
    random_number = random.randint(1, 20)
    guessed_number = 0
    attempts = 0
    print("Adivina el número entre 1 y 20")
    
    while guessed_number != random_number:
        guessed_number = int(input("Ingresa tu intento: "))
        attempts += 1
    if guessed_number < random_number:
        print("Muy bajo")
    elif guessed_number > random_number:
        print("Muy alto")
    elif guessed_number == random_number:
        print("¡Correcto!")
    else:
        print("Error")
        print("Número de intentos:", attempts)
        
start_game()