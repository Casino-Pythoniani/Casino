
from Menu.casino_pythoniani_modules import *
#from bingo.main_bingo import *
from Tragaperras.main_traga import *
from Ruleta_Europea.tableromovimiento import *
from Juanca.Tycoon.clases_tycoon import *



fichas = 50
tecla= ""

while tecla != "Key.esc" and fichas > 0:
    juego,tecla = ejecutar_menu_casino()
    if juego == 'bingo':
        ejecutar_bingo()
        #fichas = ejecutar_bingo(fichas) # falta devolver el dinero de bingo
    elif juego == "traga":
        fichas = ejecutar_traga(fichas)
    elif juego == "ruleta":
        fichas = ejecutar_ruleta()
        #fichas = ejecutar_ruleta(fichas) # falta devolver el dinero de la ruleta
        # Hay que validar la cantidad de dinero que tiene el jugador, para detenerlo de seguir jugando
    
        

    
