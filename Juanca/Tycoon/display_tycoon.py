
""" display_tycoon 
IMPORTAMOS: Playsound para reproducir sonidos y sleep para producir -pausas- controladas
 en el programa.
 Creamos los objetos K y O para disponer facilmente de algunas variables estaticas .  """

from random import randrange
from clases_tycoon import *
from pynput.keyboard import Listener
from playsound import playsound
from time import sleep
import os
k = kasino()
o = objetos()

click = 'click.mp3'
click2="bambu.mp3"
donkey= "donkey.mp3"
cancelar = "fallo.mp3"
aceptar="bros vida.mp3"
adios= "adios.mp3"
yuju = "homer.mp3"
aleluya = "aleluya.mp3"
pop="pop.mp3"
here="here.mp3"
clear = lambda: os.system('cls')
""" O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

"""    CLASE DISPLAY TYCOON                                                                                                                                                  CLASE DISPLAY TYCOON    """ 

""" O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""



class display_tycoon :

    """ Esta clase la utilizamos para los displays, todos los displays tienen una estructura similar
donde tenemos el metodo que aporta la clase grafica y el metodo controlador. La parte grafica es lo que 
printeamos y el controlador gestiona todo , es decir printea lo grafico, detecta el movimiento y actua
correspondientemente segun la posicion en la que estemos y la tecla pulsada  """


    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O       INIT   """ 


    def __init__(self):

        self.ganancias="0"
        self.lista_configuracion = [["   ","   "],["   ","   "]]
        self.lista_instalar = [["   ","   "]]
        self.lista_display_decoracion =[["   ","   ","   ","   "],["   ","   ","   ","   "],["   ","   ","   ","   "],["   ","   "]]
        self.lista_estado = [["   "]]
        self.lista_ver_mapa = [["   "]]
        self.lista_options = [['   ','   ','   ','   '] ]
        self.lista_opcion_informe = [['   ','   ','   ']] 
        self.lista_opcion_compra = [['   ','   ','   ']] 
        self.lista_maquinas =  [['   ','   ','   ','   '],['   ','   ','   ','   '],['   ','   ']  ]
        self.deco = ""
        self.primera="V"
        self.respuesta_maquinas = "¿"
        self.compra="X"  
        self.texto = "\n\t\t PULSA ENTER EN CUALQUIER JUEGO , MIRA LA DESCRIPCCION Y CUANDO ESTES SEGURO PULSA COMPRAR"
        self.texto2= "\n\t\t PULSA ENTER EN CUALQUIER MEJORA , MIRA LA DESCRIPCCION Y CUANDO ESTES SEGURO PULSA COMPRAR"
        self.figura = ""
        self._posx , self._posy , self.key_2 = 0,0,0
        

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O         FAMA    """ 


    def reset (self):  

        """ Usamos este metodo para recuperar facilmente la posicion de aquellas variables que asi lo necesiten, como x ej las listas que indican
        posicion en displays y asi al volver a ese display empezar en la casilla de inicio  """

        self.lista_configuracion = [["   ","   "],["   ","   "]]
        self.lista_instalar = [["   ","   "]]
        self.lista_display_decoracion =[["   ","   ","   ","   "],["   ","   ","   ","   "],["   ","   ","   ","   "],["   ","   "]]
        self.lista_ver_mapa = [["   "]]
        self.lista_estado = [["   "]]
        self.lista_options = [['   ','   ','   ','   '] ]
        self.lista_opcion_informe = [['   ','   ','   ']] 
        self.lista_opcion_compra = [['   ','   ','   ']] 
        self.lista_maquinas =  [['   ','   ','   ','   '],['   ','   ','   ','   '],['   ','   ']  ]
        self.primera="V"
        self.texto = "\n\t\t PULSA ENTER EN CUALQUIER JUEGO , MIRA LA DESCRIPCCION Y CUANDO ESTES SEGURO PULSA COMPRAR"  
        self.texto2= "\n\t\t PULSA ENTER EN CUALQUIER MEJORA , MIRA LA DESCRIPCCION Y CUANDO ESTES SEGURO PULSA COMPRAR"
        self._posx , self._posy , self.key_2 = 0,0,0
        




    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O         KEY ACTIONS    """ 

    def key_actions (self,lista,x): 
        print (type(self._key2))
        sleep (2) # ----------------------------------------------------------------------------------------------------------------------------------------------------------------
        """ Este metodo cogera la tecla pulsada y realizara distintas acciones dependiendo de donde la pulsemos, segun en que lista y en que parte,recibira 2 parametros , la lista por la que nos desplazaremos 
        y x que representara el menu en el que estamos ya que pulsar algo en la casilla [0][0] cambia dependiendo de donde estemos
        Metodo largo, hasta 340 mas o menos """
       
        try:
             
            if self._key2 == 'Key.right' :      # Si pulsas derecha ...
              

                playsound(click,False)

                if x == 5 and self._posy == len(lista[1])-2:
                    pass

                elif lista[self._posx][self._posy+1] == "   ":

                    lista[self._posx][self._posy],lista[self._posx][self._posy+1] = lista[self._posx][self._posy+1],lista[self._posx][self._posy]
                    self._posy = self._posy + 1

            elif self._key2 =='Key.left' :      # Si pulsas izquierda ...

                playsound(click,False)

                if x == 5 and self._posy == 1:
                    pass

                elif lista[self._posx][self._posy-1] == "   ":
                    lista[self._posx][self._posy],lista[self._posx][self._posy-1] = lista[self._posx][self._posy-1],lista[self._posx][self._posy]                                             
                    self._posy = self._posy - 1
            
            elif self._key2 =='Key.down' :      # Si pulsas abajo ...

                playsound(click,False)

                if x == 5 and self._posx ==len(lista)-2:
                    pass

                elif lista[self._posx+1][self._posy] == "   ":
                    
                    lista[self._posx][self._posy],lista[self._posx+1][self._posy] = lista[self._posx+1][self._posy],lista[self._posx][self._posy]
                    self._posx = self._posx + 1
            
            elif self._key2 =='Key.up' :        # Si pulsas arriba ...

                playsound(click,False)

                if x == 5 and self._posx ==1:
                    pass
                elif lista[self._posx-1][self._posy] == "   ":

                    lista[self._posx][self._posy],lista[self._posx-1][self._posy] = lista[self._posx-1][self._posy],lista[self._posx][self._posy]
                    self._posx = self._posx - 1
            
            elif self._key2 =='Key.enter':       # Si pulsas enter ...
                playsound(click2,False)
            #  Al pulsar enter tendremos diferentes opciones dependiendo del menú en el que estemos (apuesta,opciones etc..) y este vendrá dado como parámetro 

                """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O  KEY ACTIONS   X = 1  LIBRE    """ 

             

                """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O  KEY ACTIONS   X = 2  GAME OPTIONS  """ 

                if x == 2: # Utilizamos este para el display GAME OPTIONS

                    if lista [0][0] == ' ◄ ':
                        self.respuesta_opciones = "continue"

                    elif lista [0][1] == ' ◄ ':
                        self.respuesta_opciones = "estado"

                    elif lista [0][2] == ' ◄ ':
                        self.respuesta_opciones = "comprar"

                    elif lista [0][3] == ' ◄ ':
                        self.respuesta_opciones = "config"

                    self.continuar = "V"

                    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O  KEY ACTIONS   X = 3  OPCION COMPRA    """ 

                elif x == 3 : # Utilizamos este para el display OPCION COMPRA

                    if lista [0][0] == ' ◄ ':
                        self.respuesta_q_compra = "maquinas"

                    elif lista [0][1] == ' ◄ ':
                        self.respuesta_q_compra = "deco"

                    elif lista [0][2] == ' ◄ ':
                        self.respuesta_q_compra = "salir"    

                    self.continuar = "V"

                    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O   KEY ACTIONS   X = 4   MAQUINAS  """ 

                elif x == 4: # Utilizamos este para el display MAQUINAS

                    if lista [0][0] == ' ◄ ':
                        self.texto =  "\t\t\t\t TRAGAPERRAS  \n\n\t \t   PRECIO :"+str(k.catalogo["tragaperras"])+" $         BENEFICIOS MAX: "+str(k.beneficios_maquinas["tragaperras"])+" $ / dia  \n\n\t\t     Nuestra estupenda maquina tragaperras ... un clasico de toda la vida ,  una opcion de compra segura \n\n\t\t con rapidos beneficios a un coste moderado. Vamos es una apuesta segura !! "
                        self.respuesta_maquinas = "tragaperras"

                    elif lista [0][1] == ' ◄ ':
                        self.texto =  "\t\t\t\t  BLACK JACK  \n\n\t \t   PRECIO : "+str(k.catalogo["b_jack"])+" $         BENEFICIOS MAX: "+str(k.beneficios_maquinas["b_jack"])+" $ / dia  \n\n\t\t     Una estupenda mesa de Black Jack fabricada con los mejores materiales del mercado, seguro que tu casino  \n\n\t\t se llenará de gente y tus beneficios aumentarán.   "
                        self.respuesta_maquinas = "b_jack"

                    elif lista [0][2] == ' ◄ ':
                        self.texto = "\t\t\t\t POKER \n\n\t \t   PRECIO : "+str(k.catalogo["poker"])+" $         BENEFICIOS MAX: "+str(k.beneficios_maquinas["poker"])+" $ / dia  \n\n\t\t     El poker ... es ir a lo seguro, nuestra pieza mas cara pero sin duda vale su precio y mucho mas, no solo \n\n\t\t te traerá beneficios sino que también atraerá mas gente a tu casino ya que..   \n\n\t\t a quien no le gusta una buena partida de poker ? "
                        self.respuesta_maquinas = "poker"

                    elif lista [0][3] == ' ◄ ':
                        self.texto =  "\t\t\t\t BACCARAT \n\n\t \t   PRECIO : "+str(k.catalogo["baccarat"])+" $         BENEFICIOS MAX: "+str(k.beneficios_maquinas["baccarat"])+" $ / dia  \n\n\t\t     Un juego d cartas no tan conocido como el resto pero.. en la variedad esta el gusto no ? y no es solo una  \n\n\t\t frase cutre sino que recuerda que mientras mas variedad exista en tu   \n\n\t\t casino, mas gente vendrá a este."
                        self.respuesta_maquinas = "baccarat"

                    elif lista [1][0] == ' ◄ ':
                        self.texto =  "\t\t\t\t DADOS \n\n\t \t   PRECIO : "+str(k.catalogo["dados"])+" $         BENEFICIOS MAX: "+str(k.beneficios_maquinas["dados"])+" $ / dia  \n\n\t\t    Otro clasico.. apuestas rapidas .. dinero rapido y.. para ti !! una de estas no puede faltar en tu casino, \n\n\t\t además las calidades son las mejor del mercado a un precio excelente.  \n\n\t\t "
                        self.respuesta_maquinas = "dados"

                    elif lista [1][1] == ' ◄ ':
                        self.texto =  "\t\t\t\t RULETA \n\n\t \t   PRECIO : "+str(k.catalogo["ruleta"])+" $         BENEFICIOS MAX: "+str(k.beneficios_maquinas["ruleta"])+" $ / dia  \n\n\t\t     Aun no tienes una ruleta en tu casino ?? A que esperas para obtener este clasico indispensable para cualquier \n\n\t\t casino que se precie ?? y por ser hoy.. y por nuestra larga amistad  \n\n\t\t esta viene con un 20% de descuento incluido !"
                        self.respuesta_maquinas = "ruleta"

                    elif lista [1][2] == ' ◄ ':
                        self.texto =  "\t\t\t\t BINGO \n\n\t \t   PRECIO : "+str(k.catalogo["bingo"])+" $         BENEFICIOS MAX: "+str(k.beneficios_maquinas[ "bingo"])+" $ / dia  \n\n\t\t     Un bingo en tu casino , para que la gente pueda relajarse y perder su dinero mientras se toma algo.. \n\n\t\t con este set te entregamos todo lo necesario para que mañana mismo lo tengas  \n\n\t\t  funcionando en tu casino."
                        self.respuesta_maquinas = "bingo"

                    elif lista [1][3] == ' ◄ ':
                        self.texto =   "\t\t\t\t CARRERAS \n\n\t \t   PRECIO : "+str(k.catalogo["carreras"])+" $         BENEFICIOS MAX: "+str(k.beneficios_maquinas["carreras"])+" $ / dia  \n\n\t\t     lo necesario para que mañana mismo la gente pueda apostar por su caballo favorito.. y lo mas importante...   \n\n\t\t esto implicara beneficios para tu bolsillo."
                        self.respuesta_maquinas = "carreras"

                    elif lista [2][0] == ' ◄ ':
                        self.compra =  self.respuesta_maquinas
                        self.respuesta_maquinas = "comprar"
                        
                        

                    elif lista [2][1] == ' ◄ ':
                        self.respuesta_maquinas="salir"
                   
                    self.continuar = "V"  

                    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O  KEY ACTIONS   X = 5  CONSTRUCTOR    """  

                elif x == 5 : # utilizaremos este display para el menu  CONSTRUCTOR
                    
                    self.posiciones = [self._posx, self._posy]
                    lista[self._posx][self._posy] = "   "
                    self.continuar = "V"  
                    
                    self.mapa_cambiado=[]

                    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O KEY ACTIONS   X = 6   VER MAPA   """ 

                elif x == 6 : # utilizaremos este display para el menu VER MAPA

                    self.continuar = "V" 

                    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O        KEY ACTIONS   X = 7   DECORACION  """ 

                elif x == 7 :  # utilizaremos este numero para el display DECORACION

                    if lista [0][0] == ' ◄ ': 
                        self.texto2 = "\t\t ESTAS SON LAS PAREDES QUE VENIAN CON EL CASINO.. UN POCO CUTRES , SI.. PERO DE MOMENTO CUMPLEN SU \n\n\t\t FUNCIÓN , PERO SI HAS VENIDO AQUI ES PARA MEJORAR LO PRESENTE.. PEGA UN VISTAZO A NUESTRAS OTRAS PAREDES." 
                        self.respuesta_deco = "PAREDES-1"

                    elif lista [0][1] == ' ◄ ':
                        self.texto2 = "\t\t ESTAS PAREDES DARAN MAS ESTILO A TU CASINO ! NUESTROS EMPLEADOS PINTARAN TODAS LAS PAREDES Y SUELOS \n\n\t\t CON COLORES ELEGIDOS POR LOS MEJORES DISEÑADORES Y PINTURA DE LA MAS ALTA CALIDAD OTORGANDO A \n\n\t\t SU EDIFICIO DE UN ASPECTO RENOVADO Y MODERNO."
                        self.respuesta_deco = "PAREDES-2"

                    elif lista [0][2] == ' ◄ ':
                        self.texto2 = "\t\t SE NOTA EL BUEN GUSTO.. NUESTROS EMPLEADOS Y DISEÑADORES TRABAJARAN EN CONJUNTO PARA INSTALAR DIVERSOS \n\n\t\t ELEMENTOS DE DECORACION QUE HARAN QUE SUS CLIENTES TENGAN LA SENSACION  DE ESTAR EN UN RELAJADO\n\n\t\tBARRIO VENECIANO .. IDEAL PARA UN CASINO" 
                        self.respuesta_deco = "PAREDES-3"

                    elif lista [0][3] == ' ◄ ':
                        self.texto2 ="\t\t NUESTRO MEJOR PRODUCTO.. PINTURA PAN DE ORO , COMBINADA CON ROJO VINO E INCRUSTRACIONES DE MARMOL BLANCO\n\n\t\t DE LA MAS ALTA CALIDAD .. ESTO CONVERTIRA TU CASINO EN UNA AUTENTICA OBRA DE ARTE.. INMEJORABLE!!"  
                        self.respuesta_deco = "PAREDES-4"

                    elif lista [1][0] == ' ◄ ':
                        self.texto2 = "\t\t BUENO.. SUJETA A LA GENTE NO ? Y ES GRATIS.. EN VERDAD DEBERIAS PENSAR EN CAMBIARLO PRONTO PERO  \n\n\t\t ESTAS DE SUERTE TENEMOS UNA ESTUPENDA SELECCION , PEGA UN VISTAZO." 
                        self.respuesta_deco = "SUELO-1"

                    elif lista [1][1] == ' ◄ ':
                        self.texto2 = "\t\t LA VERDAD ES QUE PARA EL PRECIO QUE TIENE CUMPLE CONVENIENTEMENTE SU FUNCION ADEMAS DARA A TU  \n\n\t\t CASINO UN ASPECTO RENOVADO QUE ATRAERA A MUCHA MAS GENTE. ADEMAS TENEMOS LIBRE AL EQUIPO SE INSTALACION, \n\n\t\tPUEDE TENERLO INSTALADO EN 2 DIAS SI COMPRA AHORA." 
                        self.respuesta_deco = "SUELO-2"

                    elif lista [1][2] == ' ◄ ':
                        self.texto2 = "\t\t ESTAS BALDOSAS VALENCIANAS SON DE LO MEJOR DEL MERCADO , FABRICADAS DE MANERA ARTESANAL Y ADEMAS  \n\n\t\t SON PRODUCTO LOCAL. DARA AL CASINO UN TOQUE RUSTICO-CLASICO QUE AHORA ESTA DE MODA.. ESTE NUEVO ASPECTO\n\n\t\t SEGURO QUE ATRAE A MULTITUD DE GENTE " 
                        self.respuesta_deco = "SUELO-3"

                    elif lista [1][3] == ' ◄ ':
                        self.texto2 = "\t\t MARMOL BLANCO PULIDO DE LA MAS ALTA CALIDAD , SELECCIONADO CUIDADOSAMENTE PARA QUE COINCIDAN SUS  \n\n\t\t TRAZAS, NO ENCONTRARAS MEJOR PRODUCTO NI MEJOR ACABADO EN EL MERCADO, CON ESTO SITUARAS A TU CASINO\n\n\t\t A LA ALTURA DE LOS MEJORES ." 
                        self.respuesta_deco = "SUELO-4"

                    elif lista [2][0] == ' ◄ ':
                        self.texto2 = "\t\t ESTA REFORMA ES LA JUSTA QUE REALIZAMOS PARA ABRIR EL CASINO , CONTIENE MATERIALES Y ACABADOS  \n\n\t\t DE MUY BAJA CALIDAD, TODOS LOS DETALLES CUENTAN Y LA VERDAD ES QUE CISTERNAS QUE NO FUNCIONAN, LUCES \n\n\t\t FUNDIDAS Y ESE TIPO DE COSAS NO AYUDAN." 
                        self.respuesta_deco = "REF-1"

                    elif lista [2][1] == ' ◄ ':
                        self.texto2 = "\t\t SI NOS DAS EL VISTO BUENO MANDAREMOS A NUESTRO EQUIPO A REPARAR TODOS LOS DESPERFECTOS , AL  \n\n\t\t AJUSTAR EL PRESUPUESTO NO MEJORAREMOS NADA PERO DEJAREMOS TODO LO QUE HAY FUNCIONANDO, NO MAS LUCES FUNDIDAS\n\n\t\t NI GRIFOS ATASCADOS ." 
                        self.respuesta_deco = "REF-2"

                    elif lista [2][2] == ' ◄ ':
                        self.texto2 = "\t\t MEJORAREMOS TODOS LOS ELEMENTOS DE LAS INSTALACIONES, SIN IR A LAS MAS ALTAS CALIDADES RENOVAREMOS \n\n\t\t ENCHUFES,BATERES, LAMPARAS Y TODO TIPO DE ELEMENTOS.. ESTOS DETALLES SON PEQUEÑOS PERO UCHOS.. Y CUENTAN !" 
                        self.respuesta_deco = "REF-3"

                    elif lista [2][3] == ' ◄ ':
                        self.texto2 = "\t\t ELEMENTOS DE LA MAS ALTA CALIDAD .. LAMPARAS , BAÑOS , FALSO TECHO .. TODO DE DISEÑO Y CON LAS \n\n\t\t MAS ALTAS CALIDADES ESTO SERA LA GUINDA DEL PASTEL, NOS COMPROMETEMOS QUE HASTA EL MAS MINIMO DETALLE \n\n\t\t SERA TRABAJADO, SERA IMPOSIBLE SACAR HASTA EL MAS MINIMO DEFECTO.  ." 
                        self.respuesta_deco = "REF-4"

                    elif lista [3][0] == ' ◄ ':
                        self.compra_deco =  self.respuesta_deco
                        self.respuesta_deco = "comprar"
                        self.continuar = "V"  
                        playsound(aleluya,False)

                    elif lista [3][1] == ' ◄ ':
                        self.texto2= "\n\t\t PULSA ENTER EN CUALQUIER MEJORA , MIRA LA DESCRIPCCION Y CUANDO ESTES SEGURO PULSA COMPRAR"
                        self.respuesta_deco = "salir"
                        self.continuar = "V" 
                        self.salir = "V" 

                        """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O   KEY ACTIONS   X = 8   CONFIRMA INSTALACION  """ 
                
                elif x == 8 :    # utilizaremos este numero para el display CONFIRMA INSTALACION
                    if lista [0][0] == ' ◄ ':
                        self.respuesta_confirma = "V"
                        playsound(aleluya,False)

                    elif lista [0][1] == ' ◄ ':
                        self.respuesta_confirma = "X"
                        playsound(cancelar)

                    self.continuar = "V"

                    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O   KEY ACTIONS   X = 9    OPCION COMPRA   """ 

                elif x == 9 : # Utilizamos este para el display OPCION COMPRA

                    if lista [0][0] == ' ◄ ':
                        self.respuesta_estado = "mapa"

                    elif lista [0][1] == ' ◄ ':
                        self.respuesta_estado = "informe"

                    elif lista [0][2] == ' ◄ ':
                        self.respuesta_estado = "salir"    
                        self.salir = "V"

                    self.continuar = "V"

                    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O   KEY ACTIONS   X = 10    CONFIGURACION   """ 

                elif x == 10: # Utilizamos este para el display CONFIGURACION

                    if lista [0][0] == ' ◄ ':
                        self.resultado_config = "guardar"

                    elif lista [0][1] == ' ◄ ':
                        self.resultado_config = "cargar"

                    elif lista [1][0] == ' ◄ ':
                        self.resultado_config = "exit"
                        sleep(1)
                        playsound(adios)

                    elif lista [1][1] == ' ◄ ':
                        self.resultado_config = "salir"
                    
                    self.continuar = "V"
        except:         
            print("")

   

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """    METODOS GAME OPTIONS                                           X -2                                                                                                      METODOS GAME OPTIONS    """ 

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """ Metodos en grupo, display_game_options() muestra la parte grafica e integra la lista para desplazarnos por el menu, game_options() es el metodo principal y gestiona
        la funcion integrada key_recorder() que captura la tecla pulsada y mediante key_actions() realiza las acciones correspondientes, se devuelve el resultado sobre que 
        opcion de juego escogemos """



    def display_game_options (self): 
        
        dinero = k.printea_money(kasino.dinero)
        self.lista_options [self._posx][self._posy] = ' ◄ '
        sem_pasada=k.printea_money(int(self.ganancias)*7)

        print('''
                         GANANCIAS SEMANA PASADA = '''+sem_pasada+'''                     SEMANA   🢂  '''+str(kasino.dia)+'''


                                                      $ DINERO  🢂  '''+dinero+''' $ 

            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
            ♦                                                                                                             ♦
            ♣                       ELIGE UNA OPCIÓN..                                                                    ♦ 
            ♠                                                                                                             ♠                                
            ♥                              SIGUIENTE SEMANA PARA PASAR 1 SEMANA Y RECAUDAR BENEFICIOS ...                 ♥ 
            ♦                                                                                                             ♣
            ♣                                       ESTADO CASINO PARA VER EL ESTADO DE LAS INSTALACIONES  ...            ♥ 
            ♦                                                                                                             ♦
            ♣     ╔═══════════════╗           ╔═══════════════╗           ╔═══════════════╗        ╔═══════════════╗      ♣ 
            ♠     ║   1 SEMANA +  ║  '''+self.lista_options[0][0]+'''      ║ ESTADO CASINO ║  '''+self.lista_options[0][1]+'''      ║   COMPRAR $   ║  '''+self.lista_options[0][2]+'''   ║ CONFIGURACION ║  '''+self.lista_options[0][3]+''' ♠
            ♥     ╚═══════════════╝           ╚═══════════════╝           ╚═══════════════╝        ╚═══════════════╝      ♥
            ♦                                                                                                             ♦                                                     
            ♣                      ...   COMPRAR PARA ADQUIRIR NUEVAS MAQUINAS   ...                                      ♣
            ♠                                                                                                             ♠                                                                  
            ♠                                         O CONFIGURACION PARA GUARDAR PARTIDA O ABANDONAR EL JUEGO           ♠                                                                                                       
            ♦                                                                                                             ♦
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥  ''')


    def game_options (self):

        self.reset()

        def key_recorder(key):              
            self._key2 = str(key)
            l.stop( )
            return self._key2
        
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





















    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """    METODOS OPCION COMPRA                                           X -3                                                                                               METODOS OPCION COMPRA     """ 

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """  Metodos en grupo, display_opcion_compra() muestra la parte grafica e integra la lista para desplazarnos por el menu, opciones_compra() es el metodo principal y gestiona
        la funcion integrada key_recorder() que captura la tecla pulsada y mediante key_actions() realiza las acciones correspondientes, se devuelve el resultado sobre que 
        si queremos ver maquinas o decoracion 
        Como se puede apreciar en el display de abajo estos metodos interactuan con metodos maquinas y metodos decoracion ya que segun la opcion seleccionada aqui
        nos desplazaremos a uno de esos menus. """



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
            ♦                                                                                                             ♦
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ''')


    def opciones_compra (self):
       
        def key_recorder(key):              
         
            self._key2 = str(key)
            l.join( )
        
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

    
    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """    METODOS COMPRAR MAQUINAS                                           X -4                                                                                         METODOS COMPRAR MAQUINAS       """ 

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """  Metodos en grupo, display_maquinas() muestra la parte grafica e integra la lista para desplazarnos por el menu, maquinas() es el metodo principal y gestiona
        la funcion integrada key_recorder() que captura la tecla pulsada y mediante key_actions() realiza las acciones correspondientes, En este caso la respuesta se gestiona desde
        aqui,en maquinas() si la respuesta es comprar maquina se gestionaran una serie de metodos para colocar el objeto. Seran explicados debajo de cada uno.

        Grupo de metodos grande + 8     Ya que METODOS COLOCA COSAS (el siguiente) es invocado desde aqui
        """


    def display_maquinas (self): 
        
        self.lista_maquinas [self._posx][self._posy] = ' ◄ '
        dinero = k.printea_money(kasino.dinero)
        print('''
                                            TU DINERO 🢂  '''+dinero+''' $

            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
            ♦                                                                                                             ♦
            ♣         ╔═════════════╗          ╔═════════════╗           ╔═════════════╗         ╔═════════════╗          ♣ 
            ♠         ║ TRAGAPERRAS ║  '''+self.lista_maquinas [0][0]+'''     ║ BLACK JACK  ║  '''+self.lista_maquinas [0][1]+'''      ║    POKER    ║  '''+self.lista_maquinas [0][2]+'''    ║  BACCARAT   ║  '''+self.lista_maquinas [0][3]+'''     ♠
            ♥         ╚═════════════╝          ╚═════════════╝           ╚═════════════╝         ╚═════════════╝          ♥
            ♦                                                                                                             ♦
            ♣         ╔═════════════╗          ╔═════════════╗           ╔═════════════╗         ╔═════════════╗          ♣ 
            ♠         ║    DADOS    ║  '''+self.lista_maquinas [1][0]+'''     ║   RULETA    ║  '''+self.lista_maquinas [1][1]+'''      ║    BINGO    ║  '''+self.lista_maquinas [1][2]+'''    ║  CARRERAS   ║  '''+self.lista_maquinas [1][3]+'''     ♠
            ♠         ╚═════════════╝          ╚═════════════╝           ╚═════════════╝         ╚═════════════╝          ♦
            ♥                                                                                                             ♥
            ♦         ╔═════════════╗          ╔═════════════╗                                                            ♦                                                                                         
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

        self.salir = "X"

        while self.salir == "X":

            self.continuar = "X"

            while self.continuar == "X":
                
                k.titulo_maquinas()
                self.display_maquinas()

                with Listener(on_press=key_recorder) as l: 
                    l.join( )
                    
                self.key_actions (self.lista_maquinas,4) 
                clear ()
     
            if self.respuesta_maquinas == "salir":
                self.salir="V"
           
            elif self.respuesta_maquinas == "comprar" and self.compra != "¿"  and self.compra != "comprar":

                self.coloca_cosas()
            




    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """    METODOS COLOCAR MAQUINAS                                           X -5                                                                                         METODOS COLOCAR MAQUINAS       """ 

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """ Estos metodos son invocados desde maquinas () en METODOS COMPRA MAQUINAS (arriba) , Es una agrupacion de metodos y coloca_cosas es el gestor de este grupo ,utilizara display_coloca_cosas(),
    medir_espacio(), clona_mapa() e instalar() para colocar la maquina elegida anteriormente en maquinas(),arriba, en el mapa del casino, tiene key_recorder() integrado y utiliza esta y key_action()
    para desplazarnos por el mapa 

    medir_espacio() mirara si la maquina elegida cabe en la posicion seleccionada, y dependiendo de eso nos dara permiso ono para instalar 
    clona_mapa() es un pequeño metodo para copiar lista de listas
    instalar() coloca la maquina en el mapa
    display_coloca_cosas Nos muestra el mapa y la esquina superior izquierda del objeto seleccionado , pudiendo desplazarla para seleccionar la posicion de instalacion """


    def display_coloca_cosas (self): 
        
        if self.primera == "V":
            self._posx,self._posy = 1,1
            kasino.mapa [self._posx][self._posy] = "╔══"
            self.primera = "X"
        else:
            kasino.mapa [self._posx][self._posy] = "╔══"

        k.titulo_constructor()
        for i in kasino.mapa:
            print("".join(i))
        for fila in o.entrega_lista_maquina(self.compra):
            print("\t"*2,"".join(fila))
        print("""\n\t\tBIENVENIDO AL CONSTRUCTOR !! Como puedes ver estas situando la esquina superior izquierda de tu maquina ,\n\n\t\t ten en cuenta las medidas que te entrega el fabricante para situarla en el lugar adecuado
        \n\t\t\ty cuando lo tengas claro pulsa enter""")

        print("""\n\n\t\t\t"""+self.compra.upper()+"""\t  ANCHO = """+str(len(o.entrega_lista_maquina(self.compra)))+"""\t ALTO = """+str(len(o.entrega_lista_maquina(self.compra)))+"""\tCALCULA BIEN TU ESPACIO \n""")
        
        print(self._posx,self._posy)


    def medir_espacio (self,casino,objeto,posx,posy):

        ancho = len (objeto[0])
        largo = len (objeto)
        self.permiso = "V"

        for i in range(largo+1):

            if self.permiso == "X":
                    break

            for z in range(ancho+1):

                control=str(posx+i)+str(posy+z)
                
                if casino [posx+i] [posy+z] != "   ":
                    self.permiso = "X"
                    break

                if casino [posx-1] [posy-1] != "   ":
                    self.permiso = "X"
                    break
                


    def clona_mapa (self,mapa) :

        copia = [ ]
        for i in range (len(mapa)):
                c=[]
                c=(mapa[i])[:]
                copia.append(c)
        return copia
     
                 
    def instalar (self,casino,objeto,posx,posy):

        for i in range ( len(objeto)):
            for z in range(len(objeto[0])):
                casino [posx+i][posy+z] = objeto [i][z]

        return casino


    def coloca_cosas (self):
       
        def key_recorder(key):              
         
            self._key2 = str(key)
            l.stop ( )
        
        self.continuar = "X"

        while self.continuar == "X":

            self.display_coloca_cosas ()

            with Listener(on_press=key_recorder) as l: 
                l.join( )
                
            self.key_actions (kasino.mapa,5) 
            
            clear ()
    
        self.medir_espacio(kasino.mapa, o.entrega_lista_maquina(self.compra), self.posiciones[0], self.posiciones[1]) 

        if self.permiso == "V":

            self.proyecto = self.clona_mapa (kasino.mapa)

            self.proyecto = self.instalar(self.proyecto , o.entrega_lista_maquina(self.compra), self.posiciones[0], self.posiciones[1])  
            
            respuesta_proyecto = self.confirma_compra (self.proyecto)

            if respuesta_proyecto == "V":

                kasino.mapa = self.clona_mapa (self.proyecto)

                k.compra (self.compra )
              
        else:
            k.titulo_informe()
            print("\n","\t"*3,"ESTAS CONSTRUYENDO SIN DEJAR LOS ESPACIOS NECESARIOS.. MIDE BIEN ..")
            sleep(3)
            clear()
            pass     
     
        self.reset()



    def display_confirma_compra (self): 
        
        
        self.lista_instalar [self._posx][self._posy] = ' ◄ '

        print('''
          ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
          ♦                                                                                                             ♦
          ♠                                     ES ASI COMO QUIERES QUE QUEDE ??                                        ♠                                 
          ♦                                                                                                             ♦
          ♣                   ╔═════════════╗                                      ╔═════════════╗                      ♣ 
          ♠                   ║   INSTALAR  ║  '''+self.lista_instalar [0][0]+'''                                 ║   CANCELAR  ║  '''+self.lista_instalar [0][1]+'''                 ♠ 
          ♣                   ╚═════════════╝                                      ╚═════════════╝                      ♠
          ♦                                                                                                             ♦                               
          ♣            ESTA PERFECTAMENTE DONDE ESTA !!                     QUIZAS UN POCO MAS A LA DERECHA ....        ♠
          ♣                                                                                                             ♦
          ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥  ''')
 

    def confirma_compra (self,mapa):
        self.reset()
        def key_recorder(key):              
         
            self._key2 = str(key)
            l.stop( )
        
        self.continuar = "X"

        while self.continuar == "X":
            
            k.game (mapa)
            self.display_confirma_compra()

            with Listener(on_press=key_recorder) as l: 
                l.join( )
                
            self.key_actions (self.lista_instalar ,8) 
            clear ()
        
        self.reset()

        return self.respuesta_confirma 
      
      
    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """    METODOS DECORATION                                           X - 7                                                                                        METODOS DECORATION        """ 

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """  Metodos en grupo, display_decoration() muestra la parte grafica e integra la lista para desplazarnos por el menu, decoration() es el metodo principal y gestiona
        la funcion integrada key_recorder() que captura la tecla pulsada y mediante key_actions() realiza las acciones correspondientes, se encarga de mostrar todas
        las opciones de decoracion y en caso de comprar añadirlas al dicc correspondiente para que influyan en la -fama- del casino """

  
    def display_decoracion (self): 
        precio1=k.printea_money(k.catalogo["PAREDES-2"])
        precio2=k.printea_money(k.catalogo["PAREDES-3"])
        precio3=k.printea_money(k.catalogo["PAREDES-4"])
        self.lista_display_decoracion [self._posx][self._posy] = ' ◄ '
        dinero = k.printea_money(kasino.dinero)
        print('''
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
            ♦                                                                                                             ♦
            ♣                                                   PAREDES                                                   ♣
            ♠                                                                                                             ♦
            ♣         ╔═════════════╗          ╔═════════════╗           ╔═════════════╗         ╔═════════════╗          ♣ 
            ♠         ║   PAPEL DE  ║  '''+self.lista_display_decoracion [0][0]+'''     ║ PINTURA CON ║  '''+self.lista_display_decoracion [0][1]+'''      ║   ESTILO    ║  '''+self.lista_display_decoracion [0][2]+'''    ║   PAN DE    ║  '''+self.lista_display_decoracion [0][3]+'''     ♠
            ♥         ║    PARED    ║          ║   ESTILO    ║           ║  VENECIANO  ║         ║     ORO     ║          ♥
            ♦         ╚═════════════╝          ╚═════════════╝           ╚═════════════╝         ╚═════════════╝          ♦ 
            ♣               0 $                   '''+precio1+'''  $               '''+precio2+''' $              '''+precio3+'''  $             ♣               
            ♣                                                   SUELOS                                                    ♥
            ♠                                                                                                             ♦
            ♣         ╔═════════════╗          ╔═════════════╗           ╔═════════════╗         ╔═════════════╗          ♣ 
            ♠         ║   BALDOSAS  ║  '''+self.lista_display_decoracion [1][0]+'''     ║    SUELO    ║  '''+self.lista_display_decoracion [1][1]+'''      ║   BALDOSAS  ║  '''+self.lista_display_decoracion [1][2]+'''    ║   MARMOL    ║  '''+self.lista_display_decoracion [1][3]+'''     ♠
            ♥         ║    ROTAS    ║          ║  VINILICO   ║           ║ VALENCIANAS ║         ║   PULIDO    ║          ♥
            ♦         ╚═════════════╝          ╚═════════════╝           ╚═════════════╝         ╚═════════════╝          ♦ 
            ♣               0 $                   '''+precio1+''' $               '''+precio2+''' $              '''+precio3+''' $               ♣    
            ♦                                                                                                             ♦                
            ♣                                                   GENERAL                                                   ♥
            ♠                                                                                                             ♦
            ♣         ╔═════════════╗          ╔═════════════╗           ╔═════════════╗         ╔═════════════╗          ♣ 
            ♠         ║   REFORMA   ║  '''+self.lista_display_decoracion [2][0]+'''     ║   REFORMA   ║  '''+self.lista_display_decoracion [2][1]+'''      ║   REFORMA   ║  '''+self.lista_display_decoracion [2][2]+'''    ║   REFORMA   ║  '''+self.lista_display_decoracion [2][3]+'''     ♠
            ♥         ║    CUTRE    ║          ║   BASICA    ║           ║  ELEGANTE   ║         ║   SELECTA   ║          ♥
            ♦         ╚═════════════╝          ╚═════════════╝           ╚═════════════╝         ╚═════════════╝          ♦ 
            ♣               0 $                    '''+precio1+''' $               '''+precio2+''' $              '''+precio3+''' $              ♣
            ♥                                                                                                             ♥
            ♣                                                                                                             ♦
            ♠         ╔═════════════╗  '''+self.lista_display_decoracion [3][0]+'''         PASE POR CAJA..       ╔═════════════╗            GRACIAS POR ...       ♥
            ♥         ║   COMPRAR   ║          NUESTRO EQUIPO SE         ║    SALIR    ║     '''+self.lista_display_decoracion [3][1]+'''     SU VISITA.           ♣
            ♣         ╚═════════════╝       ENCARGARA DE INSTALAR        ╚═════════════╝           VUELVA PRONTO          ♦
            ♦                                   LOS PRODUCTOS                                                             ♥
            ♣                                                                                                             ♣   
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥                                                                                                      
           
                                     DINERO DISPONIBLE = '''+dinero+''' $

             EN ESTA TIENDA TIENEN CARA DE ESTIRADOS.. PREFIERO NO PREGUNTAR,ASI QUE SI NO SABES QUE MEJORAS TIENES MIRALO

                                            EN EL MENU ESTADO,INFORME
                ''')
        print(self.texto2)
                
    def decoration (self):
       
        def key_recorder(key):              
         
            self._key2 = str(key)
            l.stop( )
        
        self.continuar = "X"

        self.salir = "X"

        while self.salir == "X":

            while self.continuar == "X":
                
                k.titulo_decoracion ()
                self.display_decoracion()

                with Listener(on_press=key_recorder) as l: 
                    l.join( )
                    
                self.key_actions (self.lista_display_decoracion,7) 
                clear ()

            self.continuar = "X"
            self.reset()
            if self.respuesta_deco != "salir":

                k.compra(self.compra_deco)
                
                self.salir = "V"

        self.reset()























    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """    METODOS ESTADO CASINO                                           X -9                                                                                         METODOS ESTADO CASINO        """ 

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """ Metodos en grupo, display_opcion_estado() muestra la parte grafica e integra la lista para desplazarnos por el menu, opciones_estado() es el metodo principal y gestiona
        la funcion integrada key_recorder() que captura la tecla pulsada y mediante key_actions() realiza las acciones correspondientes,depende de lo que se elija se invocara desde aqui a
        metodos mapa o metodos informe, los dos grupos siguientes a este """

    

    def display_opcion_estado (self): 
        
        self.lista_opcion_informe [self._posx][self._posy] = ' ◄ '

        print('''
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
            ♦                                                                                                             ♦
            ♣             MAPA : Podras observar la vista aerea de tu casino con sus elementos                            ♦ 
            ♠                                                                                                             ♠                                
            ♥     INFORME :  Elaborado por nuestros asesores contiene informacion relativa a reformas, suelos, paredes..  ♥ 
            ♦                                                                                                             ♦
            ♣                 ╔═════════════╗           ╔════════════╗            ╔═════════════╗                         ♣ 
            ♠                 ║    MAPA     ║  '''+self.lista_opcion_informe[0][0]+'''      ║  INFORME   ║  '''+self.lista_opcion_informe[0][1]+'''       ║    SALIR    ║  '''+self.lista_opcion_informe[0][2]+'''                    ♠
            ♥                 ╚═════════════╝           ╚════════════╝            ╚═════════════╝                         ♥
            ♦                                                                                                             ♦                                                     
            ♣                         o.. te has equivocado y quieres volver ?.. pulsa SALIR                              ♣
            ♠                                                                                                             ♠      
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥  ''')


    def opciones_estado (self):
       
        def key_recorder(key):              
         
            self._key2 = str(key)
            l.stop( )
        
       
        self.salir = "X"

        while self.salir == "X":

            self.continuar = "X"
    
            while self.continuar == "X":
                
                
                k.titulo_informe()
                self.display_opcion_estado ()

                with Listener(on_press=key_recorder) as l: 
                    l.join( )
                    
                self.key_actions (self.lista_opcion_informe ,9) 
                clear ()
            
            self.reset()
            #return self.respuesta_estado 
            if self.respuesta_estado == "mapa":
                self.ver_mapa()
                clear ()

            elif self.respuesta_estado == "informe":
                self.estado()
                clear ()


    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """    METODOS VER MAPA                                          X -6                                                                                         METODOS VER MAPA        """ 

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """ Metodos en grupo, display_ver_mapa() muestra el mapa en su estado actual, ver_mapa() es el metodo principal y gestiona
        la funcion integrada key_recorder() que captura la tecla pulsada y mediante key_actions() realiza las acciones correspondientes,En este caso solo hay una 
        opcion, volver,nos muestra el mapa hasta que decidamos volver  """


    def display_ver_mapa (self): 
        
        self._posx,self._posy = 0,0
        self.lista_ver_mapa [self._posx][self._posy] = ' ◄ '

        print('''
          ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠  ♥
          ♦                                                                                                              ♦
          ♣           ESTE ES EL ESTADO ACTUAL DE TU CASINO                                                              ♦ 
          ♠                                                                                                              ♠                                
          ♣                                             ╔═════════════╗                                                  ♣ 
          ♠                                             ║    VOLVER   ║  '''+self.lista_ver_mapa[0][0]+'''                                             ♠
          ♠                                             ╚═════════════╝                                                  ♠                                                                                     
          ♣                                                                  PULSA ENTER PARA VOLVER AL MENU             ♦
          ♣                                                                                                              ♦
          ♥  ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥  
          
                                                  ''' )
 

    def ver_mapa (self):
       
        def key_recorder(key):              
         
            self._key2 = str(key)
            l.stop( )
        
        self.continuar = "X"

        while self.continuar == "X":
            
            k.game (kasino().mapa)
            print ("\n","\t"*4,"DINERO $$$  ➔  ",kasino.dinero,"\t\tDIA  ➔  ",kasino.dia)
            self.display_ver_mapa()

            with Listener(on_press=key_recorder) as l: 
                l.join( )
                
            self.key_actions (self.lista_ver_mapa ,6) 
            clear ()
        
        self.reset()
      
 
    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """    METODOS VER INFORME                                          X -6                                                                                       METODOS VER INFORME         """ 

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """ Metodos en grupo, display_estado() muestra un informe actual delcasino, con ladecoracion y maquinas adquiridas y su correspondiente fama, visitas y ganancia, estado() es el metodo principal y gestiona
        la funcion integrada key_recorder() que captura la tecla pulsada y mediante key_actions() realiza las acciones correspondientes,En este caso solo hay una 
        opcion, volver,nos muestra el informe hasta que decidamos volver  """


    def display_estado (self): 
        
        self._posx,self._posy = 0,0
        self.lista_estado [self._posx][self._posy] = ' ◄ '
        self.dinero_maquinas = 0
        
        paredes_4 = "\n\t\t PAREDES NIVEL 4 ➟  ESTAMOS SITUANDO NUESTRO CASINO EN LA ELITE MUNDIAL , AUTENTICA PINTURA PAN DE ORO CON UNA PUREZA  \n\t\t\t MAXIMA,E INCRUSTRACIONES DE MARMOL BLANCO , TODO UN LUJO QUE NOS SITUA ENTRE LOS MAS VISITADOS."
        paredes_3 = "\n\t\t PAREDES NIVEL 3 ➟  MAGNIFICO ESTILO Y DISEÑO , AYUDA A CREAR UN AMBIENTE TRANQUILO Y RELAJADO Y ESTO SE APRECIA \n\t\t\t ENTRE LOS CLIENTES.. AHORA NO SOLO ATRAEMOS NUEVOS SINO QUE EL QUE VIENE QUIERE REPETIR."
        paredes_2 = "\n\t\t PAREDES NIVEL 2 ➟  PUEDE QUE NO SEA NADA DEL OTRO MUNDO PERO DESPUES DE UNA ELEGANTE MANO DE PINTURA  \n\t\t\t SE RESPIRA UN AIRE RENOVADO , SEGURO QUE VENDRA MAS GENTE AHORA QUE YA NO PARECE UN TUGURIO..."
        paredes_1 = "\n\t\t PAREDES NIVEL 1 ➟  LAS PAREDES QUE TENIA EL CASINO CUANDO FUE COMPRADO.. NO ESPERES QUE ATRAIGAN MAS VISITAS \n\t\t\t QUE LA DE LA GENTE LOCAL .. DEBERIAMOS PENSAR EN PONER UNA BUENA MANO DE PINTURA..."
        pared = [paredes_1,paredes_2,paredes_3,paredes_4]
        suelo_4 = "\n\t\t SUELO NIVEL 4 ➟  CONTEMPLAR ESTE CASINO ES COMO CONTEMPLAR UN TROZO DE CIELO .. MARMOL BLANCO PULIDO DE LA MAS \n\t\t\t ALTA CALIDAD,UN REGALO PARA LA VISTA , ES UN PRIVILEGIO VISITAR UN  CASINO DE ESTAS CARACTERISTICAS"
        suelo_3 = "\n\t\t SUELO NIVEL 3 ➟  BALDOSAS DE PIEDRA VALENCIANA ARTESANAL, SINCERAMENTE .. UNA OBRA DE ARTE, SALTA A LA VISTA QUE \n\t\t\tNOS PREOCUPAMOS POR OFRECER LAS MAXIMAS CALIDADES Y ESO SE NOTA A LA HORA DE SUMAR VISITAS...."
        suelo_2 = "\n\t\t SUELO NIVEL 2 ➟  SUELO VINILICO EFECTO PIEDRA , LO CIERTO ES QUE EL RESULTADO ES EXCELENTE ,SOLO SI UNO SE FIJA SE NOTA QUE  \n\t\t\t ES VINILICO EN LUGAR DE PIEDRA NATURAL. Y LO MEJOR...YA NO PARECEMOS UN ANTRO CUTRE."
        suelo_1 =  "\n\t\t SUELO NIVEL 1 ➟  NO SE PORQUE SIEMPRE ESTA PEGAJOSO.. POR MUCHO QUE SE LIMPIE.. Y TAMBIEN ESTA BASTANTE  \n\t\t\t DETERIORADO.. CON ESTE ASPECTO NO ATRAEREMOS A NADIE, ES MAS .. REZA PARA QUE NO SE ESPANTEN."
        suelo =[suelo_1,suelo_2,suelo_3,suelo_4]
        reforma_4 =  "\n\t\t REFORMA NIVEL 4 ➟  LA GUINDA DEL PASTEL, ABSOLUTAMENTE CADA DETALLE CUIDADO PARA CONSEGUIR LA PERFECCION , \n\t\t\t DEFINITIVAMENTE ESTE CASINO ESTA ENTRE LOS MEJORES Y ES TODA UNA EXPERIENCIA VISUAL EL VISITARLO."
        reforma_3 =  "\n\t\t REFORMA NIVEL 3 ➟  TODOS LOS PRODUCTOS RENOVADOS CON ELEGANCIA EN UNA CALIDAD MEDIO-ALTA, CREA UN AMBIENTE  \n\t\t\t AGRADABLE , HIGIENICO , CUIDADO.. SE NOTAN LOS PEQUEÓS DETALLES.. Y TAMBIEN SE NOTARA EL AUMENTO DE VISITAS."
        reforma_2 =  "\n\t\t REFORMA NIVEL 2 ➟  EL SIMPLE HECHO DE ARREGLAR TODO LO PRESENTE , AUN SIN EFECTUAR CAMBIOS ES UN NOTABLE   \n\t\t\t CAMBIO.. SIN RESPIRARSE LUJO.. TODO FUNCIONA CORRECTAMENTE.. VAMOS PROGRESANDO."
        reforma_1 = "\n\t\t REFORMA NIVEL 1 ➟  EN PRINCIPIO CAMBIAMOS LO JUSTO PARA QUE NOS DEN LA LICENCIA.. TENEMOS BOMBILLAS ROTAS  \n\t\t\t Y TODO TIPO DE DESPERFECTOS. ADEMAS DE QUE LAS INSTALACIONES NO ESTAN EN MUY BUEN ESTADO.. SI TUBIERA\n\t\t\t  QUE USAR EL BAÑO DE CLIENTES NO TRABAJARIA AQUI... "
        reforma = [reforma_1,reforma_2,reforma_3,reforma_4]

        self.fama_edificio , self.paredes , self.suelo , self.decoracion = k.fama(k.decoracion)

        self.texto_deco_suelo = suelo[self.suelo-1]
        self.texto_deco_pared = pared [self.paredes-1]
        self.texto_deco_reforma = reforma [self.decoracion-1]

        for i  in kasino.maquinas:
       
            self.dinero_maquinas += (k.beneficios_maquinas[i]*kasino.maquinas[i])

        maquinas= k.printea_money(self.dinero_maquinas)

        dinero = k.printea_money(kasino.dinero)

        self.ganancias = self.dinero_maquinas*(((self.fama_edificio*3)*2)/1000+kasino.modificador_ganancias)
        ganancias = k.printea_money(int(self.ganancias))

        print(''' 
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥                           
                                                         ╔═════════════╗                                                 
                 PULSA ENTER PARA VOLVER AL MENU         ║    VOLVER   ║  '''+self.lista_estado[0][0]+'''                                           
                                                         ╚═════════════╝                                          
                DIA  ➤   '''+str(kasino.dia)+'''  

                DINERO DISPONIBLE ➤  '''+dinero+''' $              ''')

        print ("\n","\t"*2,"RECUENTO DE MAQUINAS 🢃 🢃 🢃 \t\t   DINERO MAXIMO  / DIA EN TOTAL  🢂 ",maquinas,"$\n")

        for key , value in kasino.maquinas.items():
                print ("\t\t",key.upper()," ➟ ",value)  
 
        print ("\n             ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥")

        print(self.texto_deco_pared)
        print(self.texto_deco_suelo)
        print(self.texto_deco_reforma)
        
        print ("\n","\t"*2,"FAMA == ", self.fama_edificio," \t\t\t   PREVISION DIARIA DE VISITANTES  🢂 ",self.fama_edificio *3,"\n")
        
        print("\n","\t"*2,"GANANCIAS ESTIMADAS == ",ganancias," $")


    def estado (self):
        
        def key_recorder(key):              
         
            self._key2 = str(key)
            l.stop( )
        
        self.continuar = "X"

        while self.continuar == "X":
            
            k.titulo_estado ()
            self.display_estado()

            with Listener(on_press=key_recorder) as l: 
                l.join( )
                
            self.key_actions (self.lista_estado ,6) 
            clear ()
        
        self.reset()















    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """    METODOS CONFIGURATION                                          X -6                                                                                       METODOS CONFIGURATION         """ 

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """ Metodos en grupo, display_configuracion muestra la parte grafica e integra la lista para desplazarnos por el menu , configuration() es el metodo principal y gestiona
        la funcion integrada key_recorder() que captura la tecla pulsada y mediante key_actions() realiza las acciones correspondientes,depende de lo que se elija se obtendra un resultado 
        que en esta ocasion se enviara a main para que este realice acciones en consecuencia"""
 

    def display_configuracion (self): 
        
        self.lista_configuracion [self._posx][self._posy] = ' ◄ '

        print('''
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥
            ♦                                                                                                             ♦
            ♣            PULSA GUARDAR PARA PODER SEGUIR ESTA PARTIDA EN OTRA OCASION                                     ♦ 
            ♠                                                                                                             ♠                                
            ♥                                                     PULSA CARGAR PARA RETOMAR UNA PARTIDA GUARDADA          ♥ 
            ♦                                                                                                             ♦
            ♣                              ╔═════════════╗                      ╔════════════╗                            ♣ 
            ♠                              ║   GUARDAR   ║   '''+self.lista_configuracion[0][0]+'''                ║   CARGAR   ║    '''+self.lista_configuracion[0][1]+'''                     ♠
            ♥                              ╚═════════════╝                      ╚════════════╝                            ♥
            ♦                                                                                                             ♦     
            ♥                              ╔═════════════╗                      ╔════════════╗                            ♣ 
            ♠                              ║    SALIR    ║   '''+self.lista_configuracion[1][0]+'''                ║   VOLVER   ║   '''+self.lista_configuracion[1][1]+'''                      ♠
            ♥                              ╚═════════════╝                      ╚════════════╝                            ♥
            ♦                                                                                                             ♦                                                     
            ♣       PULSA SALIR PARA ABANDONAR EL JUEGO.. GUARDA ANTES..                                                  ♣
            ♠                                                                                                             ♠                                                                  
            ♠                                                         PULSA VOLVER PARA REGRESAR AL MENU PRINCIPAL        ♠                                                                                                       
            ♦                                                                                                             ♦
            ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥  ''')


    def configuration (self):
       
        def key_recorder(key):              
         
            self._key2 = str(key)
            l.stop( )
        
        self.resultado_config  =""
        self.continuar = "X"

        while self.continuar == "X":
            
            k.titulo_configuracion()
            self.display_configuracion()

            with Listener(on_press=key_recorder) as l: 
                l.join( )
                
            self.key_actions (self.lista_configuracion ,10) 
            clear ()
         
        
        self.reset()
        return  self.resultado_config 













    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

    """    METODOS SIGUIENTE                                                                                                                                              METODOS SIGUIENTE         """ 

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""
    from random import randrange

    def siguiente (self):   

        self.dinero_maquinas = 0

        for i  in kasino.maquinas:
       
            self.dinero_maquinas += (k.beneficios_maquinas[i]*kasino.maquinas[i])

        self.fama_edificio , self.paredes , self.suelo , self.decoracion = k.fama(k.decoracion)


        suerte = randrange(6,17)/10
        self.ganancias = self.dinero_maquinas*(((self.fama_edificio*3)*2)/1000+kasino.modificador_ganancias)
        self.ganancias=self.ganancias*suerte
        podriamos = k.printea_money(self.dinero_maquinas*7)

        ganamos = k.printea_money(int(self.ganancias)*7)


        k.titulo_informe()
        playsound(pop,False)
        print ("\n"*2,"\t"*4," HA PASADO UNA SEMANA DESDE EL ULTIMO INFORME")
        sleep(1)
        playsound(pop,False)
        print ("""    

                                      INFORME SEMANAL
        

                             Con el casino lleno hubiesemos ganado = """+podriamos+""" $
                      
                                                            
                             Pero con las visitas que hemos tenido esta semana hemos ganado...
                             

                             GANANCIAS =  """+ganamos+""" $ """)

        sleep(2)
        playsound(here,False)
        sleep(1)
        clear()
        k.titulo_semana()
        sleep(1)
        clear ()
        
        kasino.dinero= int(kasino.dinero) + (int(self.ganancias)*7)
        kasino.dia = int(kasino.dia) + 1