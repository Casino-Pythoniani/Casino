from Vicente.bingo__casino.bingo_modules import *
from Vicente.bingo__casino.bingo_ascii import *
from time import sleep
from random import randrange
import os
clear = lambda: os.system('cls') 
bucle_menu = True
num_cartones = 3
#fichas = 500
global fichas

def ejecutar_bingo(fichas):
    
    while True:
        if fichas <= 0:
            break
        menu_bingo_ejecucion(fichas)
        num_cartones = numero_de_cartones()
        cpu1 = crear_carton()
        cpu2 = crear_carton()
        cpu3 = crear_carton()
        cpu4 = crear_carton()
        cpu5 = crear_carton()
        cpu6 = crear_carton()

        if num_cartones == 1:
            jugador1 = crear_carton()
            fichas -= 50
        elif num_cartones == 2:
            jugador1 = crear_carton()
            jugador2 = crear_carton()
            fichas -= 100

        elif num_cartones == 3:
            jugador1 = crear_carton()
            jugador2 = crear_carton()
            jugador3 = crear_carton()
            fichas -= 150
        elif num_cartones == 0:
            break

        contador_linea = 0
        contador_bingo = 0

        while True:
            if num_cartones == 1:
                clear()
                display_numeros()
                
                #JUGADOR
                jugador1 = comprobar_numeros(jugador1)
                display_carton(jugador1)
                #LINEA
                if contador_linea == 0:
                    if linea(jugador1) == True:
                        premio_linea()
                        fichas += 70
                        contador_linea += 1
                        sleep(3)
                #BINGO
                if contador_bingo == 0:
                    if bingo(jugador1) == True:
                        premio_bingo()
                        fichas += 130
                        contador_bingo += 1
                        sleep(3)
                        break

                sleep(0.7)
                

            elif num_cartones == 2:
                clear()
                display_numeros()

                #JUGADOR
                jugador1 = comprobar_numeros(jugador1)
                display_carton(jugador1)

                jugador2 = comprobar_numeros(jugador2)
                display_carton(jugador2)

                #LINEA
                if contador_linea == 0:
                    if linea(jugador1) == True:
                        premio_linea()
                        fichas += 130
                        contador_linea += 1
                        sleep(3)
                
                if contador_linea == 0:
                    if linea(jugador2) == True:
                        premio_linea()
                        fichas += 130
                        contador_linea += 1
                        sleep(3)

                #BINGO
                if contador_bingo == 0:
                    if bingo(jugador1) == True:
                        premio_bingo()
                        fichas += 170
                        contador_bingo += 1
                        sleep(3)
                        break
                
                if contador_bingo == 0:
                    if bingo(jugador2) == True:
                        premio_bingo()
                        fichas += 170
                        contador_bingo += 1
                        sleep(3)
                        break

                sleep(0.7)

            elif num_cartones == 3:
                clear()
                display_numeros()

                #JUGADOR
                jugador1 = comprobar_numeros(jugador1)
                display_carton(jugador1)

                jugador2 = comprobar_numeros(jugador2)
                display_carton(jugador2)

                jugador3 = comprobar_numeros(jugador3)
                display_carton(jugador3)

                #LINEA
                if contador_linea == 0:
                    if linea(jugador1) == True:
                        premio_linea()
                        fichas += 170
                        contador_linea += 1
                        sleep(3)
                
                if contador_linea == 0:
                    if linea(jugador2) == True:
                        premio_linea()
                        fichas += 170
                        contador_linea += 1
                        sleep(3)
                
                if contador_linea == 0:
                    if linea(jugador3) == True:
                        premio_linea()
                        fichas += 170
                        contador_linea += 1
                        sleep(3)

                #BINGO
                if contador_bingo == 0:
                    if bingo(jugador1) == True:
                        premio_bingo()
                        fichas += 270
                        contador_bingo += 1
                        sleep(3)
                        break
                
                if contador_bingo == 0:
                    if bingo(jugador2) == True:
                        premio_bingo()
                        fichas += 270
                        contador_bingo += 1
                        sleep(3)
                        break
                
                if contador_bingo == 0:
                    if bingo(jugador3) == True:
                        premio_bingo()
                        fichas += 270
                        contador_bingo += 1
                        sleep(3)
                        break
                sleep(0.7)

            #CPU
            cpu1 = comprobar_numeros(cpu1)
            cpu2 = comprobar_numeros(cpu2)
            cpu3 = comprobar_numeros(cpu3)
            cpu4 = comprobar_numeros(cpu4)
            cpu5 = comprobar_numeros(cpu5)
            cpu6 = comprobar_numeros(cpu6)
            
            #LINEA
            if contador_linea == 0:
                if linea(cpu1) == True:
                    premio_linea_cpu()
                    contador_linea += 1
                    sleep(3)
            
            if contador_linea == 0:
                if linea(cpu2) == True:
                    premio_linea_cpu()
                    contador_linea += 1
                    sleep(3)
            
            if contador_linea == 0:
                if linea(cpu3) == True:
                    premio_linea_cpu()
                    contador_linea += 1
                    sleep(3)
            
            if contador_linea == 0:
                if linea(cpu4) == True:
                    premio_linea_cpu()
                    contador_linea += 1
                    sleep(3)
            
            if contador_linea == 0:
                if linea(cpu5) == True:
                    premio_linea_cpu()
                    contador_linea += 1
                    sleep(3)
            
            if contador_linea == 0:
                if linea(cpu6) == True:
                    premio_linea_cpu()
                    contador_linea += 1
                    sleep(3)

            #BINGO
            if contador_bingo == 0:
                if bingo(cpu1) == True:
                    premio_bingo_cpu()
                    contador_bingo += 1
                    sleep(3)
                    break
            
            if contador_bingo == 0:
                if bingo(cpu2) == True:
                    premio_bingo_cpu()
                    contador_bingo += 1
                    sleep(3)
                    break
            
            if contador_bingo == 0:
                if bingo(cpu3) == True:
                    premio_bingo_cpu()
                    contador_bingo += 1
                    sleep(3)
                    break
            
            if contador_bingo == 0:
                if bingo(cpu4) == True:
                    premio_bingo_cpu()
                    contador_bingo += 1
                    sleep(3)
                    break

            if contador_bingo == 0:
                if bingo(cpu5) == True:
                    premio_bingo_cpu()
                    contador_bingo += 1
                    sleep(3)
                    break
            
            if contador_bingo == 0:
                if bingo(cpu6) == True:
                    premio_bingo_cpu()
                    contador_bingo += 1
                    sleep(3)
                    break
    return fichas

#ejecutar_bingo()      
