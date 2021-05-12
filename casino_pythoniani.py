
from casino_pythoniani_modules import *
from bingo.main_bingo import *
from traga.main_traga import *

fichas = 50

while True:
    ejecutar_menu_casino()
    juego = return_juegos()
    if juego == 'bingo':
        ejecutar_bingo(fichas)
        #fichas = dinero(fichas) # falta implementar un contador del dinero
    if juego == "traga":
        fichas,opcion = ejecutar_traga(fichas)
        
