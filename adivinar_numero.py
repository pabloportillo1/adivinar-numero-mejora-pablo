import random
from OutOfRangeError import OutOfRangeError

def welcome_rules(number_of_guesses: int, lowerBound: int, upperBound: int):

    print("BIENVENIDO AL JUEGO DE ADIVINAR EL NUMERO")
    print(f"--------------------------------\nTendras {number_of_guesses} intentos para adivinar.\n")
    print(f"El objetivo del juego es adivinar un número entre {lowerBound} y {upperBound}")
    print("Tienes que ingresar tu intento y el programa te dirá si es muy bajo, muy alto o correcto\n")
    print("¡Buena suerte!\n--------------------------------")


def generate_randint(lowerBound : int, upperBound : int) -> int:
    random_number = random.randint(lowerBound, upperBound)
    return random_number


def validate_guess_range(guessed_number : int, lower_bound : int, upper_bound : int):

    if guessed_number < lower_bound or guessed_number > upper_bound:
        raise  OutOfRangeError(f"Entrada no valida. Por favor ingresa un numero entre {lower_bound} y {upper_bound}.")


def guess_input(lowerBound: int, upperBound: int) -> int:

    while True:
        try:
            guessed_number = int(input("Ingresa tu intento: \n"))
            validate_guess_range(guessed_number, lowerBound, upperBound)
            return guessed_number
        except ValueError:
            print("Entrada no valida.Por favor ingresa un numero entero.")
        except OutOfRangeError as e:
            print(e)


def guess_validation(guessed_number : int, random_number : int) -> bool:

    if guessed_number < random_number:
        print("Muy bajo")
        return False
    elif guessed_number > random_number:
        print("Muy alto")
        return False
    else:
        return True

def play_game():

    number_of_guesses = int(input("Ingresa el numero de intentos que deseas tener: \n"))
    lowerBound = int(input("Ingresa el limite inferior del rango: \n"))
    upperBound = int(input("Ingresa el limite superior del rango: \n"))
    random_number = generate_randint(lowerBound, upperBound)

    welcome_rules(number_of_guesses, lowerBound, upperBound)
    available_attempts = number_of_guesses

    while available_attempts > 0:

        guessed_number = guess_input(lowerBound, upperBound)

        if guess_validation(guessed_number, random_number) == 1:
            print(f"Adivinaste, el numero era {random_number}")
            available_attempts -= 1
            break
        else:
            print(f"Tu intento es incorrecto, te quedan {available_attempts} intentos.")
            available_attempts -= 1

    print(f"--------------------------------\nPerdiste, el numero era {random_number}")

def main():
    
    play_game()
        
if __name__ == "__main__":
    main()

