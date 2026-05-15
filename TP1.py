import random
import os

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

######################## Menús #####################################

def MenuGeneral():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("""
\033[32m 
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
|#|#                                                                                 #|#|
|#|#\033[37m        __                 __          /\     ___                 __           \033[32m  #|#|
|#|#\033[37m      #|  |  __ __   ____ |  | __   #_(__)/ #|   |   ____   ____ |__| ____     \033[32m  #|#|
|#|#\033[37m      #|  | |  |  \_/ ___\|  |/ /  #/    \  #|   |  /  _ \ / ___\|  |/ ___\    \033[32m  #|#|
|#|#\033[37m      #|  |_|  |  /\  \___|    <  #|   |  \ #|   |_(  <_> ) /_/  >  \  \___    \033[32m  #|#|
|#|#\033[37m      #|____/____/  \___  >__|_ \ #|___|  / #|____/\____/\___  / |__|\___  >   \033[32m  #|#|
|#|#\033[37m                        \/     \/       \/              /_____/          \/    \033[32m  #|#|
|#|#                                                                                 #|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
|#|#|                                                                               |#|#|
|#|#|                              ¡Bienvenido!                                     |#|#|
|#|#|                               ¯¯¯¯¯¯¯¯¯¯                                      |#|#|
|#|#|    \033[37m Selecciona el juego colocando su letra correspondiente(Ej: A):\033[32m            |#|#|
|#|#|    \033[37m A - Juego del menor-mayor                                     \033[32m            |#|#|
|#|#|    \033[37m B - Adivinar el número secreto                                \033[32m            |#|#|
|#|#|    \033[37m C - BlackJack                                                 \033[32m            |#|#|
|#|#|    \033[37m D - Par o impar                                               \033[32m            |#|#|
|#|#|    \033[37m E - Reporte                                                   \033[32m            |#|#|
|#|#|    \033[37m S - Salir del programa                                        \033[32m            |#|#|
|#|#|                                                                               |#|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
    """)

def MenuJuegos():
    nombreUser = input("\033[33m    Ingrese su nombre: \033[0m").capitalize()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""          
           \033[32m¡BIENVENIDO {nombreUser}!\033[0m         

\033[32m 
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
|#|#                                     #|#|
|#|#\033[37m         A - Iniciar juego           \033[32m#|#|
|#|#\033[37m         B - Ver reglas              \033[32m#|#|
|#|#\033[37m         C - Volver al menu          \033[32m#|#|
|#|#                                     #|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|\033[0m 
    """)
    

def InicioMayorMenor():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
\033[32m          
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#||#|#||#|#||#|#||#|#|#|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#||#|#||#|#||#|#||#|#|#|#| 
|#|#                                                                                                         #|#|
|#|#\033[37m       _    _                                                                            _________      \033[32m #|#|
|#|#\033[37m     #| \  / \  _____  ___.__. ___________     ____      _____   ____   ____   __________\_____   \     \033[32m #|#|
|#|#\033[37m     #|  \/   \ \__ \ <   |  |/  _ \_  __ \  #/  _ \   #/     \_/ __ \ /    \ /  _ \_  __ \ /   __/      \033[32m#|#| 
|#|#\033[37m     #|  /\    \ / __\.\___  (  <_> )  | \/  (  <_> ) #|  Y Y  \  ___/|   |  (  <_> )  | \/|   |         \033[32m#|#| 
|#|#\033[37m     #|_|  |_   (____  / ____|\____/|__|     #\____/  #|__|_|  /\___  >___|  /\____/|__|   |___|         \033[32m#|#| 
|#|#\033[37m             \/      \/\/                                    \/     \/     \/              <___>         \033[32m#|#| 
|#|#                                                                                                         #|#| 
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#||#|#||#|#||#|#||#|#|#|#| 
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#||#|#||#|#||#|#||#|#|#|#| 
    """)

def InicioNumeroSecreto():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    \033[32m
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
|#|#                                                                                           #|#|
|#|#\033[37m       ____   __                     _________                            __               \033[32m#|#|
|#|#\033[37m      #\   \ \  | _____  ____      #/   _____/ ____   ___________   _____/  |_  ____       \033[32m#|#|
|#|#\033[37m      #/ |\ \ | ||  __ \/  _ \     #\_____  \_/ __ \_/ ___\_  __ \_/ __ \   __\/  _ \      \033[32m#|#|
|#|#\033[37m     #/  | \ \| ||  | \(  <_> )    #/        \  ___/\  \___|  | \/\  ___/|  | (  <_> )     \033[32m#|#|
|#|#\033[37m     #\__|  \__  /__|   \____/ *  #/_______  /\___  >\___  >__|    \___  >__|  \____/      \033[32m#|#|
|#|#\033[37m               \/                          \/     \/     \/            \/                  \033[32m#|#|
|#|#                                                                                           #|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|

    """)   

def InicioParOImpar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    \033[32m
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
|#|#                                                                                 #|#|
|#|#\033[37m      __________                            __                                   \033[32m#|#|
|#|#\033[37m     #\______   \_____ _______     ____   #|__| _____ ___________ _______        \033[32m#|#|
|#|#\033[37m      #|     ___/\__  \ \  __ \  #/  _ \  #|  |/     \ \___ \__  \ \  __ \       \033[32m#|#|
|#|#\033[37m      #|    |     / __ \|  | \/  (  <_> ) #|  |  Y Y  \  |_> > __ \|  | \/       \033[32m#|#|
|#|#\033[37m      #|____|    (____  /__|     #\____/  #|__|__|_|  /   __(____  /__|          \033[32m#|#|
|#|#\033[37m                      \/                            \/|__|       \/              \033[32m#|#|
|#|#                                                                                 #|#| 
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#| 
    """)      
######################## Reglas de Juegos ########################

def ReglasMayorMenor():
    print("""
\033[32m
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
|#|#                                                                                               \033[32m#|#|
|#|#\033[37m    REGLAS DE MAYOR O MENOR:                                                                   \033[32m#|#|       
|#|#                                                                                               \033[32m#|#|
|#|#\033[37m    El sistema genera un número aleatorio inicial entre 1 y 1000.                              \033[32m#|#|
|#|#\033[37m    Tu debes escribir si el siguiente número será 'mayor' o 'menor'.                           \033[32m#|#|
|#|#\033[37m    Si \033[32maciertas\033[37m sumas 1 punto.                                                                 \033[32m#|#|           
|#|#\033[37m    Si te \033[31mequivocas\033[37m vuelves a 0 puntos.                                                        \033[32m#|#|
|#|#\033[37m    * En todos los juegos se guarda el mejor puntaje obtenido (Apartado: E - Reportes) *       \033[32m#|#|
|#|#                                                                                               \033[32m#|#|
|#|#\033[37m    Para volver al menú, escribe 'salir' en cualquier momento.                                 \033[32m#|#|
|#|#                                                                                               \033[32m#|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|\033[0m          
    """)
    input("\033[33m    Presiona Enter para comenzar a jugar. \033[0m \n")

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
    InicioMayorMenor()
    MenuJuegos()
    opcionmenujuego = input("\033[33m Seleccione una opción: \033[0m ").lower()

    # Opciones del menú del juego
    if (opcionmenujuego == 'a'):
        finDeJuego = 0
    elif(opcionmenujuego == 'b'):
        ReglasMayorMenor()
        finDeJuego = 0
    elif(opcionmenujuego == 'c'):
        print("volver atras reyes 8==D")


    while(finDeJuego == 0):
        print("\033[33m\n|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|\n\033[0m")
        if (puntaje == 0):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("    Comencemos:")
        print("\n    Salió el número \033[32m",nroAleatorio)

        eleccion = input("\033[0m\n    ¿El siguiente número es\033[33m mayor o menor\033[0m? ").lower()

        # Verificación para que coloque solo 'mayor' y 'menor'
        while(eleccion != "mayor" and eleccion != "menor" and eleccion != "salir"):
            eleccion = input("Opcion incorrecta, coloque 'mayor' o 'menor'(Para vovler, coloque 'salir'): ").lower()
        
        # Verificación de asertividad en la respuesta del usuario
        if(eleccion == "mayor" and nroAleatorio < nroAleatorioParaaAdivinar):
            puntaje = puntaje + 1
            nroAleatorio = nroAleatorioParaaAdivinar
            nroAleatorioParaaAdivinar = random.randint(1,1000)
            print("\n    ¡Adivinaste!\n")
        elif(eleccion == "menor" and nroAleatorio > nroAleatorioParaaAdivinar):
            puntaje = puntaje + 1
            nroAleatorio = nroAleatorioParaaAdivinar
            nroAleatorioParaaAdivinar = random.randint(1,1000)
            print("\n    ¡Adivinaste!\n")
        elif(eleccion == "salir"):
            finDeJuego = 1
        else:
            print("\n    ¡Casi! Intenta nuevamente.\n")
            print(f"    Tu puntaje hasta aquí fué: {puntaje}")
            if(puntajeMayorMenor < puntaje):
                print(f"""
\n    \033[32m¡FELICITACIONES!                 
    Superaste tu marca personal anterior, se ha actualizado tu puntaje máximo.\033[0m \n
""")
                puntajeMayorMenor = puntaje
            input("\033[33m    Presiona Enter para comenzar a jugar. \033[0m \n")
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
    InicioNumeroSecreto()
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
    InicioParOImpar()
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
    
    opc = str(input("\033[33m    Ingrese su opcion: \033[0m"))


    # Validación de opción de usuario
    while (opc<"A" or opc>"E" and opc!= "S"):
        opc = str(input("\033[33m    Ingreso Invalido - reintente:  \033[0m"))
        
    match opc:
        case "A": JuegoMayorMenor()
        case "B": JuegoNumeroSecreto()
        case "C": JuegoBlackJack()#blackjack
        case "D": JuegoParOImpar()
        case "E": cartel() #reporte
        case "S": print('\n\n GRACIAS POR USAR NUESTRO SISTEMA!!!!')

