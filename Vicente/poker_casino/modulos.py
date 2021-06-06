lista_usadas = []


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-FUNCIONES BY JUANCA-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Es solo un ejemplo, asi no se puede printear cartas seguidas.
ejemplo_carta_1 = """  
        ╔═════╗
        ║♥    ║
        ║  k  ║
        ║    ♥║
        ╚═════╝ """

#------------------------------ XA OBTENER CARTA ALEATORIA ---------------------------------------------------

from random import randrange  
#!!!x probar!!! limites variable etc...

def random_card (num_cartas,list_of_cards): #--Esta funcion crea cartas aleatorias, el primer parametro ha de ser un int y el segundo una lista
    
    global lista_usadas
    lista_usadas.clear()

    palo = ["corazones","picas","trebol","diamantes"]
    
    for i in range (num_cartas):  #-- Xa crear n cantidad de cartas
        
        while True:
            
            carta_player = []  #-- Lista xa informacion de 1 carta, la que estamos haciendo
            a = randrange(0,4)#-- Xa elegir palo random de la lista palo  
            carta_player.append(palo[a]) #-- Añadimos el palo de la carta en curso a la lista
            numero = randrange(1,14) #-- Xa elegir numero carta de forma random
            carta_player.append(numero) #-- Añadimos el numero de la carta en curso a la lista
            
            if carta_player in lista_usadas:
                continue
            else :
                lista_usadas.append(carta_player)
                list_of_cards.append(carta_player) #-- Añadimos la carta random ya creada a una lista de cartas dada x parametro ( nuestra mano)
                break
    
    return list_of_cards #-- Devolvemos la lista dada x parametro que ahora contendra nuestra mano mas las cartas nuevas en una lista de listas.

#--En esta funcion crearemos cartas aleatorias,y las añadiremos a una lista (nuestra mano de cartas) dada x parametro ya que puede contener cartas ya durante el juego
#    esa lista la pondremos en return asi nos devolverá las cartas que ya teniamos (en mano) y las creadas por nuestra funcion.
#--La función tiene el siguiente funcionamiento: El primer bucle sirve xa crear n cantidad de cartas, carta_player es una lista donde guardaremos la información (numero y palo)
#    de una carta. Creamos un palo aleatorio y un numero aleatorio, lo añadimos a carta_player que contiene la informacion de una sola carta ( la creada) y añadimos esta lista a otra
#    dada por parámetro que sera nuestra mano. hacemos return de esta lista.
#-- EJEMPLO ==> mi_mano = random_card (2,mi_mano), necesitamos importar : from random import randrange

#----- DEJO COMENTADO EL TEST QUE LE HICE A LA FUNCION-------

##mi_mano=[]
##mi_mano=random_card(5,mi_mano)
##print (mi_mano)


#-------------------------------XA IMPRIMIR LAS CARTAS---------------------------------------------------------


def print_card (list_of_cards): #--Esta función imprime las cartas de una lista de listas <== IMP. que sera la mano del jugador

    dicc_palo = {"corazones":"║♥    ║","picas":"║♠    ║","trebol":"║♣    ║","diamantes":"║♦    ║"}
    dicc_palo2 = {"corazones":"║    ♥║","picas":"║    ♠║","trebol":"║    ♣║","diamantes":"║    ♦║"}
    dicc_card = {1:"║  A  ║",2:"║  2  ║",3:"║  3  ║",4:"║  4  ║",5:"║  5  ║",6:"║  6  ║",7:"║  7  ║",8:"║  8  ║",9:"║  9  ║",10:"║  10 ║",11:"║  J  ║",12:"║  Q  ║",13:"║  k  ║"}

    num_cartas = len(list_of_cards)#--Xa saber cuantas cartas vamos a printear
    
    for i in range (num_cartas): #-- Xa imprimir linea a linea n cartas 
        print ("╔═════╗",end="") #--Imprime la parte de arriba
    print("")
    
    for i in range (num_cartas):    
       print (dicc_palo[list_of_cards [i][0]],end="") #--Usa un diccionario xa decirle que figura debe printear, n veces
    print("")
    
    for i in range (num_cartas):                      #--Igual que la anterior pero con numeros
        print(dicc_card[list_of_cards [i][1]],end="")
    print("")
    
    for i in range (num_cartas):    
       print (dicc_palo2[list_of_cards [i][0]],end="")#--Xa la figura de abajo, n veces
    print("")
    
    for i in range (num_cartas): #--Parte de abajo de la carta, n veces
        print("╚═════╝",end="")
    print("")

#--Esta funcion imprime cartas una al lado de otra, para que sea asi debe ser linea a linea. Por eso utilizamos bucles for (la cantidad de cartas a printear)
#   para los palos y los numeros. Tambien usamos diccionarios que segun lo que introduzcas imprime. x ej :"picas":"║♠    ║" y asi vamos cambiando segun que cartas.    

#----- DEJO COMENTADO EL TEST QUE LE HICE A LA FUNCION-------

##mi_mano=[['picas', 2], ['corazones', 10], ['picas', 4], ['corazones', 4], ['trebol', 6]]
##print_card (mi_mano)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



