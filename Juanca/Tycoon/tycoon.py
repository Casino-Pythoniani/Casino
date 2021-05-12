from playsound import playsound
import os
clear = lambda: os.system('cls')
from time import sleep
from pynput.keyboard import Listener

from clases_tycoon import *
from display_tycoon import *

""" O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """

"""   PROGRAMA  """

""" O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """

print ('\n'*8,'\t'*6,' POR FAVOR EXTIENDA LA PANTALLA')
sleep(0)
clear()

casino = kasino()
casino.crear_mapa()
display = display_tycoon ()

resultado_tutorial = display.tutorial()
if resultado_tutorial == "V":
    pass
    # Poner aqui un tutorial utilizando un stream en modo read texto

continuar = "V"
casino.game()
sleep(0)
# poner aqui stream read txt con : Bienvenido a tu nuevo casino , ahora esta vacio pero tienes unos pequeños ahorros, utilizalos con cabeza !!
clear() 

while continuar == "V":

    resultado_game_options = display.game_options()

    if resultado_game_options == "continue":
        print("continue is under construction")
        continue

    elif resultado_game_options == "estado":
        print("estado is under construction")
        continue

    elif resultado_game_options == "comprar":
        proveedor = display.opciones_compra ( )

        if proveedor == "maquinas":
            resultado_maquinas = " "

            while resultado_maquinas != "comprar" or resultado_maquinas != "salir":
                resultado_maquinas = display.maquinas ()

                if resultado_maquinas == "tragaperras":
                    display.texto = "ahora soy tragaperras"

                elif resultado_maquinas == "b_jack":
                    display.texto = "ahora soy b jack"

                elif resultado_maquinas == "poker":
                    display.texto = "ahora soy poker"

                elif resultado_maquinas == "baccarat":
                    display.texto = "ahora soy baccarat"

                elif resultado_maquinas == "dados":
                    display.texto = "ahora soy dados"

                elif resultado_maquinas == "ruleta":
                    display.texto = "ahora soy ruleta"

                elif resultado_maquinas == "bingo":
                    display.texto = "ahora soy bingo"

                elif resultado_maquinas == "carreras":
                    display.texto = "ahora soy carreras"

                elif resultado_maquinas == "comprar":
                    # mediante el texto hay que decir que compre el articulo cprrespondiente
                    print ("comprar is under construction")
                    sleep (2)
                    continue

                elif resultado_maquinas == "salir":
                    continue
                
        elif proveedor == "deco":
            print ("deco is under construction")
            sleep(2)
            pass

        elif proveedor == "salir":
            pass


    elif resultado_game_options == "ver":
        casino.game()
        sleep(4)
        clear ()
    
    display.reset()
