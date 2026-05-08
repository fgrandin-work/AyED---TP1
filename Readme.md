# Trabajo práctico nro 1 - Algorimos y estructuras de datos

## Testings a realizar:

### Menu principal
- Ingresar caracteres dintitos de A, B, C, D, E, S 
- Ingresar numeros 
- Probar cada opcion, debe ingresar a la sección correpondiente, o cerrar el programa en caso de S

### Juego Mayor - Menor
#### Menu
- Estresar campo "Ingrese nombre" (no permitir string vacia)
- Corroborar menu (que no se puedan introducir caracteres fuera de A, B, C)
- Cada opcion debe hacer lo esperado
- Leer reglas, deben ser claras y correctas 
#### Dentro del juego
- Ingresar string distintos a mayor, menor o salir
- Validar que se sumen los puntos correctamente al ganar, y se reinicien al perder

### Juego Adivinar numero secreto
#### Menu
- Estresar campo "Ingrese nombre" (no permitir string vacia)
- Corroborar menu (que no se puedan introducir caracteres fuera de A, B, C)
- Cada opcion debe hacer lo esperado¨
- Leer reglas, deben ser claras y correctas 
#### Dentro del juego
- Ingresar caracteres no numericos o dar enter sin ingresar nada
- Ingresar numeros fuera del rango 1-100
- Validar que se gane el juego adivinando el numero, en intento 1, 3 y 5, para asegurar que funciona antes del while, durante el while con intentosRestantes=n y durante el while con intentosRestantes=0

### Juego par o impar
#### Menu
- Estresar campo "Ingrese nombre" (no permitir string vacia)
- Corroborar menu (que no se puedan introducir caracteres fuera de A, B, C)
- Cada opcion debe hacer lo esperado¨
- Leer reglas, deben ser claras y correctas 
#### Dentro del juego
- Ingresar string distintos a par, impar o salir
- Validar que se sumen los puntos correctamente al ganar, y se reinicien al perder


## Temas a ver:
-Consultar cuando debe pedir el nombre (por juego o por programa) y como almacenarlo
-Juego mayor menor, generar un nuevo numero cuando perdes
-Reglas numero secreto, el numero deintentos es 5 (en el código la variable es 4 porque se hace un intento antes de entrar al while)
-Revisar todas las validaciones que tengan función int() para evitar que se corte cuando ingresa un string por ejemplo.
-menú principal que admita caracteres en minúsculas?
-Al perder (o ganar?) juego adivinar numero vuelve al menú principal, debería volver al menú de juego?
