class OutOfRangeError(Exception):

    def __init__(self, message="El numero ingresado esta fuera del rango permitido."):
        self.message = message
        super().__init__(self.message)

    