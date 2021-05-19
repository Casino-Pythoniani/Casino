""" IMPORTAMOS 
Xa que funcione el programa correctamente necesitamos importar playsound para reproducir sonidos ,os para utilizar la lambda clear,
que nos dejara la pantalla a 0 para que no se acumule lo que printeamos y listener, que hara posible capturar las teclas pulsadas """

from playsound import playsound
import os
clear = lambda: os.system('cls')
from time import sleep
from pynput.keyboard import Listener
""" Importamos todo de estos dos modulos , son propios y se encuentran en estos las clases necesarias para el funcionamiento del programa """
from clases_tycoon import *
from display_tycoon import *

ambiente = "casino.mp3"
yuju = "homer.mp3"

""" O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """

"""   PROGRAMA  """

""" O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """

print ('\n'*8,'\t'*6,' POR FAVOR EXTIENDA LA PANTALLA')
sleep(0)
clear()




casino = kasino()
casino.crear_mapa()

display = display_tycoon ()


continuar = "V"


while continuar == "V":

    # playsound(ambiente,False)

    clear()
    resultado_game_options = display.game_options()

    if resultado_game_options == "continue":

        display.siguiente()

    elif resultado_game_options == "estado":

        mostrando = display.opciones_estado()

    elif resultado_game_options == "comprar":

        proveedor = display.opciones_compra ( )

        if proveedor == "maquinas":

            display.maquinas ()
                 
        elif proveedor == "deco":
            
            display.decoration()
            
        elif proveedor == "salir":
            pass


    elif resultado_game_options == "config":
  
            config = display.configuration()
           
            if config == "guardar":
                
                k.titulo_informe()
                casino.guardar_mapa(kasino.mapa)
                casino.guardar_otras(kasino.maquinas,kasino.decoracion,kasino.dia,kasino.dinero)
                print("\n"*3,"\t"*5,"TU PARTIDA HA SIDO GUARDADA")
                playsound(yuju)
                sleep(1)
                clear()

            elif config == "cargar":
                k.titulo_informe()
                kasino.mapa=casino.cargar_mapa()
                casino.cargar_otras()
                print("\n"*3,"\t"*5,"TU PARTIDA HA SIDO CARDADA")
                playsound(yuju)
                sleep(1)
                clear ()

            elif config == "exit":
                break

          
    
