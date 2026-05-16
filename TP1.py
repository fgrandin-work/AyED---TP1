import random
import os


######################## Variables de Puntajes Globales ########################

nombreUsuarioMayorMenor = ''
nombreUsuarioNumeroSecreto = ''
nombreUsuarioParOImpar = ''

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
|#|#\033[37m        __                 __          /\\      ___                 __          \033[32m  #|#|
|#|#\033[37m      #|  |  __ __   ____ |  | __   #_(__)/ #|   |   ____   ____ |__| ____     \033[32m  #|#|
|#|#\033[37m      #|  | |  |  \\_/ ___\\|  |/ /  #/    \\  #|   |  /  _ \\ / ___\\|  |/ ___\\    \033[32m  #|#|
|#|#\033[37m      #|  |_|  |  /\\  \\___|    <  #|   |  \\ #|   |_(  <_> ) /_/  >  \\  \\___    \033[32m  #|#|
|#|#\033[37m      #|____/____/  \\___  >__|_ \\ #|___|  / #|____/\\____/\\___  / |__|\\___  >   \033[32m  #|#|
|#|#\033[37m                        \\/     \\/       \\/              /_____/          \\/    \033[32m  #|#|
|#|#                                                                                 #|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
|#|#|                                                                               |#|#|
|#|#|                              ¡Bienvenido!                                     |#|#|
|#|#|                               ¯¯¯¯¯¯¯¯¯¯                                      |#|#|
|#|#|    \033[37m Selecciona el juego colocando su letra correspondiente (Ej: A):\033[32m           |#|#|
|#|#|    \033[37m A - Juego del menor-mayor                                     \033[32m            |#|#|
|#|#|    \033[37m B - Adivinar el número secreto                                \033[32m            |#|#|
|#|#|    \033[37m C - BlackJack                                                 \033[32m            |#|#|
|#|#|    \033[37m D - Par o impar                                               \033[32m            |#|#|
|#|#|    \033[37m E - Reporte                                                   \033[32m            |#|#|
|#|#|    \033[37m S - Salir del programa                                        \033[32m            |#|#|
|#|#|                                                                               |#|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
    """)

def InicioMayorMenor():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
\033[32m          
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#||#|#||#|#||#|#||#|#|#|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#||#|#||#|#||#|#||#|#|#|#| 
|#|#                                                                                                         #|#|
|#|#\033[37m       _    _                                                                            _________      \033[32m #|#|
|#|#\033[37m     #| \\  / \\  _____  ___.__. ___________     ____      _____   ____   ____   __________\\_____   \\     \033[32m #|#|
|#|#\033[37m     #|  \\/   \\ \\__ \\ <   |  |/  _ \\_  __ \\  #/  _ \\   #/     \\_/ __ \\ /    \\ /  _ \\_  __ \\ /   __/      \033[32m#|#| 
|#|#\033[37m     #|  /\\    \\ / __\\.\\___  (  <_> )  | \\/  (  <_> ) #|  Y Y  \\  ___/|   |  (  <_> )  | \\/|   |         \033[32m#|#| 
|#|#\033[37m     #|_|  |_   (____  / ____|\\____/|__|     #\\____/  #|__|_|  /\\___  >___|  /\\____/|__|   |___|         \033[32m#|#| 
|#|#\033[37m             \\/      \\/\\/                                    \\/     \\/     \\/              <___>         \033[32m#|#| 
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
|#|#\033[37m      #\\   \\ \\  | _____  ____      #/   _____/ ____   ___________   _____/  |_  ____       \033[32m#|#|
|#|#\033[37m      #/ |\\ \\ | ||  __ \\/  _ \\     #\\_____  \\_/ __ \\_/ ___\\_  __ \\_/ __ \\   __\\/  _ \\      \033[32m#|#|
|#|#\033[37m     #/  | \\ \\| ||  | \\(  <_> )    #/        \\  ___/\\  \\___|  | \\/\\  ___/|  | (  <_> )     \033[32m#|#|
|#|#\033[37m     #\\__|  \\__  /__|   \\____/ *  #/_______  /\\___  >\\___  >__|    \\___  >__|  \\____/      \033[32m#|#|
|#|#\033[37m               \\/                          \\/     \\/     \\/            \\/                  \033[32m#|#|
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
|#|#\033[37m     #\\______   \\_____ _______     ____   #|__| _____ ___________ _______        \033[32m#|#|
|#|#\033[37m      #|     ___/\\__  \\ \\  __ \\  #/  _ \\  #|  |/     \\ \\___ \\__  \\ \\  __ \\       \033[32m#|#|
|#|#\033[37m      #|    |     / __ \\|  | \\/  (  <_> ) #|  |  Y Y  \\  |_> > __ \\|  | \\/       \033[32m#|#|
|#|#\033[37m      #|____|    (____  /__|     #\\____/  #|__|__|_|  /   __(____  /__|          \033[32m#|#|
|#|#\033[37m                      \\/                            \\/|__|       \\/              \033[32m#|#|
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
    print("""\033[32m
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
|#|#\033[37m                                                                                                               \033[32m#|#|
|#|#\033[37m\tREGLAS DE NÚMERO SECRETO:                                                                                  \033[32m#|#|
|#|#\033[37m                                                                                                               \033[32m#|#|
|#|#\033[37m\tLa computadora piensa un número entre 1 y 100.                                                             \033[32m#|#|
|#|#\033[37m\tTu deberás ingresar otro numero entre 1 y 100 intentando adivinar el generado por la máquina.              \033[32m#|#|
|#|#\033[37m\tEn cada intento fallido, el sistema debe indicar si el número secreto es mayor o menor                     \033[32m#|#|
|#|#\033[37m\tal que vos ingresaste.                                                                                     \033[32m#|#|
|#|#\033[37m\tTendrás 5 intentos para adivinarlo.                                                                        \033[32m#|#|
|#|#                                                                                                               \033[32m#|#|
|#|#\033[31m    Pierdes\033[37m si se te agotan los intentos.                                                                      \033[32m#|#|
|#|#\033[37m    Si aciertas antes de agotarlos,\033[32m ¡GANAS! \033[37m                                                                   \033[32m#|#|
|#|#\033[37m    * En todos los juegos se guarda el mejor puntaje obtenido (Apartado: E - Reportes) *                       \033[32m#|#|
|#|#                                                                                                               \033[32m#|#|
|#|#\033[37m    Para volver al menú, escriba 'salir'.                                                                      \033[32m#|#|
|#|#                                                                                                               \033[32m#|#|
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|\033[0m
    """)
    input("\033[33m    Presiona Enter para comenzar a jugar. \033[0m \n")

def ReglasParOImpar():
    print("""\033[32m
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|                  
|#|#\033[37m                                                                                                         \033[32m#|#|
|#|#\033[37m    REGLAS DE PAR O IMPAR:                                                                               \033[32m#|#|
|#|#\033[37m                                                                                                         \033[32m#|#|          
|#|#\033[37m    El programa tira 2 dados y suma ambos resultados (Dado de 6 caras: 1 al 6).                          \033[32m#|#|
|#|#\033[37m    Sin ver los resultados de los dados deberás indicar si la suma de los números es par o impar.        \033[32m#|#|
|#|#\033[37m                                                                                                         \033[32m#|#|          
|#|#\033[37m    Si \033[32maciertas\033[37m sumas 1 punto.                                                                           \033[32m#|#|
|#|#\033[37m    Si \033[31mte equivocas\033[37m vuelves a 0 puntos.                                                                  \033[32m#|#|
|#|#\033[37m    * En todos los juegos se guarda el mejor puntaje obtenido(Apartado: E - Reportes) *                  \033[32m#|#|
|#|#\033[37m                                                                                                         \033[32m#|#|        
|#|#\033[37m    Para volver al menú, escriba 'salir'.                                                                \033[32m#|#|
|#|#\033[37m                                                                                                         \033[32m#|#|          
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|          
    """)
    input("\033[33m    Presiona Enter para comenzar a jugar. \033[0m \n")

 
######################## JUEGOS ########################

######################## A - Mayor a menor ########################

def JuegoMayorMenor():
    global nombreUsuarioMayorMenor
    global puntajeMayorMenor
    global vecesJugadoMayorMenor

    nroAleatorio = random.randint(1,1000)
    nroAleatorioParaaAdivinar = random.randint(1,1000)

    puntaje = 0
    finDeJuego = 1
    
    # Menú del juego y nombre usuario
    InicioMayorMenor()
    if(nombreUsuarioMayorMenor == ''):
        nombreUsuarioMayorMenor = input("\033[33m Ingrese su nombre: \033[0m ").capitalize()

    print(f"""
    BIENVENIDO \033[32m{nombreUsuarioMayorMenor}\033[0m!
    A - Iniciar juego
    B - Ver reglas
    C - Volver al menu
    """)

    opcionmenujuego = input("\033[33m Seleccione una opción: \033[0m ").lower()

    # Opciones del menú del juego
    if (opcionmenujuego == 'a'):
        finDeJuego = 0
    elif(opcionmenujuego == 'b'):
        ReglasMayorMenor()
        finDeJuego = 0
    elif(opcionmenujuego == 'c'):
        finDeJuego = 1
    else:
        print("\033[33mIngrese una opción válida.\033[0m ")



    while(finDeJuego == 0):
        print("\033[33m\n|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|\n\033[0m")
        if (puntaje == 0):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("    Comencemos:")
            nroAleatorio = random.randint(1,1000)
            nroAleatorioParaaAdivinar = random.randint(1,1000)
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
    global nombreUsuarioNumeroSecreto
    global vecesJugadoNumeroSecreto
    global ganadasNumeroSecreto
    global perdidasNumeroSecreto

    IntentosRestantes = 4
    nroAleatorio = random.randint(1,100)
    finDeJuego= 1
    
    # Menú del juego y nombre usuario       
    InicioNumeroSecreto()
    if(nombreUsuarioNumeroSecreto == ''):
        nombreUsuarioNumeroSecreto = input("\033[33m Ingrese su nombre: \033[0m ").capitalize()

    print(f"""
    BIENVENIDO \033[32m{nombreUsuarioNumeroSecreto}\033[0m!
    A - Iniciar juego
    B - Ver reglas
    C - Volver al menu
    """)
    opcionmenujuego = input("\033[33m Seleccione una opción: \033[0m ").lower()
    while(opcionmenujuego<"a" or opcionmenujuego>"c"):
        print("Ingrese una opción válida.")
        opcionmenujuego = input("Seleccione una opción: ").lower()

    # Opciones del menú del juego
    if (opcionmenujuego == 'a'):
        finDeJuego= 0
    elif(opcionmenujuego == 'b'):
        ReglasNumeroSecreto()
        finDeJuego = 0
    elif(opcionmenujuego == 'c'):
        finDeJuego = 1  
    
        

    while(finDeJuego == 0):

        os.system('cls' if os.name == 'nt' else 'clear')

        print("\033[33m\n|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|\n\033[0m")
        # Petición y Validación de Tipo de dato ingresado        
        nroIngresado = input("\033[33mIngrese un número: \033[0m")
        valido = 0
        while (valido == 0):
            try:
                nroIngresado = int(nroIngresado)
                valido = 1
            except ValueError:
                print(f"Intente nuevamente.")
                nroIngresado = input("\033[33mIngrese un número: \033[0m")
                
        # Validación por rango
        while(nroIngresado < 1 or nroIngresado > 100):
            print("El número ingresado debe estar entre 1 y 100.")
            print("\033[33mIngrese otro número:\033[0m")
            nroIngresado = int(input())
            
        while(nroIngresado != nroAleatorio and IntentosRestantes > 0):
            
            if(nroIngresado > nroAleatorio):
                print("El número secreto es menor al ingresado.\n")

            elif (nroIngresado < nroAleatorio):
                print("El número secreto es mayor al ingresado.\n")

            IntentosRestantes = IntentosRestantes - 1

            # Petición y Validación de Tipo de dato ingresado
            nroIngresado = input("\033[33mIngrese un número: \033[0m")
            valido = 0
            while (valido == 0):
                try:
                    nroIngresado = int(nroIngresado)
                    valido = 1
                except ValueError:
                    print(f"Intente nuevamente.")
                    nroIngresado = input("\033[33mIngrese un número: \033[0m")
                        
            # Validación por rango
            while(nroIngresado < 1 or nroIngresado > 100):
                print("El número ingresado debe estar entre 1 y 100.")
                print("\033[33mIngrese otro número:\033[0m")
                nroIngresado = int(input())
            

        # Fín del juego
        if(nroIngresado == nroAleatorio):
            vecesJugadoNumeroSecreto += 1
            ganadasNumeroSecreto += 1
            finDeJuego = 1
            print("\n\033[32m¡Ganaste!\033[0m El número secreto era:", nroAleatorio)
        else:
            vecesJugadoNumeroSecreto += 1
            perdidasNumeroSecreto += 1
            finDeJuego = 1
            print("\n\033[31m¡Perdiste!\033[0m El número secreto era:", nroAleatorio)

        print("""
\033[33m\n|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|\n\033[0m
        A - Seguir jugando
        B - Salir a menú principal
        """)
        opcionmenujuego = input("\033[33mSeleccione una opción: \033[0m").lower()
        while(opcionmenujuego<"a" or opcionmenujuego>"b"):
            print("Ingrese una opción válida.")
            opcionmenujuego = input("\033[33mSeleccione una opción: \033[0m").lower()

        if (opcionmenujuego == 'a'):
            IntentosRestantes = 4
            nroAleatorio = random.randint(1,100)
            finDeJuego= 0
        elif(opcionmenujuego == 'b'):
            finDeJuego = 1


######################## C - BLACK JACK ########################

def EnConstruccion():
    print("""
    Estamos construyendo el juego, pronto estará publicado.
    ¡Gracias por tu paciencia!
    """)
    input("Presiona Enter para volver al menú principal.")
    
def JuegoBlackJack():
    os.system('cls' if os.name == 'nt' else 'clear')
    return EnConstruccion()

######################## D - Par o impar ########################

def JuegoParOImpar():
    global nombreUsuarioParOImpar
    global ganadasParOImpar
    global perdidasParOImpar
    global vecesJugadoParOImpar
    finDeJuego = 1

    # Menú del juego y nombre usuario
    InicioParOImpar()
    if(nombreUsuarioParOImpar == ''):
        nombreUsuarioParOImpar = input("\033[33m Ingrese su nombre: \033[0m ").capitalize()

    print(f"""
    BIENVENIDO \033[32m{nombreUsuarioParOImpar}\033[0m!
    A - Iniciar juego
    B - Ver reglas
    C - Volver al menu
    """)
    while(opcionmenujuego<"a" or opcionmenujuego>"c"):
        print("Ingrese una opción válida.")
        opcionmenujuego = input("\033[33m Seleccione una opción: \033[0m ").lower()

    # Opciones del menú del juego
    if (opcionmenujuego == 'a'):
        finDeJuego = 0
    elif(opcionmenujuego == 'b'):
        ReglasParOImpar()
        finDeJuego = 0
    elif(opcionmenujuego == 'c'):
        finDeJuego = 1
    
    os.system('cls' if os.name == 'nt' else 'clear')

    while (finDeJuego == 0):
        dadoA = random.randint(1, 6)
        dadoB = random.randint(1, 6)
        suma = dadoA + dadoB

        # Input
        print("""
\033[33m\n|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|\n\033[0m 
Los dados se hán tirado.
Crees que la suma será \033[33mpar o impar\033[0m?\n
        """)
        respuesta = input("\033[33mRespuesta: \033[0m").lower()

        # Verificación de respuesta (par, impar o salir)
        while (respuesta != 'par' and respuesta != 'impar' and respuesta != 'salir'):
            print("""\n
Respuesta incorrecta. Intente nuevamente.
* Recuerda que solo se permite introducir 'par' o 'impar'(Para salir coloque 'salir').
            """)
            respuesta = input("\033[33mRespuesta: \033[0m").lower()
    
        # Comparación de respuesta del usuario y los dados
        if (suma % 2 == 0 and respuesta == 'par' or suma % 2 != 0 and respuesta == 'impar'):
            ganadasParOImpar += 1
            vecesJugadoParOImpar += 1
            print(f"\n\033[32m¡Acertaste!\033[0m Los números fueron {dadoA} y {dadoB}, y suman {suma}.")
        elif (respuesta == 'salir'):
            finDeJuego = 1
        else:
            print(f"\n\033[31m¡Te equivocaste!\033[0m Los números fueron {dadoA} y {dadoB}, y suman {suma}.")
            vecesJugadoParOImpar += 1
            perdidasParOImpar += 1
######################## REPORTES ########################

def Reportes():

    finDeJuego = 0

    # Mayor y Menor
    global nombreUsuarioMayorMenor
    global vecesJugadoMayorMenor
    global puntajeMayorMenor 
    # Numero Secreto
    global nombreUsuarioNumeroSecreto
    global vecesJugadoNumeroSecreto
    global ganadasNumeroSecreto 
    global perdidasNumeroSecreto 
    # Par o Impar
    global nombreUsuarioParOImpar
    global vecesJugadoParOImpar
    global ganadasParOImpar 
    global perdidasParOImpar 

    print(f""" \033[32m
|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
|#|#                                                             #|#|
|#|#                           REPORTES                          #|#|
|#|#                                                             #|#|
\033[32m|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|
                           
    Mayor y Menor:\033[0m
        Nombre de usuario : {nombreUsuarioMayorMenor}
        Cantidad de veces jugadas: {vecesJugadoMayorMenor}
        \033[32mMejor puntaje:\033[0m {puntajeMayorMenor}

\033[32m|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|

    Número secreto:\033[0m
        Nombre de usuario : {nombreUsuarioNumeroSecreto}
        Cantidad de veces jugadas: {vecesJugadoNumeroSecreto}        
        Cantidad de \033[32mganadas:\033[0m {ganadasNumeroSecreto}
        Cantidad de \033[31mperdidas:\033[0m {perdidasNumeroSecreto}

\033[32m|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|\033[

    Par o Impar:\033[0m
        Nombre de usuario : {nombreUsuarioParOImpar}
        Cantidad de veces jugadas: {vecesJugadoParOImpar}
        Cantidad de \033[32mganadas:\033[0m {ganadasParOImpar}
        Cantidad de \033[31mperdidas:\033[0m {perdidasParOImpar}

\033[32m|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|#|\033[0m
    """)
    input("\033[33mPresiona enter para volver al menu principal.\033[0m")

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
    
    opc = input("\033[33m    Ingrese su opcion: \033[0m").lower()


    # Validación de opción de usuario
    while (opc<"a" or opc>"e" and opc!= "s"):
        MenuGeneral()
        opc = input("\033[33m    Opción inválida. Intente nuevamente:  \033[0m").lower()
    
    match opc:
        case "a": JuegoMayorMenor()
        case "b": JuegoNumeroSecreto()
        case "c": JuegoBlackJack()
        case "d": JuegoParOImpar()
        case "e": Reportes()
        case "s": print('\n ¡GRACIAS POR USAR NUESTRO SISTEMA!')
    if (opc != 's'):
        opc = ''

            

# 