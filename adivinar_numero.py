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


def bounds_input(lowerOrUpper: str) -> int:

    while True:
        try: 
            bound = int(input(f"Ingresa el limite {lowerOrUpper} del rango: \n"))
            return bound
        except ValueError:
            print("Entrada incorrecta, el valor debe de ser un entero.")

def attempts_input() -> int:
    
    while True:
        try:
            number_of_guesses = int(input("Ingresa el numero de intentos que deseas tener: \n"))
            if number_of_guesses <= 0:
                print("El numero de intentos debe ser un entero positivo. Por favor ingresa el numero de intentos nuevamente.")
                continue
            return number_of_guesses
        except ValueError:
            print("Entrada no valida.Por favor ingresa un numero entero positivo.")


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


    number_of_guesses = attempts_input()
    lowerBound = bounds_input("inferior")
    upperBound = bounds_input("superior")
    random_number = generate_randint(lowerBound, upperBound)


    welcome_rules(number_of_guesses, lowerBound, upperBound)
    available_attempts = number_of_guesses

    while available_attempts > 0:

        guessed_number = guess_input(lowerBound, upperBound)

        if guess_validation(guessed_number, random_number) == 1:
            print(f"Adivinaste, el numero era {random_number}")
            available_attempts -= 1
            break
        elif available_attempts == 0:
            print(f"Te has quedado sin intentos, el numero era {random_number}")
            break
        else:
            available_attempts -= 1
            print(f"Tu intento es incorrecto, te quedan {available_attempts} intentos.")
