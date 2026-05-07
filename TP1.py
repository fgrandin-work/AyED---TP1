import random

puntajeMayorMenor = 0 

def cartel():
    print("....en construcción...")

def MENU():
    print("........MENU PRINCIPAL. ")
    print("A- Mayor o Menor ")
    print("B- Numero Secreto. ")
    print("C- BlackJack Simple ")
    print("D- Dados.- Par o impar ")
    print("E- Reporte ")
    print("S- Fin DEL PROGRAMA")

def MayorMenor():
    global puntajeMayorMenor
    nroAleatorio = random.randint(1,1000)
    puntaje = 0
    finDeJuego = 0

    print("A.Iniciar juego")
    print("B.Ver reglas")
    print("C.Volver al menu")

    while(finDeJuego == 0):
        print(nroAleatorio)
        nroAleatorioParaaAdivinar = random.randint(1,1000)

        while(nroAleatorioParaaAdivinar == nroAleatorio):
            nroAleatorioParaaAdivinar = random.randint(1,1000)

        print("¿Es mayor o menor?")
        eleccion = str(input()).lower()
        while(eleccion != "mayor" and eleccion != "menor"):
            print("Opcion incorrecta, intente nuevamente")
            eleccion = str(input()).lower()
        
        if(eleccion == "mayor" and nroAleatorio < nroAleatorioParaaAdivinar):
            puntaje = puntaje + 1
            nroAleatorio = nroAleatorioParaaAdivinar
        elif(eleccion == "menor" and nroAleatorio > nroAleatorioParaaAdivinar):
            puntaje = puntaje + 1
            nroAleatorio = nroAleatorioParaaAdivinar
        else:
            print("perdiste burrazo")
            if(puntajeMayorMenor < puntaje):
                puntajeMayorMenor = puntaje
                finDeJuego = 1
            
         

    print(nroAleatorio)

def NumeroSecreto():
    IntentosRestantes = 4
    nroAleatorio = random.randint(1,100)
    finDeJuego = 0
    
    print("Ingrese un numero:")
    nroElejido = int(input())

    #Valida que el número ingresado este entre 1 y 100
    while(nroElejido < 1 or nroElejido > 100):
        print("El número elejido debe estar entre 1 y 100.")
        print("Ingrese otro número:")
        nroElejido = int(input())
    #agregar validacion 1-100
    while(nroElejido != nroAleatorio and IntentosRestantes > 0):

        if(nroElejido > nroAleatorio):
            print("El número secreto es menor al ingresado.")
            print("Ingrese otro número:")
            nroElejido = int(input())

            while(nroElejido < 1 or nroElejido > 100):
                print("El número elejido debe estar entre 1 y 100.")
                print("Ingrese otro número:")
                nroElejido = int(input())

        else:
            print("El número secreto es mayor al ingresado.")
            print("Ingrese otro número:")
            nroElejido = int(input())

            while(nroElejido < 1 or nroElejido > 100):
                print("El número elejido debe estar entre 1 y 100.")
                print("Ingrese otro número:")
                nroElejido = int(input())

        IntentosRestantes = IntentosRestantes-1

    if(nroElejido == nroAleatorio):
        print("¡Ganaste! El número secreto era:", nroAleatorio)
    else:
        print("¡Perdiste! El número secreto era:", nroAleatorio)

# acá comienza el Programa Principal
opc = " " # así lo obligo a entrar al mientras y lo convierto en un Repetir
#MayorMenor()
NumeroSecreto()
""" 
while (opc!="S"):
    MENU()
    opc = str(input("Ingrese su opcion: "))
    while (opc<"A" or opc>"E" and opc!= "S"):
        opc = str(input("Ingreso Invalido - reintente "))
        match opc:
            case "A": MayorMenor()
            case "B": NumeroSecreto()
            case "C": cartel()#blackjack
            case "D": Juego4t
            case "E": cartel()#reporte
            case "S": print('\n\n GRACIAS POR USAR NUESTRO SISTEMA!!!!') """