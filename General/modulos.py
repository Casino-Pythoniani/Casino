# Es solo un ejemplo, asi no se puede printear cartas seguidas.
ejemplo_carta_1="""  
        ╔═════╗
        ║♥    ║
        ║  k  ║
        ║    ♥║
        ╚═════╝ """

#------------------------------ XA OBTENER CARTA ALEATORIA ---------------------------------------------------

from random import randrange  #!!!  necesitamos tener importado randrange:   from random import randrange
#!!!x probar!!! limites variable etc...

palo=["corazones","picas","trebol","diamantes"]

def random_card (num_cartas,lista_cartas): #--Esta funcion crea cartas aleatorias, el primer parametro ha de ser un int y el segundo una lista
    for i in range (num_cartas):  #-- Xa crear n cantidad de cartas
        carta_player=[]  #-- Lista xa informacion de 1 carta, la que estamos haciendo
        a=randrange(0,4)#-- Xa elegir palo random de la lista palo  
        carta_player.append(palo[a]) #-- Añadimos el palo de la carta en curso a la lista
        numero=randrange(1,13) #-- Xa elegir numero carta de forma random
        carta_player.append(numero) #-- Añadimos el numero de la carta en curso a la lista
        lista_cartas.append(carta_player) #-- Añadimos la carta random ya creada a una lista de cartas dada x parametro ( nuestra mano)
    return lista_cartas #-- Devolvemos la lista dada x parametro que ahora contendra nuestra mano mas las cartas nuevas en una lista de listas.

#--En esta funcion crearemos cartas aleatorias,y las añadiremos a una lista (nuestra mano de cartas) dada x parametro ya que puede contener cartas ya durante el juego
#    esa lista la pondremos en return asi nos devolverá las cartas que ya teniamos (en mano) y las creadas por nuestra funcion.
#--La función tiene el siguiente funcionamiento: El primer bucle sirve xa crear n cantidad de cartas, carta_player es una lista donde guardaremos la información (numero y palo)
#    de una carta. Creamos un palo aleatorio y un numero aleatorio, lo añadimos a carta_player que contiene la informacion de una sola carta ( la creada) y añadimos esta lista a otra
#    dada por parámetro que sera nuestra mano. hacemos return de esta lista.
#-- EJEMPLO ==> mi_mano = random_card (2,mi_mano), necesitamos : from random import randrange

#----- DEJO COMENTADO EL TEST QUE LE HICE A LA FUNCION-------

##mi_mano=[]
##mi_mano=random_card(5,mi_mano)
##print (mi_mano)


#-------------------------------XA IMPRIMIR LAS CARTAS---------------------------------------------------------

def print_c (list_to_print): #--Esta función imprime las cartas de una lista de listas <== IMP. que sera la mano del jugador
    num_cartas=len(cartas_player)#--Xa saber cuantas cartas vamos a printear
    for i in range (num_cartas):
    print ("╔═════╗",end="")
    print("")
    for i in range (num_cartas):    
       print (dicc_palo[cartas_player [i][0]],end="")
    print("")
    for i in range (num_cartas):
        print(dicc_card[cartas_player [i][1]],end="")
    print("")
    for i in range (num_cartas):    
       print (dicc_palo2[cartas_player [i][0]],end="")
    print("")
    for i in range (num_cartas):
        print("╚═════╝",end="")
    print("")





    
