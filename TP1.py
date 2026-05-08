import random

######################## Variables de Puntajes Globales ########################

nombredeuser = ''

vecesjugadoMyM = 0
puntajeMayorMenor = 0 

vecesjugadoNS = 0
ganadasNumeroSecreto = 0 
perdidasNumeroSecreto = 0 

vecesjugadoPoI = 0
ganadasParOImpar = 0 
perdidasParOImpar = 0 

######################## Menús ########################

def MenuGeneral():
    print("""
    Los juegos de apuesta están prohibidos para los menores de edad y es perjudicial para la salud.
    ####################
    ### ¡Bienvenido! ###
    ####################
    Selecciona el juego colocando su letra correspondiente(Ej: A):
    A - Juego del menor-mayor
    B - Adivinar el número secreto
    C - BlackJack
    D - Par o impar
    E - Reporte
    S - Salir del programa
    """)

def MenuJuegos():
    nombreUser = input("Ingrese su nombre: ").capitalize()
    print(f"""
    BIENVENIDO {nombreUser}!
    A - Iniciar juego
    B - Ver reglas
    C - Volver al menu
    """)
    
######################## Reglas de Juegos ########################

def ReglasMayorMenor():
    print("""
    REGLAS DE MAYOR O MENOR:
    * En todos los juegos se guarda el mejor puntaje obtenido(Apartado: E - Reportes) *
                  
    El sistema genera un número aleatorio inicial entre 1 y 1000.
    El usuario debe escribir si el siguiente número será 'mayor' o 'menor'.
    Si aciertas sumas 1 punto.
    Si te equivocas vuelves a 0 puntos. 
          
    Para volver al menú, escriba 'salir'.
    """)
    input("Presiona Enter para comenzar a jugar. ")

def ReglasNumeroSecreto():
    print("""
    REGLAS DE NÚMERO SECRETO:
    * En todos los juegos se guarda el mejor puntaje obtenido(Apartado: E - Reportes) *
                  
    La computadora piensa un número entre 1 y 100. 
    En cada intento fallido, el sistema debe indicar si el número secreto es mayor o menor al que vos ingresaste.
    Tendrás 4 intentos para adivinarlo.
          
    Pierdes si se te agotan los intentos.
    Si aciertas antes de agotarlos, ¡GANAS!
          
    Para volver al menú, escriba 'salir'.
    """)
    input("Presiona Enter para comenzar a jugar. ")

def ReglasParOImpar():
    print("""
    REGLAS DE PAR O IMPAR:
    * En todos los juegos se guarda el mejor puntaje obtenido(Apartado: E - Reportes) *
          
    El programa tira 2 dados y suma ambos resultados(Dado de 6 caras: 1 al 6).
    Sin ver los resultados de los dados deberás indicar si la suma de los números es par o impar. 
    Si aciertas sumas 1 punto.
    Si pierdes vuelves a 0 puntos.
        
    Para volver al menú, escriba 'salir'.
    """)
    input("Presiona Enter para comenzar a jugar. ")


######################## JUEGOS ########################

######################## A - Mayor a menor ########################

def JuegoMayorMenor():
    global puntajeMayorMenor

    nroAleatorio = random.randint(1,1000)
    nroAleatorioParaaAdivinar = random.randint(1,1000)

    puntaje = 0
    finDeJuego = 1
    
    # Menú del juego y nombre usuario
    MenuJuegos()
    opcionmenujuego = input("Seleccione una opción: ").lower()

    # Opciones del menú del juego
    if (opcionmenujuego == 'a'):
        finDeJuego = 0
    elif(opcionmenujuego == 'b'):
        ReglasMayorMenor()
        finDeJuego = 0
    elif(opcionmenujuego == 'c'):
        print("volver atras reyes 8==D")


    while(finDeJuego == 0):
        if (puntaje == 0):
            print("Comencemos: ")
        print(nroAleatorio)

        eleccion = input("¿Es mayor o menor el siguiente número? ").lower()

        # Verificación para que coloque solo 'mayor' y 'menor'
        while(eleccion != "mayor" and eleccion != "menor" and eleccion != "salir"):
            eleccion = input("Opcion incorrecta, coloque 'mayor' o 'menor'(Para vovler, coloque 'salir'): ").lower()
        
        # Verificación de asertividad en la respuesta del usuario
        if(eleccion == "mayor" and nroAleatorio < nroAleatorioParaaAdivinar):
            puntaje = puntaje + 1
            nroAleatorio = nroAleatorioParaaAdivinar
            nroAleatorioParaaAdivinar = random.randint(1,1000)
            print("¡Bien!")
        elif(eleccion == "menor" and nroAleatorio > nroAleatorioParaaAdivinar):
            puntaje = puntaje + 1
            nroAleatorio = nroAleatorioParaaAdivinar
            nroAleatorioParaaAdivinar = random.randint(1,1000)
            print("¡Bien!")
        elif(eleccion == "salir"):
            finDeJuego = 1
        else:
            print("¡Casi! Intenta nuevamente.")
            print(f"Tu puntaje hasta aquí fué: {puntaje}")
            if(puntajeMayorMenor < puntaje):
                print(f"Superaste tu marca personal anterior, se ha actualizado tu puntaje máximo.")
                puntajeMayorMenor = puntaje
            puntaje = 0

        # Evitar igualdad en la aleatoriedad del número nuevo y el anterior
        while(nroAleatorioParaaAdivinar == nroAleatorio):
            nroAleatorioParaaAdivinar = random.randint(1,1000)

        # Testing
        #print(nroAleatorio)
        #print(nroAleatorioParaaAdivinar)

######################## B - Número secreto ########################

def ValidacionNumeroSecreto(nroIngresado):
    while(nroIngresado < 1 or nroIngresado > 100):
        print("El número ingresado debe estar entre 1 y 100.")
        print("Ingrese otro número:")
        nroIngresado = int(input())
    
def JuegoNumeroSecreto():
    global puntajeNumeroSecreto
    IntentosRestantes = 4
    nroAleatorio = random.randint(1,100)
    finDeJuego= 1
    
    # Menú del juego y nombre usuario
    MenuJuegos()
    opcionmenujuego = input("Seleccione una opción: ").lower()

    # Opciones del menú del juego
    if (opcionmenujuego == 'a'):
        finDeJuego= 0
    elif(opcionmenujuego == 'b'):
        ReglasNumeroSecreto()
    elif(opcionmenujuego == 'c'):
        print("voilver atras reyes 8==D")   

    nroIngresado = int(input("Ingrese un numero: "))

    # Validación
    ValidacionNumeroSecreto(nroIngresado)
        
    while(nroIngresado != nroAleatorio and IntentosRestantes > 0):

        if(nroIngresado > nroAleatorio):
            print("El número secreto es menor al ingresado.")
            print("Ingrese otro número:")
            nroIngresado = int(input())

            # Validación
            ValidacionNumeroSecreto(nroIngresado)

        else:
            print("El número secreto es mayor al ingresado.")
            print("Ingrese otro número:")
            nroIngresado = int(input())

            # Validación
            ValidacionNumeroSecreto(nroIngresado)

        IntentosRestantes = IntentosRestantes-1

    # Fín del juego
    if(nroIngresado == nroAleatorio):
        print("¡Ganaste! El número secreto era:", nroAleatorio)
        puntajeNumeroSecreto += 1
    else:
        print("¡Perdiste! El número secreto era:", nroAleatorio)

######################## C - BLACK JACK ########################

def EnConstruccion():
    print("""
    Estamos construyendo el juego, pronto estará publicado.
    ¡Gracias por tu paciencia!
    """)
    input("Presiona Enter para volver al menú principal.")
    
def JuegoBlackJack():
    return EnConstruccion()

######################## D - Par o impar ########################

def JuegoParOImpar():
    global puntajeParOImpar
    puntaje = 0
    finDeJuego = 1

    # Menú del juego y nombre usuario
    MenuJuegos()
    opcionmenujuego = input("Seleccione una opción: ").lower()

    # Opciones del menú del juego
    if (opcionmenujuego == 'a'):
        finDeJuego = 0
    elif(opcionmenujuego == 'b'):
        ReglasParOImpar()
        finDeJuego = 0
    elif(opcionmenujuego == 'c'):
        print("voilver atras reyes 8==D")
    
    while (finDeJuego == 0):
        dadoA = random.randint(1, 6)
        dadoB = random.randint(1, 6)
        suma = dadoA + dadoB

        # Input
        print("""
        Los dados se hán tirado.
        Crees que la suma será par o impar?
        """)
        respuesta = input("Respuesta: ").lower()

        # Verificación de respuesta (par, impar o salir)
        while (respuesta != 'par' and respuesta != 'impar' and respuesta != 'salir'):
            print("""
            Respuesta incorrecta. Intente nuevamente.
            * Recuerda que solo se permite introducir 'par' o 'impar'(Para salir coloque 'salir').
            """)
            respuesta = input("Respuesta: ").lower()
    
        # Comparación de respuesta del usuario y los dados
        if (suma % 2 == 0 and respuesta == 'par' or suma % 2 != 0 and respuesta == 'impar'):
            puntaje += 1
            print(f"Acertaste! Los números fueron {dadoA} y {dadoB}, y suman {suma}.")
        elif (respuesta == 'salir'):
            finDeJuego = 1
        else:
            print(f"Te equivocaste! Los números fueron {dadoA} y {dadoB}, y suman {suma}.")
            print(f"Tu puntaje alcanzado fue: {puntaje}")
            puntaje = 0

######################## REPORTES ########################

def Reportes():
    global puntajeMayorMenor
    global puntajeNumeroSecreto
    global puntajeParOImpar

    print("""

    """)

######################## Testing de partes individualmente ########################

# MenuGeneral()
# MenuJuegos()

# JuegoMayorMenor()
# JuegoNumeroSecreto()
# JuegoBlackJack()
# JuegoParOImpar()

######################## FUNCIÓN MAIN ########################

opc = "" # así lo obligo a entrar al mientras y lo convierto en un Repetir

while (opc!="S"):

    MenuGeneral()
    opc = str(input("Ingrese su opcion: "))

    # Validación de opción de usuario
    while (opc<"A" or opc>"E" and opc!= "S"):
        opc = str(input("Ingreso Invalido - reintente "))
        match opc:
            case "A": JuegoMayorMenor()
            case "B": JuegoNumeroSecreto()
            case "C": JuegoBlackJack()#blackjack
            case "D": JuegoParOImpar()
            case "E": cartel()#reporte
            case "S": print('\n\n GRACIAS POR USAR NUESTRO SISTEMA!!!!')

