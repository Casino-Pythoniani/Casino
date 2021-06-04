

from time import sleep
from Menu.casino_pythoniani_modules import *

bingo = "X"
dados = "X"
bj= "X"
tragaperras = "X"
baccarat = "X"
ruleta= "X"
caballos = "X"
poker ="X"


#from Juanca.Tycoon.clases_tycoon import *



   
fichas = 300

tecla= ""

while tecla != "Key.esc" and fichas > 0:
    
    juego,tecla = ejecutar_menu_casino(fichas)

#   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X    BINGO    X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X 

    if juego == 'bingo':  

        try:
            if bingo == "X":
                from Vicente.bingo__casino.main_bingo import *
                bingo = "V"
        
            fichas = ejecutar_bingo(fichas)

        except Exception as e:
            print ("Algo ha salido mal durante la ejecucion del bingo")
            print (e)
            sleep (3)

#   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X    DADOS    X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X 

    elif juego == "dados":

        try:
            if dados == "X":
                from Lucas.dados import *
                dados = "V"

            fichas = ejecutar_dados(fichas)

        except Exception as e:
            print ("Algo ha salido mal durante la ejecucion del Crabbs")
            print (e)
            sleep(3)

#   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X    BLACK JACK   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X 

    elif juego == "blackjack":

        try :
            
            if bj == "X":
                from Juanca.Bj.Black_Jack import *
                bj = "V"
                
            fichas = ejecutar_BJ(fichas)

        except Exception as e:
            print ("Algo ha salido mal durante la ejecucion del Black Jack ")
            print (e)
            sleep(3)



#   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X    CABALLOS   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X 

    elif juego == "caballos":

        try:
            if caballos == "X":
                from Vicente.caballos_casino.carrera_caballos import *
                caballos = "V"

            fichas = ejecutar_caballos(fichas)

        except Exception as e:
            print ("Algo ha salido mal durante la ejecucion de la ruleta ")
            print (e)
            sleep(3)



#   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X    TRAGAPERRAS   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X 

    elif juego == "traga":

        try:
            if tragaperras == "X":
                from Alejandro.tragaperras.main_traga import *
                tragaperras = "V"

            fichas = ejecutar_traga(fichas)

        except Exception as e:
            print ("Algo ha salido mal durante la ejecucion de la Tragaperras ")
            print (e)
            sleep(3)



#   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X    BACCARAT   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X 

    elif juego == "baccarat":

        try:
            if baccarat == "X":
                from Ruben.baccarat import *
                baccarat = "V"

            fichas = ejecutar_baccarat(fichas)

        except Exception as e:
            print ("Algo ha salido mal durante la ejecucion del baccarat ")
            print (e)
            sleep(3)



#   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X    RULETA   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X 

    elif juego == "ruleta":

        try:
            if ruleta == "X":
                from Ruleta_Europea.tableromovimiento import *
                ruleta = "V"

            fichas = ejecutar_ruleta(fichas)

        except Exception as e:
            print ("Algo ha salido mal durante la ejecucion de la ruleta ")
            print (e)
            sleep(3)




#   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X    POKER   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X 

    elif juego == "poker":

        try:
            if poker == "X":
                #from poker import *
                poker = "V"

            fichas = ejecutar_poker(fichas)

        except Exception as e:
            print ("Algo ha salido mal durante la ejecucion de la ruleta ")
            print (e)
            sleep(3)





    
    
        

    
