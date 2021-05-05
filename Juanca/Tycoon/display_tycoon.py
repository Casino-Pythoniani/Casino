from clases_tycoon import *
from pynput.keyboard import Listener

k = kasino()




class display_tycoon :

    def __init__(self):

        self.texto = "prueba"
        self.lista_tutorial=[['   ','   ']] 
        self._posx , self._posy , self.key_2 = 0,0,0
        self.lista_options = [['   ','   ','   ','   '] ]
        self.lista_opcion_compra = [['   ','   ','   ']] 
        self.lista_maquinas =  [['   ','   ','   ','   '],['   ','   ','   ','   '],['   ']  ]

    def reset (self):   

        self.lista_tutorial=[['   ','   ']] 
        self._posx , self._posy , self.key_2 = 0,0,0
        self.lista_options = [['   ','   ','   ','   '] ]
        self.lista_opcion_compra = [['   ','   ','   ']] 
        self.lista_maquinas =  [['   ','   ','   ','   '],['   ','   ','   ','   '],['   ','   ']  ]




    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """

    def key_actions (self,lista,x): 
       
        try:
        
            if self._key2 == 'Key.right' :      # Si pulsas derecha ...

                lista[self._posx][self._posy],lista[self._posx][self._posy+1] = lista[self._posx][self._posy+1],lista[self._posx][self._posy]
                self._posy = self._posy + 1

            elif self._key2 =='Key.left' :      # Si pulsas izquierda ...
                
                lista[self._posx][self._posy],lista[self._posx][self._posy-1] = lista[self._posx][self._posy-1],lista[self._posx][self._posy]                                             
                self._posy = self._posy - 1
            
            elif self._key2 =='Key.down' :      # Si pulsas abajo ...

                lista[self._posx][self._posy],lista[self._posx+1][self._posy] = lista[self._posx+1][self._posy],lista[self._posx][self._posy]
                self._posx = self._posx + 1
            
            elif self._key2 =='Key.up' :        # Si pulsas arriba ...

                lista[self._posx][self._posy],lista[self._posx-1][self._posy] = lista[self._posx-1][self._posy],lista[self._posx][self._posy]
                self._posx = self._posx - 1
            
            elif self._key2 =='Key.enter':       # Si pulsas enter ...
            #  Al pulsar enter tendremos diferentes opciones dependiendo del menú en el que estemos (apuesta,opciones etc..) y este vendrá dado como parámetro 

                if x == 1 : # Utilizamos este para el display TUTORIAL

                    if lista [0][0] == ' ◄ ':
                        self.respuesta_tutorial = "X"

                    elif lista [0][1] == ' ◄ ':
                        self.respuesta_tutorial = "V"

                    self.continuar = "V"

                elif x == 2: # Utilizamos este para el display GAME OPTIONS

                    if lista [0][0] == ' ◄ ':
                        self.respuesta_opciones = "continue"

                    elif lista [0][1] == ' ◄ ':
                        self.respuesta_opciones = "estado"

                    elif lista [0][2] == ' ◄ ':
                        self.respuesta_opciones = "comprar"

                    elif lista [0][3] == ' ◄ ':
                        self.respuesta_opciones = "ver"

                    self.continuar = "V"

                elif x == 3 : # Utilizamos este para el display OPCION COMPRA

                    if lista [0][0] == ' ◄ ':
                        self.respuesta_q_compra = "maquinas"

                    elif lista [0][1] == ' ◄ ':
                        self.respuesta_q_compra = "deco"

                    elif lista [0][2] == ' ◄ ':
                        self.respuesta_q_compra = "salir"    

                    self.continuar = "V"

                elif x == 4: # Utilizamos este para el display MAQUINAS

                    if lista [0][0] == ' ◄ ':
                        self.respuesta_maquinas = "tragaperras"

                    elif lista [0][1] == ' ◄ ':
                        self.respuesta_maquinas = "b_jack"

                    elif lista [0][2] == ' ◄ ':
                        self.respuesta_maquinas = "poker"

                    elif lista [0][3] == ' ◄ ':
                        self.respuesta_maquinas = "baccarat"

                    elif lista [1][0] == ' ◄ ':
                        self.respuesta_maquinas = "dados"

                    elif lista [1][1] == ' ◄ ':
                        self.respuesta_maquinas = "ruleta"

                    elif lista [1][2] == ' ◄ ':
                        self.respuesta_maquinas = "bingo"

                    elif lista [1][3] == ' ◄ ':
                        self.respuesta_maquinas = "carreras"

                    elif lista [2][0] == ' ◄ ':
                        self.respuesta_maquinas = "comprar"    

                    elif lista [2][0] == ' ◄ ':
                        self.respuesta_maquinas = "salir"        

                    self.continuar = "V"   

        except:         
            print("")

                   
        











    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """


    def display_tutorial (self): 
        
        self.lista_tutorial [self._posx][self._posy] = ' ◄ '

        print('''
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
            ♦                                                                                                             ♦
            ♣                                 ES LA PRIMERA VEZ QUE DIRIGES UN CASINO TYCOON ??                           ♦ 
            ♠                                                                                                             ♠                                
            ♥                                         QUIERES OMITIR EL TUTORIAL ??                                       ♥ 
            ♦                                                                                                             ♦
            ♣                                    ╔═════════════╗           ╔════════════╗                                 ♣ 
            ♠                                    ║    OMITIR   ║  '''+self.lista_tutorial[0][0]+'''      ║ ASISTENCIA ║  '''+self.lista_tutorial[0][1]+'''                            ♠
            ♥                                    ╚═════════════╝           ╚════════════╝                                 ♥
            ♦                                                                                                             ♦                                                     
            ♣                                    ¿¿ DESEAS ASISTENCIA DE NUESTRO ASESOR ??                                ♣
            ♠                                                                                                             ♠                                                                  
            ♠                                                                                                             ♠                                                                                                       
            ♦                                                                                                             ♦
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥  ''')


    def tutorial (self):
       
        def key_recorder(key):              
         
            self._key2 = str(key)
            l.stop( )
        
        self.respuesta_tutorial = "X"
        self.continuar = "X"

        while self.continuar == "X":
            
            k.titulo()
            self.display_tutorial()

            with Listener(on_press=key_recorder) as l: 
                l.join( )
                
            self.key_actions (self.lista_tutorial ,1) 
            clear ()
        
        self.reset()
        return self.respuesta_tutorial













    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """

    def display_game_options (self): 
        
        self.lista_options [self._posx][self._posy] = ' ◄ '

        print('''
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
            ♦                                                                                                             ♦
            ♣                       ELIGE UNA OPCIÓN..                                                                    ♦ 
            ♠                                                                                                             ♠                                
            ♥                              SIGUIENTE DIA PARA SEGUIR JUGANDO...                                           ♥ 
            ♦                                                                                                             ♣
            ♣                                       ESTADO CASINO PARA VER EL ESTADO DE LAS INSTALACIONES  ...            ♥ 
            ♦                                                                                                             ♦
            ♣     ╔═══════════════╗           ╔═══════════════╗           ╔═══════════════╗        ╔═══════════════╗      ♣ 
            ♠     ║ SIGUIENTE DIA ║  '''+self.lista_options[0][0]+'''      ║ ESTADO CASINO ║  '''+self.lista_options[0][1]+'''      ║   COMPRAR $   ║  '''+self.lista_options[0][2]+'''   ║   VER CASINO  ║  '''+self.lista_options[0][3]+''' ♠
            ♥     ╚═══════════════╝           ╚═══════════════╝           ╚═══════════════╝        ╚═══════════════╝      ♥
            ♦                                                                                                             ♦                                                     
            ♣                      ...   COMPRAR PARA ADQUIRIR NUEVAS MAQUINAS   ...                                      ♣
            ♠                                                                                                             ♠                                                                  
            ♠                                         O VER CASINO PARA PEGAR UN VISTAZO AL MAPA DE LAS INSTALACIONES     ♠                                                                                                       
            ♦                                                                                                             ♦
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥  ''')


    def game_options (self):
       
        def key_recorder(key):              
         
            self._key2 = str(key)
            l.stop( )
        
        self.respuesta_opciones = "X"
        self.continuar = "X"

        while self.continuar == "X":
            
            k.titulo()
            self.display_game_options()

            with Listener(on_press=key_recorder) as l: 
                l.join( )
                
            self.key_actions (self.lista_options,2) 
            clear ()
        
        self.reset()
        return self.respuesta_opciones













        """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """


    def display_opcion_compra (self): 
        
        self.lista_opcion_compra [self._posx][self._posy] = ' ◄ '

        print('''
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
            ♦                                                                                                             ♦
            ♣             PROVEEDOR DE MAQUINAS : Visita el catalogo de maquinas disponibles para tu casino               ♦ 
            ♠                                                                                                             ♠                                
            ♥     TIENDA DE DECORACION :  Plantas, estatuas.. todo lo imaginable para mejorar el aspecto de tu casino     ♥ 
            ♦                                                                                                             ♦
            ♣                 ╔═════════════╗           ╔════════════╗            ╔═════════════╗                         ♣ 
            ♠                 ║  MAQUINAS   ║  '''+self.lista_opcion_compra[0][0]+'''      ║ DECORACION ║  '''+self.lista_opcion_compra[0][1]+'''       ║    SALIR    ║  '''+self.lista_opcion_compra[0][2]+'''                    ♠
            ♥                 ╚═════════════╝           ╚════════════╝            ╚═════════════╝                         ♥
            ♦                                                                                                             ♦                                                     
            ♣                         o.. te has equivocado y quieres volver ?.. pulsa SALIR                              ♣
            ♠                                                                                                             ♠                                                                                                                                                                    
            ♦                                                                                                             ♦
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥  ''')


    def opciones_compra (self):
       
        def key_recorder(key):              
         
            self._key2 = str(key)
            l.stop( )
        
        self.respuesta_q_compra = "salir"
        self.continuar = "X"

        while self.continuar == "X":
            
            k.proveedores()
            self.display_opcion_compra()

            with Listener(on_press=key_recorder) as l: 
                l.join( )
                
            self.key_actions (self.lista_opcion_compra ,3) 
            clear ()
        
        self.reset()
        return self.respuesta_q_compra

















    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """


    def display_maquinas (self): 
        
        self.lista_maquinas [self._posx][self._posy] = ' ◄ '

        print('''
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
            ♦                                                                                                             ♦
            ♣         ╔═════════════╗          ╔═════════════╗           ╔═════════════╗         ╔═════════════╗          ♣ 
            ♠         ║ TRAGAPERRAS ║  '''+self.lista_maquinas [0][0]+'''     ║ BLACK JACK  ║  '''+self.lista_maquinas [0][1]+'''      ║    POKER    ║  '''+self.lista_maquinas [0][2]+'''    ║  BACCARAT   ║  '''+self.lista_maquinas [0][3]+'''     ♠
            ♥         ╚═════════════╝          ╚═════════════╝           ╚═════════════╝         ╚═════════════╝          ♥
            ♣         ╔═════════════╗          ╔═════════════╗           ╔═════════════╗         ╔═════════════╗          ♣ 
            ♠         ║    DADOS    ║  '''+self.lista_maquinas [1][0]+'''     ║   RULETA    ║  '''+self.lista_maquinas [1][1]+'''      ║    BINGO    ║  '''+self.lista_maquinas [1][2]+'''    ║  CARRERAS   ║  '''+self.lista_maquinas [1][3]+'''     ♠
            ♥         ╚═════════════╝          ╚═════════════╝           ╚═════════════╝         ╚═════════════╝          ♥                                                                                                                                                                       
            ♣                                                                                                             ♣
            ♠         ╔═════════════╗          ╔═════════════╗        ELIGE UNA MAQUINA                                   ♠                                                                                                                                                                    
            ♦         ║  COMPRAR $$ ║  '''+self.lista_maquinas [2][0]+'''     ║    SALIR    ║  '''+self.lista_maquinas [2][1]+'''              FIJATE BIEN EN LA DESCRIPCION !          ♥
            ♥         ╚═════════════╝          ╚═════════════╝                                    Y .. A COMPRAR !!       ♣
            ♣                                                                                                             ♦
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥       
                ''')
        print(self.texto)

    def maquinas (self):
       
        def key_recorder(key):              
         
            self._key2 = str(key)
            l.stop( )
        

        self.respuesta_maquinas = "¿"
        self.continuar = "X"

        while self.continuar == "X":
            
            k.titulo_maquinas()
            self.display_maquinas()

            with Listener(on_press=key_recorder) as l: 
                l.join( )
                
            self.key_actions (self.lista_maquinas,4) 
            clear ()
        
        self.reset()
        
        return self.respuesta_maquinas