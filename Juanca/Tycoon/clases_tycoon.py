

from playsound import playsound
import os
clear = lambda: os.system('cls')
from time import sleep


""" O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """

"""    CLASE CASINO    """

""" O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """

class kasino:

    def __init__(self):

        self.lista_mapa = []
        self.ancho = 40
        self.largo = 30


    def crear_mapa (self):

        for i in range (self.largo):
            a = "   "
            b = []
            for z in range (self.ancho):
                b.append(a)
            self.lista_mapa.append(b)

        for i in range (1,self.ancho -1):
            self.lista_mapa[0][i]="═══"
            self.lista_mapa[self.largo-1][i]="═══"

        for i in range (1,self.largo -1):
            self.lista_mapa[i][0]= "        ║"
            self.lista_mapa[i][self.ancho-1]= "║"
        
        self.lista_mapa [0][0]="        ╔"
        self.lista_mapa [0][self.ancho-1]="╗"
        self.lista_mapa [self.largo-1][0]="        ╚"
        self.lista_mapa [self.largo-1][self.ancho-1]="╝"


    def game (self):

        self.titulo()

        for fila in self.lista_mapa:
            print("".join(fila))



    def titulo (self):

        print ("""
                            
                    ░█████╗░░█████╗░░██████╗██╗███╗░░██╗░█████╗░  ████████╗██╗░░░██╗░█████╗░░█████╗░░█████╗░███╗░░██╗
                    ██╔══██╗██╔══██╗██╔════╝██║████╗░██║██╔══██╗  ╚══██╔══╝╚██╗░██╔╝██╔══██╗██╔══██╗██╔══██╗████╗░██║
                    ██║░░╚═╝███████║╚█████╗░██║██╔██╗██║██║░░██║  ░░░██║░░░░╚████╔╝░██║░░╚═╝██║░░██║██║░░██║██╔██╗██║
                    ██║░░██╗██╔══██║░╚═══██╗██║██║╚████║██║░░██║  ░░░██║░░░░░╚██╔╝░░██║░░██╗██║░░██║██║░░██║██║╚████║
                    ╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚█████╔╝  ░░░██║░░░░░░██║░░░╚█████╔╝╚█████╔╝╚█████╔╝██║░╚███║
                    ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚════╝░  ░░░╚═╝░░░░░░╚═╝░░░░╚════╝░░╚════╝░░╚════╝░╚═╝░░╚══╝
    """)

    def proveedores (self):

        print (""" 
                                
                        ██████╗░██████╗░░█████╗░██╗░░░██╗███████╗███████╗██████╗░░█████╗░██████╗░███████╗░██████╗
                        ██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
                        ██████╔╝██████╔╝██║░░██║╚██╗░██╔╝█████╗░░█████╗░░██║░░██║██║░░██║██████╔╝█████╗░░╚█████╗░
                        ██╔═══╝░██╔══██╗██║░░██║░╚████╔╝░██╔══╝░░██╔══╝░░██║░░██║██║░░██║██╔══██╗██╔══╝░░░╚═══██╗
                        ██║░░░░░██║░░██║╚█████╔╝░░╚██╔╝░░███████╗███████╗██████╔╝╚█████╔╝██║░░██║███████╗██████╔╝
                        ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░
                        """)

    def titulo_maquinas (self):

        print ( """ 
        
                ███╗░░░███╗░█████╗░░██████╗░██╗░░░██╗██╗███╗░░██╗░█████╗░░██████╗  ░█████╗░░█████╗░░██████╗██╗███╗░░██╗░█████╗░
                ████╗░████║██╔══██╗██╔═══██╗██║░░░██║██║████╗░██║██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██╔════╝██║████╗░██║██╔══██╗
                ██╔████╔██║███████║██║██╗██║██║░░░██║██║██╔██╗██║███████║╚█████╗░  ██║░░╚═╝███████║╚█████╗░██║██╔██╗██║██║░░██║
                ██║╚██╔╝██║██╔══██║╚██████╔╝██║░░░██║██║██║╚████║██╔══██║░╚═══██╗  ██║░░██╗██╔══██║░╚═══██╗██║██║╚████║██║░░██║
                ██║░╚═╝░██║██║░░██║░╚═██╔═╝░╚██████╔╝██║██║░╚███║██║░░██║██████╔╝  ╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚█████╔╝
                ╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░  ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚════╝░
                """)






""" O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """

"""   CLASE OBJETOS   """

""" O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """

class objetos ():

    def __init__(self):
        self.tragaperras = [["╔══","═══","══╗"],["║  ","T_P","  ║"],["╚══","═══","══╝"]]
        self.baccarat =  [["╔══","═══","═══","══╗"],["║ B","ACC","ARA","T ║"],["╚══","═══","═══","══╝"]]
        self.dados = [["╔══","═══","══╗"],["║  ","DA2","  ║"],["╚══","═══","══╝"]]
        self.ruleta = [["╔══","═══","══╗"],["║  ","   ","  ║"],["║  ","RUL","  ║"],["║  ","   ","  ║"],["╚══","═══","══╝"]]
        self.poker = [["╔══","═══","═══","══╗"],["║  ","   ","   ","  ║"],["║  "," PO","KER","  ║"],["║  ","   ","   ","  ║"],["╚══","═══","═══","══╝"]]
        self.b_jack =  [["╔══","═══","═══","══╗"],["║  ","BLA","CK ","  ║"],["║  ","  J","ACK","  ║"],["╚══","═══","═══","══╝"]]
        self.bingo = [["B ▀"," ▀ ","▀ B"],["I ▀"," ▀ ","▀ I"],["N ▀"," ▀ ","▀ N"],["G  ","▀▀▀","  G"],]
        self.carreras = [["H O"," R ","S E"],["R o"," o ","o R"],["U o"," o ","o U"],["N  ","▄▄▄","  N"],]



    def printea (self):
        for fila in self.tragaperras:
            print("".join(fila))
        print ("")
        for fila in self.baccarat:
            print("".join(fila)) 
        print ("")
        for fila in self.dados:
            print("".join(fila))
        print ("")     
        for fila in self.ruleta:
            print("".join(fila))
        print ("")    
        for fila in self.poker :
            print("".join(fila))
        print ("")    
        for fila in self.b_jack :
            print("".join(fila))
        print ("")    
        for fila in self.bingo :
            print("".join(fila))
        print ("")    
        for fila in self.carreras :
            print("".join(fila))
