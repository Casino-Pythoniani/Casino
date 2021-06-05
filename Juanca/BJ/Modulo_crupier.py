#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-CLASES BY JUANCA-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#X X X X X X X X X X X X X X X X X  MODULOS_PERSONALES_BJ X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

from random import randrange  # QUITAR si no es necesario aqui
from playsound import playsound

pierdes = 'Juanca\BJ\pierdes.mp3'

ganas = 'Juanca\BJ\ganas.mp3'
empate = 'Juanca\BJ\c_exit.mp3'
# O O O O O O O O O O O O O O O O O O   CLASS CRUPIER    O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O 

'''  Modulo_crupier.py

    CLASS CRUPIER
    
    random_card ( )

    points ( )
       
    SIN CLASE
    
    compara_puntos ( )   '''

class Crupier:

    ''' Esta clase representara la 'mano' de cada jugador mediante la variable lista de listas self._hand, constará de 2 métodos , random_card () al cual le pondremos como parametro un número, que será 
                la cantidad de cartas que nos 'repartiran' y un lista 'used' que utilizaremos para saber que cartas han sido utilizadas (en todas las 'manos') y que asi no vuelvan a repartirse
        Por otro lado tenemos el método points ( ) al cual le introduciremos como parámetro el valor que hemos decidido para el 'as' durante el juego (Para que sepa como puntuarlo) y nos devolverá
                la puntuación de la mano (self._hand) según las reglas del Black Jack 
        También estan los dos métodos cortos get_hand y reset_hand . El primero devuelve la lista de istas con las cartas 'nuestra mano' y el segudo resetea la mano para volver a empezar
        2 Metodos pequeños mas : add_card( ) y delete_card( ) , el primero añadira una carta (elegida por nosotros en lugar de random) y el segundo borrara una carta de nuestra 'mano' '''
        
    def __init__ ( self ):

        self._hand = [ ]
        self._valor_as = 11
        
#----------------  DEF RANDOM CARD --- CLASS CRUPIER ----------------------------------------------------------------------------------------------------------------------------------------

    def random_card (self,num_cartas,used): 

        palo = ["corazones","picas","trebol","diamantes"]
    
        for i in range (num_cartas):  
        
            while True:
            
                carta_player = []  
                a  , numero = randrange(0,4),randrange(1,14)
                carta_player.append(palo[a])
                carta_player.append(numero)

                if carta_player in used:
                    continue
                else :
                    used.append(carta_player)
                    self._hand.append(carta_player)
                break
            
        return used 


#----------------  DEF POINTS --- CLASS CRUPIER ----------------------------------------------------------------------------------------------------------------------------------------
   
    def points (self ):   

        puntos = 0
        
        for cartas in range (len (self._hand)):
        
            if self._hand [cartas][1] == 11 or self._hand [cartas][1] == 12 or self._hand [cartas][1] == 13:
                puntos += 10
            elif self._hand [cartas][1] == 1: 

                if self._valor_as == 1:

                    puntos += 1
      
                elif self._valor_as == 11:

                    puntos += 11
                
            else:                                                                            
                puntos += self._hand [cartas][1]
    
        return puntos 

#----------------  DEF GET HAND --- CLASS DISPLAYS ----------------------------------------------------------------------------------------------------------------------------------------

    def get_hand (self):
        return self._hand

#----------------  DEF RESET HAND --- CLASS DISPLAYS ----------------------------------------------------------------------------------------------------------------------------------------

    def reset_hand (self):
        self._hand = [ ]  

#----------------  DEF ADD CARD --- CLASS DISPLAYS ----------------------------------------------------------------------------------------------------------------------------------------

    def add_card ( self , card ):
        self._hand.append(card)

#----------------  DEF DELETE CARD --- CLASS DISPLAYS ----------------------------------------------------------------------------------------------------------------------------------------

    def delete_card (self):
        self._hand.pop (-1)


#----------------  COMPARA PUNTOS --- SIN CLASE ----------------------------------------------------------------------------------------------------------------------------------------

''' compara_puntos es una función sin clase a la cual le introducimos como parámetros : los puntos de ambas manos , fichas y apuesta . Esta función nos devolverá un resultado según ganemos, 
            perdamos o empatemos (cosa que dependerá de los puntos) y también nos devolverá las fichas , cuyo valor dependerá del resultado y de la apuesta realizada. 
    Esto lo hace de forma visual apoyandose en las pequeñas funciones de abajo que solo sirven dentro de compara_puntos  '''

def compara_puntos (puntos_player,puntos_dealer,fichas,apuesta):                                                                              
    
    if puntos_dealer > 21:#--Si la IA se pasa pierde..x lo que gana el player
        resultado = "V"

    elif puntos_player > 21:#--Si te pasas de 21 pierdes
        resultado = "X"
        
    elif puntos_player < puntos_dealer:
        resultado = "X"
        
    elif puntos_player == puntos_dealer :  
        resultado = "E"
        
    elif puntos_dealer < puntos_player :
        resultado = "V"
        
    resultado_bj () #--Titulo
    
    if resultado == "V": #--Segun el resultado de estas comparaciones realizaremos distintas acciones
        ganado ()
        playsound(ganas)
        print("                         Felicidades!! Has ganado ",(apuesta*2)
         ,"$!!\n") #--Si ganamos..                                         #              PUNTOS
        fichas += apuesta * 2
        
        
    elif resultado == "X": #--Si perdemos..
        perdido ()
        playsound(pierdes)
        if fichas > 0:
            print("                     Has perdido ",apuesta,"$ !!\n\n            Aun te quedan ",fichas,"€\n")
        else:
            print("                     Has perdido ",apuesta," $ !!\n\n           Te has quedado sin fichas... \n")
            
    elif resultado == "E":#--Si empatamos..
        empatamos ()
        playsound(empate)
        fichas += apuesta
        print ("                    Jugaremos una ronda de desempate..\n")

    return fichas , apuesta          



def resultado_bj ():
    print('''

                            ██████╗░███████╗░██████╗██╗░░░██╗██╗░░░░░████████╗░█████╗░██████╗░░█████╗░
                            ██╔══██╗██╔════╝██╔════╝██║░░░██║██║░░░░░╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
                            ██████╔╝█████╗░░╚█████╗░██║░░░██║██║░░░░░░░░██║░░░███████║██║░░██║██║░░██║
                            ██╔══██╗██╔══╝░░░╚═══██╗██║░░░██║██║░░░░░░░░██║░░░██╔══██║██║░░██║██║░░██║
                            ██║░░██║███████╗██████╔╝╚██████╔╝███████╗░░░██║░░░██║░░██║██████╔╝╚█████╔╝
                            ╚═╝░░╚═╝╚══════╝╚═════╝░░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░╚════╝░

                                                              ''')
def empatamos ():
    print ('''
                        ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ 

                                        █▀▀ █▀▄▀█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ 
                                        █▀▀ █░▀░█ █░░█ █▄▄█ ░░█░░ █▀▀ 
                                        ▀▀▀ ▀░░░▀ █▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀

                        ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ 
                      ''')

def perdido ():
    print ('''
                        ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ 

                                    █░░█ █▀▀█ █▀▀ 　 █▀▀█ █▀▀ █▀▀█ █▀▀▄ ░▀░ █▀▀▄ █▀▀█ 
                                    █▀▀█ █▄▄█ ▀▀█ 　 █░░█ █▀▀ █▄▄▀ █░░█ ▀█▀ █░░█ █░░█ 
                                    ▀░░▀ ▀░░▀ ▀▀▀ 　 █▀▀▀ ▀▀▀ ▀░▀▀ ▀▀▀░ ▀▀▀ ▀▀▀░ ▀▀▀▀

                        ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ 
                             ''')
    
def ganado () :
    print  ('''

                        ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ 

                                    █░░█ █▀▀█ █▀▀ 　 █▀▀▀ █▀▀█ █▀▀▄ █▀▀█ █▀▀▄ █▀▀█ 
                                    █▀▀█ █▄▄█ ▀▀█ 　 █░▀█ █▄▄█ █░░█ █▄▄█ █░░█ █░░█ 
                                    ▀░░▀ ▀░░▀ ▀▀▀ 　 ▀▀▀▀ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀░ ▀▀▀▀

                        ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ 
                                ''')

def titulo_mano ():
    print  ('''


                        ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ 

                            █▀▀ ░▀░ █▀▀▀ █░░█ ░▀░ █▀▀ █▀▀▄ ▀▀█▀▀ █▀▀ 　 █▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ 
                            ▀▀█ ▀█▀ █░▀█ █░░█ ▀█▀ █▀▀ █░░█ ░░█░░ █▀▀ 　 █░▀░█ █▄▄█ █░░█ █░░█ 
                            ▀▀▀ ▀▀▀ ▀▀▀▀ ░▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ 　 ▀░░░▀ ▀░░▀ ▀░░▀ ▀▀▀▀

                        ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ 
                     ''')






