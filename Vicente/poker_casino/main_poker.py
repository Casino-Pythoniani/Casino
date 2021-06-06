#Se importan las clases que hay en el archivo poker_clases.py
from Vicente.poker_casino.poker_modules import *
#Se importa el módulo OS para crear la función de limpiar la pantalla
import os
clear = lambda: os.system('cls') 

#Se importa el módulo Time
from time import sleep

#Variables
#Valores para el juego
def ejecutar_poker(fichas):
    bote = 0
    #Baraja_poker pasa a ser un objeto
    baraja_poker = Baraja()

    jugador = Jugador(False,fichas)
    cpu1 = Jugador()
    cpu2 = Jugador()
    cpu3 = Jugador()
    cpu4 = Jugador()
    cpu5 = Jugador()

    jugadores = [jugador,cpu1,cpu2,cpu3,cpu4,cpu5]

    partida_poker = True

    print('\n'*33)
    while partida_poker:
        clear()
        jugadores = resetear_turno(jugadores) #CAMBIA LAS BLINDS CADA TURNO, RESETEA LAS MANOS, ELIMINA A LOS JUGADORES QUE NO ESTAN EN PARTIDA
        turnos = True
        valores_final = 0
        for i in range(1,5):
            if i == 1:   #PREFLOP
                jugadores = limpiar_elementos(jugadores)
                mesa_poker = []
                baraja_poker.barajar()           
                
                baraja_poker.repartir(jugador.mano)
                baraja_poker.repartir(cpu1.mano)
                baraja_poker.repartir(cpu2.mano)
                baraja_poker.repartir(cpu3.mano)
                baraja_poker.repartir(cpu4.mano)
                baraja_poker.repartir(cpu5.mano)
                baraja_poker.repartir(jugador.mano)
                baraja_poker.repartir(cpu1.mano)
                baraja_poker.repartir(cpu2.mano)
                baraja_poker.repartir(cpu3.mano)
                baraja_poker.repartir(cpu4.mano)
                baraja_poker.repartir(cpu5.mano)
            
                copia_jugadores = jugadores.copy()
                valores_final += 1

            if i == 2: #FLOP
                jugadores = limpiar_elementos(jugadores)
                baraja_poker.quemar()
                baraja_poker.repartir(mesa_poker)
                baraja_poker.repartir(mesa_poker)
                baraja_poker.repartir(mesa_poker)
                valores_final += 1
            
            if i == 3: #TURN
                jugadores = limpiar_elementos(jugadores)
                baraja_poker.quemar()
                baraja_poker.repartir(mesa_poker)
                valores_final += 1
                
            if i == 4: #RIVER
                jugadores = limpiar_elementos(jugadores)
                baraja_poker.quemar()
                baraja_poker.repartir(mesa_poker)
                valores_final += 1
            
            while turnos:

                print(("\033[F") * 38)
                display_tablero_poker(jugador,cpu1,cpu2,cpu3,cpu4,cpu5,mesa_poker,bote)
                
                if copia_jugadores[-1].seguir_mano == True:
                    copia_jugadores[-1].decision()
                    if copia_jugadores[-1].cpu == True:
                        pass
                        sleep(1)
                    
                    print(("\033[F") * 38)
                    display_tablero_poker(jugador,cpu1,cpu2,cpu3,cpu4,cpu5,mesa_poker,bote)
                    
                    if copia_jugadores[-1].salir == True:
                        turnos = False
                        partida_poker = False
                        break
                        return jugador.fichas

                    if copia_jugadores[-1].decidir == 'Igualar─':
                        copia_jugadores.insert(0,copia_jugadores[-1])
                        del copia_jugadores[-1]
                    
                    elif copia_jugadores[-1].decidir == '──Irse──':
                        copia_jugadores.insert(0,copia_jugadores[-1])
                        del copia_jugadores[-1]
                    
                    elif copia_jugadores[-1].decidir == '─Subir──':
                        pila = []
                        pila.append(copia_jugadores[-1])
                        del copia_jugadores[-1]
                        copia_jugadores = limpiar_elementos(copia_jugadores)
                        copia_jugadores.insert(0,pila[0])
                        del pila
                        
                if copia_jugadores[-1].seguir_mano == False:
                    copia_jugadores[-1].decidir = '──Irse──'
                    copia_jugadores.insert(0,copia_jugadores[-1])
                    del copia_jugadores[-1]
                
                contador_retirada = 0
                for i in copia_jugadores:
                    if i.decidir == '──Irse──':
                        contador_retirada += 1

                if contador_retirada == (len(copia_jugadores)-1):
                    for i in copia_jugadores:
                        bote += i.fichas_apostadas
                        i.fichas_apostadas = 0
                    for i in copia_jugadores:
                        if i.decidir != '──Irse──':
                            i.fichas += bote
                            bote = 0
                            turnos = False
                            sleep(2)
                            break   

                pasar_turno = 0
                for i in copia_jugadores:
                    if i.decidir != '────────':
                        pasar_turno += 1               

                reparto = 0             
                if pasar_turno == len(copia_jugadores):
                    copia_jugadores = limpiar_elementos(copia_jugadores)
                    resetear_apuestas()
                    for i in copia_jugadores:
                        bote += i.fichas_apostadas
                        i.fichas_apostadas = 0
                    
                    if valores_final == 4 and contador_retirada != (len(copia_jugadores)-1):
                        copia_jugadores = valores(copia_jugadores,mesa_poker)
                        for i in copia_jugadores:
                            if i.victoria == True:
                                reparto += 1

                        if reparto > 1:                    
                            bote = bote//reparto
                        else:
                            bote = bote
                            
                        for i in copia_jugadores:
                            if i.victoria == True:
                                i.fichas += bote
                        bote = 0

                        print(("\033[F") * 38)
                        display_tablero_poker(jugador,cpu1,cpu2,cpu3,cpu4,cpu5,mesa_poker,bote)
                        sleep(3)
                        
                    sleep(1)
                    break     
                    
                print(("\033[F") * 38)
                display_tablero_poker(jugador,cpu1,cpu2,cpu3,cpu4,cpu5,mesa_poker,bote)
                
    return jugador.fichas
        
        