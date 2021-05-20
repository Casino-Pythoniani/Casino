#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-CLASES BY JUANCA-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#X X X X X X X X X X X X X X X X X  MODULOS_PERSONALES_BJ X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

from playsound import playsound
moneda = 'Coin_1.mp3'
monedas = 'Coins_Drop.mp3'
click = 'click.mp3'
reparto = 'c_reparto.mp3'
plantar = 'c_plantar.mp3'
fuera = 'continue.mp3'
out = 'c_exit.mp3'
vida = 'c_round2.mp3'



from time import sleep
import os
clear = lambda: os.system('cls')
from pynput.keyboard import Listener

# O O O O O O O O O O O O O O O O O O   CLASS DISPLAYS    O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O 

'''  Modulo_display.py 

    CLASS DISPLAYS:

        INICIO      init ( )
                    key_actions ( ) 

        APUESTA     display_bj_apuesta ( )
                    actions_apuesta ( )
                    
        2MANOS?     display_2manos ( )
                    manos_bj ( )
                    
        ELECCION    display_bj_options ( )
                    actions_oprions ( )
                    
        AS??        display_as ( )
                    as_points ( )

        CONTINUE?   display_continue ( )
                    continue_bj ( )
                
        OTRAS       tablero ( )
                    print_hand ( )    


    ==> Esta es la estructura de la clase 'displays' , es la clase principal del sotfware para el juego Black Jack y se encarga de mostrar y ejecutar todas las elecciones a lo largo del juego . 

    -En apuesta elegiremos la cantidad de fichas que apostamos.
    -En 2manos elegiremos (en caso de tener dos cartas de igual numero) si queremos jugar con dos manos , o seguir como siempre.
    -En eleccion escogeremos entre (pedir,plantar,doblar o gestionar valor de 'as')
    -En 'as' escogeremos una vez dentro del menu que valor queremos (1 u 11) para nuestra carta.
    -En continue elegimos si queremos jugar otra ronda o volver al menu de juegos.

    - OTRAS: print_hand nos printeara la lista de cartas (nuestra mano), se usara en tablero ( ) para mostrar nuestras cartas junto con las cartas del dealer y las puntuaciones correspondientes.
            La usaremos donde sea necesario, coomo por ej en ELECCION asi ves las cartas y puntos que tienes para poder elegir mejor ( pedir,plantar...)

    - (apuesta,2manos,eleccion,as?,continue?) funcionan las 5 igual . tienen 2 metodos un display que es la parte visual con una lista de listas que emula movimiento entre las casillas de opcciones
            y otro metodo que es el principal que es el que organiza el display , el key logger y key_actions (INICIO) asi conseguimos la parte visual con display, capturar la tecla con key logger
            y dependiendo de en que casilla estemos realizar distintas acciones con key_actions.         
        '''
    





# O O O O O O O O O O O O O O O O O O   CLASS DISPLAYS    O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O 

# X X X X X X X X X X X X X X X X X X INICIO - variables y key_actions   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X 

''' En esta parte (Inicio) pondremos el método constructor (Declara las variables) y el método key_actions (lista,x). El primer parámetro (lista) corresponde a la lista que contiene las opciones
            según el display en el que estemos y el segundo parámetro (x) es un número que diferenciará entre los distintos displays para que key_actions realice distintas acciones al pulsar 
            'enter' según el display en el que nos encontremos. Para emular el movimiento por la lista tendremos  self._posx y self._posy que igualaremos a  ' ◄ ' en la lista correspondiente
            para saber la casilla en la que nos encontramos.
    De esta forma las opciones se elegirán mediante displays usando las direcciones y 'enter'.  '''

class displays:
    
    def __init__ ( self ) :

        self._lista_as = [['   ','   ']] 
        self._lista_continue = [['   ','   ']]
        self._lista_opciones = [['   ','   '],['   ','   ']]
        self._lista_apuesta = [ ['   ','   '],['   ','   '],['   ','   '] ] 
        self._lista_2manos = [['   ','   ']]

        self._apuesta , self._key2 , self._posx , self._posy , self._continuar , self._fin_op ,  self._resultado_opciones  = 0 , 0 , 0 , 0 , 0 , 0 , 0

        self._fin_as_election , self._fin_continue , self._fin_apuesta = "X" , "X" , "X"
        
        self._fichas = 500
        self._valor_as = 11

#----------------  DEF KEY ACTIONS --- CLASS DISPLAYS ----------------------------------------------------------------------------------------------------------------------------------------

    def key_actions (self,lista,x): 

        try:
        
            if self._key2 == 'Key.right' :      # Si pulsas derecha ...

                playsound(click)
                lista[self._posx][self._posy],lista[self._posx][self._posy+1] = lista[self._posx][self._posy+1],lista[self._posx][self._posy]
                self._posy = self._posy + 1

            elif self._key2 =='Key.left' :      # Si pulsas izquierda ...

                playsound(click)
                lista[self._posx][self._posy],lista[self._posx][self._posy-1] = lista[self._posx][self._posy-1],lista[self._posx][self._posy]                                             
                self._posy = self._posy - 1
            
            elif self._key2 =='Key.down' :      # Si pulsas abajo ...

                playsound(click)
                lista[self._posx][self._posy],lista[self._posx+1][self._posy] = lista[self._posx+1][self._posy],lista[self._posx][self._posy]
                self._posx = self._posx + 1
            
            elif self._key2 =='Key.up' :        # Si pulsas arriba ...

                playsound(click)
                lista[self._posx][self._posy],lista[self._posx-1][self._posy] = lista[self._posx-1][self._posy],lista[self._posx][self._posy]
                self._posx = self._posx - 1
            
            elif self._key2 =='Key.enter':       # Si pulsas enter ...
            #  Al pulsar enter tendremos diferentes opciones dependiendo del menú en el que estemos (apuesta,opciones etc..) y este vendrá dado como parámetro 
            
                if x == 1:  #  DISPLAY APUESTAS == Utilizaremos 1 para este display.............................................................................................................
            
                    if lista [0][0] == ' ◄ ': 

                        playsound(moneda)
                        self._fichas -= 5           
                        self._apuesta += 5 

                    elif lista [1][0] == ' ◄ ': 

                        playsound(moneda)
                        self._fichas -= 25           
                        self._apuesta += 25
                    
                    elif lista [2][0] == ' ◄ ':

                        playsound(monedas)
                        self._fichas += self._apuesta
                        self._apuesta = 0
                    
                    elif lista [0][1] == ' ◄ ':  

                        playsound(moneda)                                                                                 
                        self._fichas -= 10
                        self._apuesta += 10
                    
                    elif lista [1][1] == ' ◄ ':
                        
                        playsound(moneda)
                        self._fichas -= 100
                        self._apuesta += 100
                    
                    elif lista [2][1] == ' ◄ ':
                        
                        playsound(moneda)
                        if self._apuesta >= 5:
                            self._fin_apuesta = "V" 
                            self._posx,self._posy = 0,0
                            for i in range (4):
                                playsound(reparto) 
                            
                            
                        
                        else:
                            print ("   No has realizado ninguna apuesta ")
                           
                        
                elif x == 2:  # DISPLAY OPCCIONES JUEGO ==> Utilizaremos el 2 para este display .....................................................................................................       
 
                    if lista [0][0] == ' ◄ ':
                        playsound(reparto)
                        self._resultado_opciones = 'pedir'

                    elif lista [0][1] == ' ◄ ':
                        #playsound(plantar)
                        self._resultado_opciones = 'plantar' 
                    
                    elif lista [1][0] == ' ◄ ':
                        playsound(monedas)
                        playsound(reparto)
                        self._resultado_opciones ='doblar'

                    elif lista [1][1] ==' ◄ ':
                        playsound(reparto)
                        self._resultado_opciones = 'as'
                
                    self._fin_op ="V"         



                elif x == 3: # DISPLAY CONTINUAR ==> Utilizaremos el 3 para este display   .........................................................................................................                                           
 
                    if lista [0][0] == ' ◄ ':
                        playsound(vida)
                        self._continuar = "True"

                    elif lista [0][1] == ' ◄ ':
                        playsound(fuera)
                        self._continuar = "False"
                    
                    self._fin_continue = "V"



                elif x == 4 :  # DISPLAY VALOR DE AS==> Utilizaremos el 4 para este display  ........................................................................................................
               
                    if lista [0][0] ==' ◄ ':
                        playsound(out)
                        self._valor_as =1

                    elif lista [0][1] == ' ◄ ':
                        playsound(out)
                        self._valor_as = 11
                    
                    self._fin_as_election = "V"


                elif x == 5 :  # DISPLAY CUANTAS MANOS ?? ==> Utilizaremos el 5 para este display  .................................................................................................
                    if lista [0][0] == ' ◄ ':
                        playsound(out)
                        self.__manos = 2

                    elif lista [0][1] == ' ◄ ':
                        playsound(out)
                        self.__manos = 1
 
                    self.__fin_2manos = "V"
                                                   
        except:         
            print("")
















# O O O O O O O O O O O O O O O O O O   CLASS DISPLAYS    O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O 

# X X X X X X X X X X X X X X X X X X   APUESTAS - Display y Acciones   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

    ''' En esta parte (Apuestas) tendremos un método pequeño (display_bj_apuesta) que printeará un titulo y unas instrucciones para el menú de apuestas ,  otro método (display_bj_apuesta) que será la parte 
                'visual' , nos mostrará las distintas casillas con sus correspondientes opciones que seleccionaremos desplazando ' ◄ ' por las casillas y seleccionaremos con 'enter'.  
        Por último tenemos el método (actions_apuesta) , este será el único que ejecutemos en el Main ya que gestionará los dos métodos anteriores yl el key logger (capta-teclas) y nos devolverá
                (apuesta,fichas) la apuesta realizada y las fichas restantes. '''

    def titulo_apuesta_bj (self) :

         print ( """\n\n\n\n

                                    ░█████╗░██████╗░██╗░░░██╗███████╗░██████╗████████╗░█████╗░░██████╗
                                    ██╔══██╗██╔══██╗██║░░░██║██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝
                                    ███████║██████╔╝██║░░░██║█████╗░░╚█████╗░░░░██║░░░███████║╚█████╗░
                                    ██╔══██║██╔═══╝░██║░░░██║██╔══╝░░░╚═══██╗░░░██║░░░██╔══██║░╚═══██╗
                                    ██║░░██║██║░░░░░╚██████╔╝███████╗██████╔╝░░░██║░░░██║░░██║██████╔╝
                                    ╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░
                                    Utiliza las 'flechas' para desplazarte y 'Enter' para selecionar
      
                        """)


#----------------  DEF DISPLAY APUESTA --- CLASS DISPLAYS ----------------------------------------------------------------------------------------------------------------------------------------------

    def display_bj_apuesta (self): 

        self._lista_apuesta [self._posx][self._posy] = ' ◄ '

        print('''\n
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥  
            ♣                                                                                                             ♣
            ♦                                                                                                             ♦ 
            ♣                                                                                                             ♣
            ♠                        ╔══════╗       ╔══════╗                                                              ♥
            ♥                        ║  5$  ║ '''+self._lista_apuesta [0][0]+'''   ║  10$ ║ '''+self._lista_apuesta [0][1]+'''                                                          ♠
            ♦                        ╚══════╝       ╚══════╝                                                              ♥
            ♣                                                                APOSTADO == '''+str(self._apuesta).ljust(10)+'''                       ♣ 
            ♠                        ╔══════╗       ╔══════╗                                                              ♠
            ♥                        ║  25$ ║ '''+self._lista_apuesta [1][0]+'''   ║ 100$ ║ '''+self._lista_apuesta [1][1]+'''                                                          ♥ 
            ♦                        ╚══════╝       ╚══════╝                                                              ♦
            ♣                                                                FICHAS RESTANTES == '''+str(self._fichas).ljust(10)+'''               ♣                              
            ♠                         ANULAR  '''+self._lista_apuesta [2][0]+'''   APOSTAR  '''+self._lista_apuesta [2][1]+'''                                                          ♠
            ♥                                                                                                             ♥
            ♣                                                                                                             ♣
            ♠                                                                                                             ♠
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
        ''')

#----------------  DEF ACTIONS APUESTA --- CLASS DISPLAYS ---------------------------------------------------------------------------------------------------------------------------------------------

    def actions_apuesta (self):

        def key_recorder (key):                
      
            self._key2 = str(key)
            l.stop( )

        self._fin_apuesta = 'X'
        while self._fin_apuesta == 'X':
            self.juego()
            self.titulo_apuesta_bj   ( ) 
            self.display_bj_apuesta ( ) 

            with Listener(on_press = key_recorder) as l:  
                l.join( )
            
            self.key_actions (self._lista_apuesta,1) 

            clear ()
        

    def apuesta_var (self) :                             

        return       self._apuesta  , self._fichas 
    












# O O O O O O O O O O O O O O O O O O   CLASS DISPLAYS    O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O 

# X X X X X X X X X X X X X X X X X X   2 MANOS ?? - Para elegir si doblamos mano al obtener 2 cartas iguales   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X 

    
    ''' En esta parte (2 manos ??) tendremos un método  (display_2manos) que será la parte 'visual' , nos mostrará las distintas casillas con sus correspondientes opciones que seleccionaremos desplazando
                     ' ◄ ' por las casillas y seleccionaremos con 'enter'.  
        Por último tenemos el método (manos_bj) , este será el único que ejecutemos en el Main ya que gestionará el método anterior y el key logger (capta-teclas) y nos devolverá
                     (self.__manos) que nos servirá para saber si doblamos mano o no. '''


#----------------  DEF DISPLAY 2 MANOS --- CLASS DISPLAYS ---------------------------------------------------------------------------------------------------------------------------------------------

    def display_2manos (self):
    
      
        self._lista_2manos [self._posx][self._posy] = ' ◄ '
        
        
        print('''
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
            ♦   TE HAN TOCADO 2 CARTAS IGUALES QUIERES CONSERVARLAS Y SEGUIR O JUEGAS A 2 MANOS Y DOBLAS APUESTA          ♦ 
            ♣                                                                                                             ♣ 
            ♠                                                                                                             ♠
            ♥                                            █▀▀ █░░ ░▀░ █▀▀▀ █▀▀                                             ♥
            ♦                                            █▀▀ █░░ ▀█▀ █░▀█ █▀▀                                             ♦ 
            ♣                                            ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀                                             ♣
            ♠                                                                                                             ♠           
            ♥                                                                                                             ♥ 
            ♦                                                                                                             ♦
            ♣                                    ╔═════════════╗           ╔════════════╗                                 ♣ 
            ♠                                    ║ DOBLAR MANO ║  '''+self._lista_2manos[0][0]+'''      ║ SEGUIR ASI ║  '''+self._lista_2manos[0][1]+'''                            ♠
            ♥                                    ╚═════════════╝           ╚════════════╝                                 ♥
            ♦                                                                                                             ♦                                                     
            ♣                                ¿¿ QUIERS JUGAR CON 2 MANOS O CONTINUAR CON UNA ??                           ♣
            ♠                                                                                                             ♠                                                                  
            ♠                                                                                                             ♠                                                                                                       
            ♦                                                                                                             ♦
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥  ''')

#----------------  DEF 2 MANOS ACCIONES --- CLASS DISPLAYS ---------------------------------------------------------------------------------------------------------------------------------------------

    def manos_bj (self):
       
        def key_recorder(key):              
         
            self._key2 = str(key)
            l.stop( )

        self.__manos = 1
        self.__fin_2manos = "X"

        while self.__fin_2manos == "X":
            
            self.juego ( )
            self.display_2manos( )

            with Listener(on_press=key_recorder) as l: 
                l.join( )
                
            self.key_actions (self._lista_2manos,5) 

            clear ()

        return self.__manos


















# O O O O O O O O O O O O O O O O O O   CLASS DISPLAYS    O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O 

# X X X X X X X X X X X X X X X X X X   ELECCIÓN - Pedir,Plantar,Doblar...   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

    ''' En esta parte (eleccion pedir plantar... ) tendremos un método pequeño (titulo_puntos) que printeará un titulo, tenemos otro método ( display_bj_options )  que  que será la parte 
                'visual' , nos mostrará las distintas casillas con sus correspondientes opciones que seleccionaremos desplazando ' ◄ ' por las casillas y seleccionaremos con 'enter'.   
         Por último tenemos el método (actions_options) , este será el único que ejecutemos en el Main ya que gestionará los dos métodos anteriores yl el key logger (capta-teclas) y nos devolverá
                (self._resultado_opciones) que será la opcción elegida según la cual luego efectuaremos distintas acciones (pedir,plantar etc..) '''
     
    def sep_line (self):
        print("♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ")


#----------------  DEF DISPLAY ELECCION --- CLASS DISPLAYS ----------------------------------------------------------------------------------------------------------------------------------------

    def display_bj_options (self):

        self._lista_opciones [self._posx] [self._posy] = ' ◄ '                                                                              
        
        print ('''                         APUESTA ==> '''+str(self._apuesta)+'''$

               ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
               ♦                                                                                                             ♦
               ♣        █▀█ █▀█ █▀▀ █ █▀█ █▄░█ █▀▀ █▀                                                                        ♣
               ♠        █▄█ █▀▀ █▄▄ █ █▄█ █░▀█ ██▄ ▄█                                                                        ♠
               ♥                                                                                                             ♥
               ♦                                                                                                             ♦
               ♣                              ╔═══════╗           ╔═════════╗                                                ♣      
               ♠                              ║ Pedir ║  '''+self._lista_opciones [0][0]+'''      ║ Plantar ║  '''+self._lista_opciones [0][1]+'''                                           ♠
               ♥                              ╚═══════╝           ╚═════════╝                                                ♥      
               ♦                                                                                                             ♦
               ♣                                      QUE QUIERES HACER?                                                     ♣
               ♠                                                                                                             ♠
               ♥                              ╔════════╗            ╔══════╗                                                 ♥
               ♦                              ║ Doblar ║  '''+self._lista_opciones [1][0]+'''       ║  AS  ║  '''+self._lista_opciones [1][1]+'''                                            ♦                            
               ♣                              ╚════════╝            ╚══════╝                                                 ♣
               ♠                                      (Solo si tienes AS)                                                    ♠
               ♥                                                                                                             ♥
               ♣                                                                                                             ♣
               ♠                                                                                                             ♠
               ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥                                    ''')
                                                                                                                                              
#----------------  DEF OPCIONES-JUEGO --- CLASS DISPLAYS ----------------------------------------------------------------------------------------------------------------------------------------

    def actions_options (self,dealer_points,player_points,player_hand,dealer_hand):
                                                                                     
        def key_recorder(key):                   
    
            self._key2 = str(key)
            l.stop ()
        
        self._fin_op = "X"
        while self._fin_op == "X":  
            

            # NOS MUESTRA LAS CARTAS Y SUS PUNTOS
            
            self.juego ()
            
            self.tablero(dealer_points,player_points,player_hand,dealer_hand)

            # self.print_hand (dealer_hand)
            # print (" Puntos Dealer => ",dealer_points)
            # print (" Tus Puntos    => ",player_points)
            # self.print_hand (player_hand)
            
            # NOS MUESTRA EL MENÚ

            print ("")
        
            self.display_bj_options ( )
        
            with Listener(on_press = key_recorder) as l:  #--Esto es del listener (capturar teclas)
                l.join ( )
    
            self.key_actions (self._lista_opciones,2)

            clear ()

        self._lista_opciones= [['   ','   '],['   ','   ']]
        return self._resultado_opciones

















# O O O O O O O O O O O O O O O O O O   CLASS DISPLAYS    O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O 

# X X X X X X X X X X X X X X X X X X   GESTION AS_CARD   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

    ''' En esta parte ( GESTION AS_CARD) tendremos un método  (display_as) que será la parte 'visual' , nos mostrará las distintas casillas con sus correspondientes opciones que seleccionaremos desplazando
                     ' ◄ ' por las casillas y seleccionaremos con 'enter'.  
        Por último tenemos el método (as_points) , este será el único que ejecutemos en el Main ya que gestionará el método anterior y el key logger (capta-teclas) y nos devolverá
                     (self.__valor_as) que nos servirá para saber la puntuación de cada mano en función del valor elegido para nuestro 'as' '''

#----------------  DEF DISPLAY AS --- CLASS DISPLAYS ----------------------------------------------------------------------------------------------------------------------------------------

    def display_as (self):
                                                                                                   
        self._lista_as [self._posx][self._posy] = ' ◄ '       

        print(''' 
                    VALOR ACTUAL =  '''+str(self._valor_as)+'''


            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
            ♦                                                                                                             ♦ 
            ♣                                                                                                             ♣
            ♠                                                                                                             ♠
            ♥                            █▀▀ █░░ ░▀░ █▀▀▀ █▀▀ 　 ▄█░ 　 ▀█░█▀ █▀▀█ █░░ █▀▀█ █▀▀█                          ♥
            ♦                            █▀▀ █░░ ▀█▀ █░▀█ █▀▀ 　 ░█░ 　 ░█▄█░ █▄▄█ █░░ █░░█ █▄▄▀                          ♦
            ♣                            ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ 　 ▄█▄ 　 ░░▀░░ ▀░░▀ ▀▀▀ ▀▀▀▀ ▀░▀▀                          ♣
            ♠                                                                                                             ♠
            ♥                                                                                                             ♥ 
            ♦                                    ╔═══════════╗       ╔════════════╗                                       ♦
            ♣                                    ║ valor = 1 ║  '''+self._lista_as [0][0]+'''  ║ valor = 11 ║  '''+self._lista_as [0][1]+'''                                 ♣              
            ♠                                    ╚═══════════╝       ╚════════════╝                                       ♠
            ♥                                                                                                             ♥
            ♦                                                                                                             ♦
            ♣                        █▀▀█ █▀▀█ █▀▀█ █▀▀█ 　 ▀▀█▀▀ █░░█ 　 █▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀█                        ♣
            ♠                        █░░█ █▄▄█ █▄▄▀ █▄▄█ 　 ░░█░░ █░░█ 　 █░░ █▄▄█ █▄▄▀ ░░█░░ █▄▄█                        ♠
            ♥                        █▀▀▀ ▀░░▀ ▀░▀▀ ▀░░▀ 　 ░░▀░░ ░▀▀▀ 　 ▀▀▀ ▀░░▀ ▀░▀▀ ░░▀░░ ▀░░▀                        ♥ 
            ♦                                                                                                             ♦
            ♣                                                                                                             ♣
            ♠                                                                                                             ♠
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
                                        ''')
                              

#----------------  DEF PUNTOS_AS --- CLASS DISPLAYS ----------------------------------------------------------------------------------------------------------------------------------------

    def as_points (self):
        
        self._posx , self._posy = 0 , 0

        def key_recorder(key):              
        
            self._key2 = str(key)                                                                                                  
            l.stop()

        while self._fin_as_election == "X":
            
            self.juego()
            self.display_as ()      

            with Listener(on_press=key_recorder) as l:  
                l.join()
                
            self.key_actions (self._lista_as,4) 

            clear ()
        
        print (" Ahora el valor de tu carta es : ", self._valor_as )
            
        self._posx, self._posy = 0,0
        self._lista_as = [['   ','   ']] 
        self._fin_as_election = "X"
        
        return self._valor_as
        











# O O O O O O O O O O O O O O O O O O   CLASS DISPLAYS    O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O 

# X X X X X X X X X X X X X X X X X X   CONTINUE   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

    ''' En esta parte (  CONTINUE ) tendremos un método  (display_continue) que será la parte 'visual' , nos mostrará las distintas casillas con sus correspondientes opciones que seleccionaremos desplazando
                     ' ◄ ' por las casillas y seleccionaremos con 'enter'.  
        Por último tenemos el método (continue_bj) , este será el único que ejecutemos en el Main ya que gestionará el método anterior y el key logger (capta-teclas) y nos devolverá
                     (return self._continuar) de cuyo valor depende que volvamos a jugar una ronda o salgamos al menú de juegos , ya que este método se ejecuta en último lugar para resetear las variables
                      necesarias '''


#----------------  DEF DISPLAY_CONTINUE --- CLASS DISPLAYS ----------------------------------------------------------------------------------------------------------------------------------------


    def display_continue (self,fichas):

        self._lista_continue [self._posx][self._posy] = ' ◄ '
        print (" ")
        print('''



                ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥  
                ♦                                                                                                             ♦
                ♣                                                                                                             ♣
                ♠                            █▀▀ █▀▀█ █▀▀▄ ▀▀█▀▀ ░▀░ █▀▀▄ █░░█ █▀▀ 　 ▀█ ▀█                                   ♠
                ♥                            █░░ █░░█ █░░█ ░░█░░ ▀█▀ █░░█ █░░█ █▀▀ 　 █▀ █▀                                   ♥
                ♥                            ▀▀▀ ▀▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀░░▀ ░▀▀▀ ▀▀▀ 　 ▄░ ▄░                                   ♣                                 
                ♣                                                                                                             ♠
                ♠                                                                                                             ♥ 
                ♥                                                                                                             ♦ 
                ♦                                                                                                             ♣ 
                ♣                                                                                                             ♠
                ♠                                ╔═══════════╗           ╔═════════╗                                          ♥
                ♥                                ║ CONTINUAR ║  '''+self._lista_continue [0][0]+'''      ║  SALIR  ║  '''+self._lista_continue [0][1]+'''                                     ♦
                ♦                                ╚═══════════╝           ╚═════════╝                                          ♣
                ♣                                                                                                             ♠
                ♠                                                                                                             ♥
                ♥                               TE QUEDAN '''+str(fichas)+''' FICHAS                                                          ♦
                ♦                                                                                                             ♣
                ♣                                                                                                             ♠
                ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥                                    
        ''')


#----------------  DEF CONTINUE_BJ --- CLASS DISPLAYS ----------------------------------------------------------------------------------------------------------------------------------------


    def continue_bj (self,fichas,apuesta):

        self._posx , self._posy = 0 , 0

        def key_recorder (key):              
    
            self._key2 = str(key)
            l.stop()

        self._fin_continue = "X"
        while self._fin_continue == "X":
            
            self.juego ()
            self.display_continue (fichas)
            
            with Listener(on_press=key_recorder) as l: 
                l.join()
                
            self.key_actions (self._lista_continue,3)

            clear ( )

        
        self._apuesta , self._key2 ,  self._posx ,  self._posy , self._resultado_opciones ,  self._fin_op = 0 , 0 , 0 , 0 , 0 , 0
      
        self._fin_as_election , self._fin_continue , self._fin_apuesta = "X" , "X" , "X"
    
        self._lista_as= [['   ','   ']] 
        self._lista_continue= [['   ','   ']]
        self._lista_2manos= [['   ','   ']]
        self._lista_opciones= [['   ','   '],['   ','   ']]
        self._lista_apuesta = [ ['   ','   '],['   ','   '],['   ','   '] ] 

        self._valor_as = 11
        self._fichas = fichas

        return self._continuar 














# O O O O O O O O O O O O O O O O O O   CLASS DISPLAYS    O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O 

# X X X X X X X X X X X X X X X X X X  TABLERO Y PRINT_HAND   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

    def tablero (self,dealer_points,player_points,player_hand,dealer_hand):
        margen=50
        self.print_hand (dealer_hand)
        print ('\n\n ',' '*margen ," PUNTOS DEALER => ",dealer_points)
        print ('\n',' '*margen ,"  TUS PUNTOS    => ",player_points,)
        self.print_hand (player_hand)




    def print_hand ( self , X_Hand):

        dicc_palo = { "corazones":"║♥    ║","picas":"║♠    ║","trebol":"║♣    ║","diamantes":"║♦    ║" }
        dicc_palo2 = { "corazones":"║    ♥║","picas":"║    ♠║","trebol":"║    ♣║","diamantes":"║    ♦║" }
        dicc_card = { 1:"║  A  ║",2:"║  2  ║",3:"║  3  ║",4:"║  4  ║",5:"║  5  ║",6:"║  6  ║",7:"║  7  ║",8:"║  8  ║",9:"║  9  ║",10:"║  10 ║",11:"║  J  ║",12:"║  Q  ║",13:"║  k  ║" }

        num_cards = len (X_Hand )
        space =2
        separa= 49-num_cards

        print('\n\n               ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥\n\n',' '*separa,end=' ')
       
        for i in range ( num_cards ):

            print ( " "*space,"╔═════╗",end="" )
        print( '\n ',' '*separa,end='')

        for i in range ( num_cards ):

            print (" "*space, dicc_palo [ X_Hand [i][0] ],end="" ) 
        print( '\n ',' '*separa,end='')

        for i in range ( num_cards ):   

            print ( " "*space,dicc_card [ X_Hand [i][1] ],end="" )
        print( '\n ',' '*separa,end='')

        for i in range ( num_cards ):  

            print ( " "*space,dicc_palo2 [ X_Hand [i][0] ],end="" )
        print( '\n ',' '*separa,end='')

        for i in range ( num_cards ): 

            print (" "*space, "╚═════╝",end="" )
        
        print('\n\n               ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥')

    def juego (self):

        print (''' \n\n\n\n

                                ██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗    ░░░░░██╗░█████╗░░█████╗░██╗░░██╗
                                ██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝    ░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
                                ██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░    ░░░░░██║███████║██║░░╚═╝█████═╝░
                                ██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░    ██╗░░██║██╔══██║██║░░██╗██╔═██╗░
                                ██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗    ╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
                                ╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝    ░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ''')

           

     



