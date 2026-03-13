# Pull Request and Code Review

## Cambios aplicados

### Separación de responsabilidades en funciones

El código está dividido en muchas funciones con un solo propósito, tales como:

guess_input(...) → valida que el número esté dentro de rango.

validate_guess_range(...) → lanza excepción si el número está fuera del rango.

attempts_input() → valida la entrada de intentos.

bounds_input(...) → obtiene límites de rango del usuario.

guess_validation(...) → compara el número adivinado con el número aleatorio.

### Manejo de errores con excepciones personalizado
Se define una clase OutOfRangeError para manejar el caso en que el usuario introduzca un número fuera del rango permitido, lo cual proporciona un feedback más claro y controlado.

### Validaciones de entrada mucho más robustas
En lugar de permitir que la entrada rompa el juego con un error (ValueError), se captura el error y se vuelve a solicitar la entrada.

### Rango dinámico de juego
El usuario ahora puede ingresar el límite inferior y superior del rango en el que se genera el número a adivinar, lo cual hace el juego más flexible.

### Control de intentos configurable
El usuario puede elegir cuántos intentos quiere tener para adivinar, en lugar de que sea infinito o fijo.

### Mensajes al usuario más completos e instructivos
Mensajes de bienvenida, reglas claras y conteo de intentos faltantes se muestran durante el juego.

## Principios de Clean Code:

### Funciones de una sola responsabilidad

Cada función hace solo una cosa y lo hace bien:

  Una función solo lee el número con validación.

  Otra genera el número aleatorio.

  Otra compara el intento con el número secreto.

Esto mejora la legibilidad y testabilidad.

### Evitar duplicación y evitar código espagueti

En la versión original todo estaba dentro de un bucle while en una sola función.
La versión mejorada divide en funciones reutilizables, lo que hace mucho más fácil entender y mantener el programa.

### Manejo explícito de excepciones

Usar una clase de excepción personalizada (OutOfRangeError) permite separar claramente casos de error y lógica de juego.

### Mensajes al usuario consistentes

El código mejorado entrega mensajes útiles y consistentes (qué esperar, qué hacer y cómo corregir errores).

## Decisiones importantes tomadas y por qué

Comenze por decidir dejar al usuario establecer el rango de numeros dentro del cual se generaria el numero del juego. Esto hace el juego más configurable y reutilizable para distintos niveles de dificultad.
Enseguida, valide que los límites del rango tengan sentido evitando que el juego pueda generar un número imposible de adivinar.
Finalmente, decidi manejar las entradas incorrectas con el uso de excepciones como ValueError y una extra disenada por mi, con el proposito de validar que el input ddel ususario se encuentre dentro del rango establecido por el mismo. Esto garantiza una mejor experiencia de usuario y mitiga posibles errores obligandolo a mantenerse dentro de cierrtas reglas del juego.
