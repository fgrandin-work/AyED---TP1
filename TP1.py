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

# acá comienza el Programa Principal
opc = " " # así lo obligo a entrar al mientras y lo convierto en un Repetir

while (opc!="S"):
    MENU()
    opc = str(input("Ingrese su opcion: "))
    while (opc<"A" or opc>"E" and opc!= "S"):
        opc = str(input("Ingreso Invalido - reintente "))
        match opc:
            case "A": Juego1
            case "B": Juego2
            case "C": cartel()#blackjack
            case "D": Juego4t
            case "E": cartel()#reporte
            case "S": print('\n\n GRACIAS POR USAR NUESTRO SISTEMA!!!!')