
from casino_pythoniani_modules import *
# from bingo.main_binhimport *
# from traga.main_traga import *
from Ruleta_Europea.tableromovimiento import *

fichas = 50

while True:
    ejecutar_menu_casino()
    juego = return_juegos()
    if juego == 'bingo':
        ejecutar_bingo(fichas)
        #fichas = dinero(fichas) # falta implementar un contador del dinero
    if juego == "traga":
        fichas,opcion = ejecutar_traga(fichas)

    if juego == "ruleta":
        ejecutar_ruleta()
        
