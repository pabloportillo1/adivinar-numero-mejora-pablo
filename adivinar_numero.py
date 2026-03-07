import random

def welcome_rules(number_of_guesses: int, lowerBound: int, upperBound: int):

    print("BIENVENIDO AL JUEGO DE ADIVINAR EL NUMERO")
    print(f"--------------------------------\nTendras {number_of_guesses} intentos para adivinar.\n")
    print(f"El objetivo del juego es adivinar un número entre {lowerBound} y {upperBound}")
    print("Tienes que ingresar tu intento y el programa te dirá si es muy bajo, muy alto o correcto\n")
    print("¡Buena suerte!\n--------------------------------")

def generate_randint(lowerBound : int, upperBound : int) -> int:
    random_number = random.randint(lowerBound, upperBound)
    return random_number

def guess_input() -> int:

    while True:
        try:
            guessed_number = int(input("Ingresa tu intento: \n"))
            return guessed_number
        except ValueError:
            print("Entrada no valida.Por favor ingresa un numero entero.")
            return guess_input()

def guess_validation(guessed_number : int, random_number : int) -> bool:
    if guessed_number < random_number:
        return 0
    elif guessed_number > random_number:
        return 0
    else:
        return 1
    
def attempt_counter( guess_validation : bool, number_of_guesses : int ) -> int:
    attempts = 0
    if guess_validation == 0:
        attempts += 1
        number_of_guesses -= 1
    return attempts, number_of_guesses

def play_game():

    number_of_guesses = int(input("Ingresa el numero de intentos que deseas tener: \n"))
    lowerBound = int(input("Ingresa el limite inferior del rango: \n"))
    upperBound = int(input("Ingresa el limite superior del rango: \n"))
    random_number = generate_randint(lowerBound, upperBound)

    welcome_rules(number_of_guesses, lowerBound, upperBound)
    while number_of_guesses > 0:
        guessed_number = guess_input()

        if guess_validation(guessed_number, random_number) == 1:
            print(f"Adivinaste, el numero era {random_number}")
            break
        else:
            print(f"Tu intento es incorrecto, te quedan {number_of_guesses} intentos.")
            number_of_guesses -= 1
            if number_of_guesses == 0:
                print(f"--------------------------------\nPerdiste, el numero era {random_number}")

def main():
    
    play_game()
        
if __name__ == "__main__":
    main()

