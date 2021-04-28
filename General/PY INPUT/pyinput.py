from time import sleep
import os
clear = lambda: os.system('cls')
from pynput.keyboard import Listener



''' '''
class displays:
    
    def __init__ ( self ) :
        ''' Aqui tendremos que poner las listas que vamos a utilizar '''
        self.__lista_apuesta = [ ['   ','   '],['   ','   '],['   ','   '] ] 
        self.__lista_continue = [['   ','   ']]
        self.__lista_opciones = [['   ','   '],['   ','   ']]
        self.__apuesta , self.__key2 , self.__posx , self.__posy , self.__continuar , self.__fin_op ,  self.__resultado_opciones  = 0 , 0 , 0 , 0 , 0 , 0 , 0
        self.__fichas = 500
        self.continuar = 'False'
        
    def key_actions (self,lista,x): 
        ''' Key actions le dice a python lo que hacer con las teclas capturadas , en nuestro caso será desplazarse por una lista que estará printeada en un display
                para elegir opciones
            - Necesita como parámetro una lista que será según necesidad.. de 3 elementos si queremos tener 3 opciones en linea, de 2 x 2 etc.. segun queramos nosotros
                hacemos la lista y se la pasamos como parametro asi podremos reutilizarlo para varios displays
            - Necesita el parámetro x que utilizaremos para diferénciar entre distintos displays y por lo tanto distintas acciones. Mirar abajo en el codigo la diferencia entre elif x == a 2 o 3
                en un caso queremos que el resultado sea (pedir,plantar,doblar..) y en el otro si queremos continuar o no. Por lo que el parametro x nos ayuda a utilizar el mismo codigo para muchos displays.

                -- Con try y except hacemos que esto funcione con todas las listas que queramos y asi evitamos indexerror '''
        try:
        
            if self.__key2 == 'Key.right' :      # Si pulsas derecha ...

                lista[self.__posx][self.__posy],lista[self.__posx][self.__posy+1] = lista[self.__posx][self.__posy+1],lista[self.__posx][self.__posy]
                self.__posy = self.__posy + 1

            elif self.__key2 =='Key.left' :      # Si pulsas izquierda ...

                lista[self.__posx][self.__posy],lista[self.__posx][self.__posy-1] = lista[self.__posx][self.__posy-1],lista[self.__posx][self.__posy]                                             
                self.__posy = self.__posy - 1
            
            elif self.__key2 =='Key.down' :      # Si pulsas abajo ...

                lista[self.__posx][self.__posy],lista[self.__posx+1][self.__posy] = lista[self.__posx+1][self.__posy],lista[self.__posx][self.__posy]
                self.__posx = self.__posx + 1
            
            elif self.__key2 =='Key.up' :        # Si pulsas arriba ...

                lista[self.__posx][self.__posy],lista[self.__posx-1][self.__posy] = lista[self.__posx-1][self.__posy],lista[self.__posx][self.__posy]
                self.__posx = self.__posx - 1
            
            elif self.__key2 =='Key.enter':       # Si pulsas enter ...
            #  Al pulsar enter tendremos diferentes opciones dependiendo del menú en el que estemos (apuesta,opciones etc..) y este vendrá dado como parámetro 
                ''' Hasta aqui todos utilizamos lo mismo ya que la parte de arriba sirve para desplazarnos por la lista (cosa que todos necesitamos)
                        La parte de abajo ha de ser personal de cada uno ya que se adapta a lo que queremos que haga cada display '''
            
                if x == 1:  #  DISPLAY APUESTAS == Utilizaremos 1 para este display.............................................................................................................
                
                    if lista [0][0] == ' ◄ ': 

                        self.__fichas -= 5           
                        self.__apuesta += 5 
                    
                    elif lista [1][0] == ' ◄ ': 

                        self.__fichas -= 25           
                        self.__apuesta += 25
                    
                    elif lista [2][0] == ' ◄ ':

                        self.__fichas += self.__apuesta
                        self.__apuesta = 0
                    
                    elif lista [0][1] == ' ◄ ':  
                                                                                                         
                        self.__fichas -= 10
                        self.__apuesta += 10
                    
                    elif lista [1][1] == ' ◄ ':

                        self.__fichas -= 100
                        self.__apuesta += 100
                    
                    elif lista [2][1] == ' ◄ ':
                    
                        if self.__apuesta >= 5:
                            self.__fin_apuesta = "V" 
                            self.__posx,self.__posy = 0,0
                        
                        else:
                            print ("   No has realizado ninguna apuesta ")
                           
                        
                elif x == 2:  # DISPLAY OPCCIONES JUEGO ==> Utilizaremos el 2 para este display .....................................................................................................       
 
                    if lista [0][0] == ' ◄ ':
                        self.__resultado_opciones = 'pedir'

                    elif lista [0][1] == ' ◄ ':
                        self.__resultado_opciones = 'plantar' 
                    
                    elif lista [1][0] == ' ◄ ':
                        self.__resultado_opciones ='doblar'

                    elif lista [1][1] ==' ◄ ':
                        self.__resultado_opciones = 'as'
                
                    self.__fin_op ="V"         



                elif x == 3: # DISPLAY CONTINUAR ==> Utilizaremos el 3 para este display   .........................................................................................................                                           
 
                    if lista [0][0] == ' ◄ ':
                        self.continuar = "True"

                    elif lista [0][1] == ' ◄ ':
                        self.continuar = "False"
                    
                    self.__fin_continue = "V"

   
        except:         
            print("")











    ''' En la parte de arriba tenemos lo que tienen que hacer las teclas, en la parte de abajo haremos el resto. Agruparemos el titulo titulo_apuesta_bj,y la lista con display que
        crearemos cada uno a nuestro gusto display_bj_apuesta y luego tenemos def actions_apuesta una funcion que cordinara todo ,el titulo, la tecla capturada, la respuesta para esa tecla '''





# O O O O O O O O O O O O O O O O O O   CLASS DISPLAYS    O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O 

# X X X X X X X X X X X X X X X X X X   APUESTAS - Display y Acciones   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

    ''' En esta parte (Apuestas) tendremos un método pequeño (display_bj_apuesta) que printeará un titulo y unas instrucciones para el menú de apuestas ,  otro método (display_bj_apuesta) que será la parte 
                'visual' , nos mostrará las distintas casillas con sus correspondientes opciones que seleccionaremos desplazando ' ◄ ' por las casillas y seleccionaremos con 'enter'.  
        Por último tenemos el método (actions_apuesta) , este será el único que ejecutemos en el Main ya que gestionará los dos métodos anteriores yl el key logger (capta-teclas) y nos devolverá
                (apuesta,fichas) la apuesta realizada y las fichas restantes. '''

    def titulo_apuesta_bj (self) :

         print ( """

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

        self.__lista_apuesta [self.__posx][self.__posy] = ' ◄ '

        print('''
        ╔══════╗       ╔══════╗
        ║  5$  ║ '''+self.__lista_apuesta [0][0]+'''   ║  10$ ║ '''+self.__lista_apuesta [0][1]+'''
        ╚══════╝       ╚══════╝
                                                APOSTADO == '''+str(self.__apuesta)+'''
        ╔══════╗       ╔══════╗
        ║  25$ ║ '''+self.__lista_apuesta [1][0]+'''   ║ 100$ ║ '''+self.__lista_apuesta [1][1]+'''
        ╚══════╝       ╚══════╝
                                                FICHAS RESTANTES == '''+str(self.__fichas)+'''                                   
         ANULAR  '''+self.__lista_apuesta [2][0]+'''   APOSTAR  '''+self.__lista_apuesta [2][1]+'''

        ''')

#----------------  DEF ACTIONS APUESTA --- CLASS DISPLAYS ---------------------------------------------------------------------------------------------------------------------------------------------

    def actions_apuesta (self):
        ''' Este metodo gestiona todo: ha de seguir esta estructura para que funcione, key recorder ha de estar aqui puesta..no cambiar'''
        def key_recorder (key):                
      
            self.__key2 = str(key)
            l.stop( )

        self.__fin_apuesta = 'X'
        while self.__fin_apuesta == 'X':
            ''' LO REALMENTE IMPORTANTE ES ESTO : Entramos en un bucle donde ponemos tecla, la captura , realizamos accion segun la tecla capturada
                    y volvemos a poner una tecla que realizara otra accion... asi hasta que mediante la tecla que queramos indiquemos que la accion sea cerrar este bucle.
                Con esto podemos hacer todo.. x ej aqui al pulsar direcciones la accion correspondiente es movernos por el display diseñado previamente , al pulsar enter encima de cierto elemento
                subiremos la apuesta o la reiniciaremos, y al pulsar enter encima del elemento adecuado terminamos apuesta y cerramos este bucle'''

            self.titulo_apuesta_bj   ( ) 
            self.display_bj_apuesta ( ) 

            with Listener(on_press = key_recorder) as l:  
                l.join( )
            
            self.key_actions (self.__lista_apuesta,1) 

            clear ()
        





















    ''' Esto es otro ejemplo, funciona igual que el bloque de arriba (siempre es asi) un titulo si queremos un display con lista insertada obligado y la funcion coordinadora
    que contiene def key_recorder y gestiona las elecciones con ayuda de 1 bucle

    En este caso tendremos solo 2 opciones , con las teclas nos moveremos por estas y segun donde pulsemos enter se realizaran distintas acciones '''


# O O O O O O O O O O O O O O O O O O   CLASS DISPLAYS    O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O 

# X X X X X X X X X X X X X X X X X X   CONTINUE   X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

    ''' En esta parte (  CONTINUE ) tendremos un método  (display_continue) que será la parte 'visual' , nos mostrará las distintas casillas con sus correspondientes opciones que seleccionaremos desplazando
                     ' ◄ ' por las casillas y seleccionaremos con 'enter'.  
        Por último tenemos el método (continue_bj) , este será el único que ejecutemos en el Main ya que gestionará el método anterior y el key logger (capta-teclas) y nos devolverá
                     (return self.__continuar) de cuyo valor depende que volvamos a jugar una ronda o salgamos al menú de juegos , ya que este método se ejecuta en último lugar para resetear las variables
                      necesarias '''


#----------------  DEF DISPLAY_CONTINUE --- CLASS DISPLAYS ----------------------------------------------------------------------------------------------------------------------------------------


    def display_continue (self):

        clear ()
        self.__lista_continue [self.__posx][self.__posy] = ' ◄ '
        print (" ")
        print('''


        █▀▀ █▀▀█ █▀▀▄ ▀▀█▀▀ ░▀░ █▀▀▄ █░░█ █▀▀ 　 ▀█ ▀█ 
        █░░ █░░█ █░░█ ░░█░░ ▀█▀ █░░█ █░░█ █▀▀ 　 █▀ █▀ 
        ▀▀▀ ▀▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀░░▀ ░▀▀▀ ▀▀▀ 　 ▄░ ▄░



            ╔═══════════╗           ╔═════════╗         
            ║ CONTINUAR ║  '''+self.__lista_continue [0][0]+'''      ║  SALIR  ║  '''+self.__lista_continue [0][1]+'''
            ╚═══════════╝           ╚═════════╝ 


                TE QUEDAN 0 FICHAS .. a la calle
        ''')



#----------------  DEF CONTINUE_BJ --- CLASS DISPLAYS ----------------------------------------------------------------------------------------------------------------------------------------


    def continue_bj (self):

        self.__posx , self.__posy = 0 , 0

        def key_recorder (key):              
    
            self.__key2 = str(key)
            l.stop()

        self.__fin_continue = "X"
        while self.__fin_continue == "X":

            self.display_continue ()
            
            with Listener(on_press=key_recorder) as l: 
                l.join()
                
            self.key_actions (self.__lista_continue,3)

            clear ( )

        
        self.__apuesta , self.__key2 ,  self.__posx ,  self.__posy , self.__resultado_opciones ,  self.__fin_op = 0 , 0 , 0 , 0 , 0 , 0
      
        self.__fin_as_election , self.__fin_continue , self.__fin_apuesta = "X" , "X" , "X"
    
        
        self.__lista_continue= [['   ','   ']]
        self.__lista_apuesta = [ ['   ','   '],['   ','   '],['   ','   '] ] 

        return self.continuar







''' Ejemplo de los menús , el de apuesta y el de continuar, siguiendo los pasos de arriba y cambiando solo la lista , el display y ciertas acciones al pulsar teclas
cada uno puede hacer sus menús'''

display = displays ()

while True:
    display.actions_apuesta()
    display.continue_bj()
    if display.continuar == 'False':
        break








    
