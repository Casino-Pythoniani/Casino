
## O O O O O O O O O O O O O O O O O O  BLACK JACK  O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O 

''' Para empezar importamos crupier , esta clase sirve para crear objetos que representen las 'manos' de cartas , creamos con esta 2 'manos':  la nuestra (player) y la de nuestro rival (dealer).
        De este modulo importamos también la función compara_puntos() que sirve para determinar quien gana según la pntuación y gestionar las fichas según apuesta y resultado de la partida.
    Importamos displays , esta es la clase principal y contiene los displays de todas las elecciones del juego asi como los actos que conllevan estas elecciones, creamos con esta clase el objeto display   '''

fichas =500
from Modulo_crupier import Crupier
from Modulo_crupier import compara_puntos
from Modulo_crupier import titulo_mano
from playsound import playsound
from Modulo_display import displays

import os
clear = lambda: os.system('cls')
from time import sleep

cont = 'True'
print ('\n'*8,'\t'*6,' POR FAVOR EXTIENDA LA PANTALLA')
sleep(2)
clear()

while cont == 'True':

    display = displays ( )  # OBJ
    player = Crupier ( )    # OBJ
    dealer = Crupier ( )    # OBJ
    display._fichas = fichas

    '''  ==> PRINCIPIO <==

        Utilizamos este bucle para poder volver a jugar otra ronda (se pregunta al final) , primero reseteamos la lista de cartas usadas y le damos a la carta 'as' un valor de 11 por defecto.
            Luego (.reset_hand) reseteamos las cartas de cada 'mano' por si venimos de rondas anteriores.
            Finalmente repartimos dos cartas a cada manos según dictan las reglas de este juego.  '''

    used_cards = [ ]
    as_card = 11

    player.reset_hand ( )
    dealer.reset_hand ( )

    display.actions_apuesta ( )
    apuesta,fichas = display.apuesta_var ( )

    used_cards = player.random_card (2,used_cards)
    used_cards = dealer.random_card (2,used_cards)
   
    '''  ==> SI TENEMOS 2 CARTAS CON EL MISMO NÚMERO <== 
    
        En el caso de tener 2 cartas con el mismo número según dictan las reglas del juego podemos elegir jugar con 2 manos, cada una de las 'iguales ' irán a una mano y se repartirá una nueva por mano.
        Esta parte consta solo de 2 pasos, en el 1 mediante el 'if' comprobamos si las cartas tienen el mismo número y en caso de tenerlo mediante display.manos_bj() mostramos un display que 
               pregunte si queremos jugar con dos manos o seguir con una y nos devuelve la elección tomada 'hands'
        A partir de aqui el programa se divide en 2 partes JUGAMOS CON 1 MANO // JUGAMOS CON 2 MANOS , según la elección tomada.
        Adjunto debajo bateria de prueba para 2 manos (fuerza tener 2 cartas 'iguales') 
        Adjunto debajo bateria de prueba para as (fuerza tener un 'as' en la mano) '''

    # # PRUEBA XA 2 MANOS   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # lista_2 = [['trebol', 10], ['corazones', 10]]
    # player.reset_hand ( )
    # player.add_card (lista_2 [0])
    # player.add_card (lista_2 [1])

    # #   PRUEBA PARA AS

    # player.delete_card ( )
    # player.add_card (['corazones',1])

    if player.get_hand()[0][1] == player.get_hand()[1][1] and (apuesta*2) < fichas:
        hands = display.manos_bj ()

    else:

        hands = 1

    '''  PASO 1 => PREPARAR MANOS , Preparamos las manos en caso de jugar 'a 2 ' . Segun las reglas como se explica arriba '''

    if hands == 2 :

        player_2 = Crupier  ( )
        player_2.add_card (player.get_hand () [1])
        used_cards = player_2.random_card (1,used_cards)

        player.delete_card ( )
        used_cards = player.random_card (1,used_cards)

        fichas -= apuesta

    ''' PASO 2 ==> BUCLE INTELIGENTE  , Este bucle sera in range 2 , si jugamos una mano saltara una vuelta si jugamos 2 manos cambiaremos player x player_2 al final del bucle  '''
    
     
    for z in range (2):
        
        eleccion = 0
        have_as = 'False'

        while eleccion != 'plantar' and eleccion != 'doblar':

            for i in player.get_hand():

                if i [1] == 1 : 
                    have_as = 'True' 

            if player.points () == 21 :
                eleccion = 'plantar'

            elif player.points () > 21 :

                if have_as == 'False' or (player.points()-10 ) > 21 or player._valor_as==1 : 
                    eleccion = 'plantar'

                else:
                    display.tablero (dealer.points(),player.points(),player.get_hand(),dealer.get_hand())
                    print('\n\nTE HAS PASADO.. PERO AUN PUEDES BAJAR EL VALOR DE TU AS')
                    sleep (3)
                    clear ( )
                    eleccion = 'as'

            else: 
                eleccion = display.actions_options (dealer.points(),player.points(),player.get_hand(),dealer.get_hand())
     
            if eleccion == 'pedir' :

                ''' Elegimos 'pedir' ==> Aqui solo añadiremos una carta a nuestra 'mano' , lo haremos con el método random_card ( ) , con esta opción no saldremos del bucle anterior, se nos volverá
                            a ofrecer distintas opciones''' 

                used_cards = player.random_card (1,used_cards) 
            
    
            elif eleccion == 'as' : 

                ''' Elegimos 'gestion-as' ==> En esta opción se nos mostrará el display para elegir el valor de nuestro 'as' mediante el método as_points ( ) , el resto de esta parte es para válidar
                            que tengamos la carta 'as' , si no la tenemos no podremos entrar al display. con esta opción no saldremos del bucle anterior, se nos volverá a ofrecer distintas opciones.  '''
              
                if have_as == 'True':   
                    player._valor_as = display.as_points()

            elif eleccion == 'plantar':

                ''' Elegimos 'plantar' ==> Elegimos esta opción para que el dealer robe (hasta tener >= 18 , según reglas) y se comparen los puntos, después se acabará la ronda. Con el primer bucle 
                            conseguimos la parte de que el dealer robe hasta > 17 , una vez acabe con el método compara_puntos ( ) vemos el resultado y lo mostramos  en un pequeño display que se muestra 
                            junto al método display.tablero ( ), Este último nos muestra las cartas de las dos manos para que veamos como han quedado.
                    Por último tenemos el método continue_bj que nos muestra un display en el que elegiremos si queremos jugar otra ronda o salir al menú de juegos. '''

                if player.points () <  21:

                    for i in dealer.get_hand():
                        if i [1] == 1 : 
                            dealer_as = True
                    while dealer.points () < 17 : 
                        used_cards = dealer.random_card (1,used_cards)
                        if dealer.points()  > 21 and dealer_as == True and (dealer.points()-10)  <  21:
                            print('Dealer ha modificado el valor de su as')
                            dealer._valor_as = 1
                            

                display.juego()
                display.tablero (dealer.points(),player.points(),player.get_hand(),dealer.get_hand())
                #clear ( )
                fichas,apuesta = compara_puntos (player.points(),dealer.points(),fichas,apuesta)
                sleep (3)
                clear ( )
                

            elif eleccion == 'doblar':

                ''' Elegimos 'doblar' ==> Esta opción es igual que la anterior con la pequeña diferéncia de que doblaremos nuestra apuesta y pediremos una última carta antes de plantarnos. '''

                used_cards = player.random_card (1,used_cards)

                if player.points () <  21:
                    
                    dealer_as = False
                    for i in dealer.get_hand():
                        if i [1] == 1 : 
                            dealer_as = True
                    while dealer.points () < 17 : 
                        used_cards = dealer.random_card (1,used_cards)
                        if dealer.points()  > 21 and dealer_as == True and (dealer.points()-10)  <  21:
                            print('Dealer ha modificado el valor de su as')
                            dealer._valor_as = 1
                            

                fichas -= apuesta
                apuesta += apuesta
                
                display.juego()
                display.tablero (dealer.points(),player.points(),player.get_hand(),dealer.get_hand())
                #clear ( )
                fichas,apuesta = compara_puntos (player.points(),dealer.points(),fichas,apuesta)
                sleep (3)
                clear ( )
                
        if hands == 1 :
            break


        if z == 0 :
            clear()
            titulo_mano ()
            player.reset_hand ()
            player.add_card (player_2.get_hand () [0])
            used_cards = player.random_card (1,used_cards)
            dealer.reset_hand()
            used_cards = dealer.random_card (2,used_cards)
       
    cont = display.continue_bj (fichas,apuesta)





















































































































































































































































































































































































































































