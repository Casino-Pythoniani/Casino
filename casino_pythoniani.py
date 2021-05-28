
from Menu.casino_pythoniani_modules import *
from Vicente.bingo__casino.main_bingo import *
#from Vicente.caballos_casino.carrera_caballos import *
from Alejandro.tragaperras.main_traga import *
from Ruleta_Europea.tableromovimiento import *
from Lucas.dados import *
#from Juanca.Tycoon.clases_tycoon import *
#from Juanca.BJ.Black_Jack import *
#from Ruben.baccarat import *
#from poker import *



fichas = 100
tecla= ""

while tecla != "Key.esc" and fichas > 0:
    juego,tecla = ejecutar_menu_casino()
    if juego == 'bingo':
        fichas = ejecutar_bingo(fichas)
    elif juego == "traga":
        fichas = ejecutar_traga(fichas)
    elif juego == "ruleta":
        fichas = ejecutar_ruleta(fichas)
##    elif juego == "blackjack":
##            ejecutar_BJ()
    elif juego == "dados":
        fichas = ejecutar_dados(fichas)
##    elif juego == "poker":
##        ejecutar_poker()
##    elif juego == "caballos":
##        ejecutar_caballos()
##    elif juego == "baccarat":
##        ejecutar_baccarat()
    
    
        

    
