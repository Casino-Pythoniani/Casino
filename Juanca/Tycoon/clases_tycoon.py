
""" clases_tycoon 
IMPORTAMOS: Playsound para reproducir sonidos, os para poder usar nuestra lambda clear, que dejara la pantalla a 0 , para que no se acumule lo printeado y sleep para producir -pausas- controladas
 en el programa.  """

from playsound import playsound
import os
clear = lambda: os.system('cls')
from time import sleep

from os import close, strerror


""" O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""

"""    CLASE CASINO                                                                                                                                                                 CLASE KASINO   """ 

""" O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O"""



class kasino:

    """ El objetivo de esta clase es guardar el mapa, que sera lista de listas y lo pondremos como variable de 
        de clase para facilitar el acceso a este desde cualquier modulo al igual que el resto de variables de clase.
        (mapa,dinero,dia,maquinas y decoracion son las variables que -guardaremos- para poder seguir partidas)"""

    mapa= []
    dinero = 500000
    dia = 0
    maquinas = {"tragaperras": 0 , "b_jack" : 0 , "poker" : 0 , "baccarat": 0 , "dados": 0 , "ruleta": 0 , "bingo" : 0 ,"carreras":0}
    decoracion = { "PAREDES-2" : 0 , "PAREDES-3": 0 , "PAREDES-4": 0, "SUELO-2" : 0 , "SUELO-3": 0 , "SUELO-4": 0,"REF-2" : 0 , "REF-3": 0 , "REF-4":0}

    modificador_fama=0
    """MODIFICADOR_FAMA  nos permite calibrar el juego influyendo en la fama de esta manera : fama = (10*paredes)+(10*suelo)+(10*reforma) + modificador_fama + kasino.modificador_fama """

    modificador_ganancias=-0
    """ MODIFICADOR_GANANCIAS nos permite calibrar el juego influyendo en las ganancias de esta manera:  self.ganancias = self.dinero_maquinas*(((self.fama_edificio*3)*2)/1000+kasino.modificador_ganancias)"""

# VARIABLES DE GUARDADO


    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O           INIT    """


    def __init__(self):

        """ En el constructor tenemos self.beneficios_maquinas que es un diccionario que nos indicara cuanto ganaremos con cada maquina  """

        self.beneficios_maquinas = {"tragaperras":500 , "b_jack" : 900 , "poker" : 1000 , "baccarat": 600 , "dados":500 , "ruleta":900 , "bingo" :750 ,"carreras":700}

        self.catalogo = {"tragaperras":50000 , "b_jack" : 90000 , "poker" : 100000 , "baccarat": 60000 , "dados": 50000 , "ruleta":90000 , "bingo" :75000 ,"carreras":70000,
                        "PAREDES-2" : 80000 , "PAREDES-3": 250000 , "PAREDES-4":1000000,"SUELO-2" : 80000 , "SUELO-3": 250000 , "SUELO-4":1000000,"REF-2" : 80000 , "REF-3": 250000 , "REF-4":1000000}

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O         CREAR-MAPA  """   


    def crear_mapa (self, ancho = 40 , largo = 40):

        """ Este metodo nos creara el mapa Kasino por defecto se creara de 40x40 y aunque en este prog no es necesario, dejo la opcion 
        de introducir ancho y largo distintos para poder crear diferentes mapas segun avances o segun dificultad... 
        TENER EN CUENTA QUE LOS ESPACIOS DE LA LISTA DE EL -MAPA- SON 3 CARACTERES ESPACIO  """

        for i in range (largo):

            a = "   "
            b = []
            for z in range (ancho):
                b.append(a)
            kasino.mapa.append(b)

        for i in range (1,ancho -1):
            kasino.mapa[0][i]="═══"
            kasino.mapa[largo-1][i]="═══"

        for i in range (1,largo -1):
            kasino.mapa[i][0]= "        ║"
            kasino.mapa[i][ancho-1]= "║"
        
        kasino.mapa [0][0]="        ╔"
        kasino.mapa [0][ancho-1]="╗"
        kasino.mapa [largo-1][0]="        ╚"
        kasino.mapa [largo-1][ancho-1]="╝"

        
    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O         FAMA    """ 

    
    def fama (self , diccionario):

        """ Este metodo nos dara mediante una formula la variable fama , que dependera de la decoracion del casino e influira en las visitas.
         Utilizamos el diccionario kasino.decoracion, variable propia de esta clase para hacer con este una lista, luego dividimos en 3 partes la lista
        segun corresponde. Luego las recorremos para puntuar paredes suelo y reforma segun indique y utilizaremos estas 3 variables para la formula fama.  """

        decoracion_list = []
        for key , value in diccionario.items():
            a=[]
            a.append(key)
            a.append(value)
            decoracion_list.append (a)

        paredes_list = decoracion_list [0:3]
        suelo_list = decoracion_list  [3:6]
        reforma_list = decoracion_list  [6:]

        paredes = 1
        suelo = 1
        reforma = 1

        for i in range (len(paredes_list)):
            if paredes_list [i][1] == 1 :
                paredes = i+2 

        for i in range (len(suelo_list)):
            if suelo_list [i][1] == 1 :
                suelo = i+2

        for i in range (len(reforma_list)):
            if reforma_list [i][1] == 1 :
                reforma = i+2

        modificador_fama = 0

        if paredes >= 4 and suelo >= 4 and reforma >= 4 :
            modificador_fama = 45

        elif paredes >= 3 and suelo >= 3 and reforma >= 3 :
            modificador_fama = 33   

        elif paredes >= 2 and suelo >= 2 and reforma >= 2 :
            modificador_fama = 12

        fama = (10*paredes)+(10*suelo)+(10*reforma) + modificador_fama + kasino.modificador_fama

        """ FORMULA FAMA : Con esta formula se calcula la fama, que dependera de la decoracion e influira en los visitantes 
        Se puede usar modificador_fama para calibrar el juego o añadir niveles de dificulad """
        
        return fama , paredes , suelo , reforma


    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O         GAME    """ 


    def game (self,mapa):

        """ Este metodo lo usaremos para printear el mapa, pondremos un titulo y luego mediante -join- printearemos la lista-mapa   """

        self.titulo()

        for fila in mapa:
            print("".join(fila))




    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O         COMPRA    """ 


    def compra (self,algo):

        """ Este metodo se ejecutara al comprar cualquier articulo y añadira dicho articulo al dicc correspondiente para -saber- que lo tenemos y 
        nos descontara el dinero si lo tenemos, en caso contrario nos avisara que no nos llega y volveremos. 
        Nos pide 1 parametro, algo es aquello que compramos  """

        

        if kasino.dinero < self.catalogo[algo]:
            print ("\n"*6,"\t"*5,"No te llega el dinero, vuelve a visitarnos mas adelante")
            sleep(3)
            clear()
               
        else:

            if algo in kasino().maquinas.keys():

               kasino().maquinas[algo] += 1
               kasino.dinero -= self.catalogo[algo]
               kasino.titulo_informe(self)
               print("\n"*6,"\t"*5,"GRACIAS POR TU COMPRA !!\n\n","\t"*4,"EN BREVES LO RECIBIRAS Y LO INSTALAREMOS")
               sleep(1)
               clear()
               

            elif algo in kasino().decoracion.keys():
                 
                if kasino().decoracion[algo] == 0:

                   kasino().decoracion[algo] = 1
                   kasino.dinero -= self.catalogo[algo]
                   kasino.titulo_informe(self)
                   print("\n"*6,"\t"*5,"GRACIAS POR TU COMPRA !!\n\n","\t"*4,"EN BREVES LO RECIBIRAS Y LO INSTALAREMOS")
                   sleep(2)
                   clear()
                  

                else:
                    print("\n"*6,"\t"*5,"YA TIENES ESTA MEJORA !!\n\n","\t"*3,"SI LO DESEAS PUEDES ESCOGER OTRO ARTICULO")
                    sleep(3)
                    clear()

            else:
                print("\n"*6,"\t"*5,"YA TIENES ESTA MEJORA !!\n\n","\t"*3,"SI LO DESEAS PUEDES ESCOGER OTRO ARTICULO")
                sleep(3)
                clear()


    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O         GUARDAR     MAPA   """ 
    

    def guardar_mapa( self, mapa ):

        """ Este metodo parte el mapa entregado en 2 mitades ya que es muy grande para pasarlo a documento, luego abre un stream WT y añadimos las filas de los mapas al documento txt 
        corespondiente separadas con una X que usaremos luego, tambien separamos con una S las dos mitades del mapa. saremos la s para distinguir entro las 2 mitades y la x para hacer 
        split y separar elementos """

        self.mapa_izda=[]
        self.mapa_dxa=[]
      
        for i in mapa:
            self.mapa_izda.append ( i [0:19] )
            self.mapa_dxa.append ( i [19:40] )

        stream_guardar = open("yo_mapa.txt","wt",encoding="utf-8")

        for i in self.mapa_izda:

                stream_guardar.write(str(i)+"X")

        primero = True 

        for i in self.mapa_dxa:
                if primero == True:
                    stream_guardar.write("S"+str(i)+"X")
                    primero = False
                else:
                    stream_guardar.write(str(i)+"X")
        stream_guardar=(close)

   


      
    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O         CARGAR MAPA   """ 

    def cargar_mapa (self):

        """ Usamos este metodo para igualar la variable mapa kasino a lo escrito en el metodo casino.guardar en 1 documento y asi rcuperar datos .
        separamos el str con un split usando las X escritas , recorremos el str y usamos las comas para recuperar los elementos de la lineas de mapa, [][] es decir de
        la lista de listas.La S nos distingue entre las dos mitades del mapa, luegojuntamos las dos mitades en un solo mapa otra vez , cerramos el stream
        y hacemos return de el mapa cargado  """

        stream_cargar = open ('yo_mapa.txt', 'rt',encoding="utf-8")
        mapa=stream_cargar.readlines()
        
        a = mapa[0].split("X")
        mapa__I=[]
        mapa__D=[]
        toca = "izda"
        for lista in a:
            pasar="X"
            linea1=[]
            trozo=""
            for i in lista:
                if pasar=="X":
                
                    borrar = ["[","'"]
                    if i in borrar:
                        pass
                    elif i == "," or i == "]":
                        linea1.append(trozo)
                        trozo=""
                        pasar="V"
                    elif i == "S":
                        toca="dxa"
                    else:
                        trozo+=i

                else:
                    pasar="X"
                    pass
            if toca == "izda":
                mapa__I.append(linea1)
            else:
                mapa__D.append(linea1)

        mapa_cargado=[]
        for i in range (len(mapa__I)):

            mapa_cargado.append(mapa__I[i]+mapa__D[i]) 

        stream_cargar=(close)
        return  mapa_cargado


    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O        GUARDAR-OTROS      """ 


    def guardar_otras (self,maquinas,decoracion,dia,dinero):#dicc,dicc,int,int

        """ Este metodo guardara en 1 documento los dicc kasino maquina y kasino decoracion y los ints dia y dinero ,en esta ocasion se escribiran todos juntos ya que es facil recuperarlos """

        stream_guardar = open("yo_otros.txt","wt",encoding="utf-8")
        for i in maquinas:
            stream_guardar.write(str(maquinas[i]))

        for i in decoracion:
                stream_guardar.write(str(decoracion[i]))

        stream_guardar.write("D"+str(dia))
        stream_guardar.write("M"+str(dinero))    


    def cargar_otras(self):

        """ Este metodo recuperara los dicc kasino maquinas y kasino decoracion y los ints dia y dinero, para ello usamos un contador y recorremos los dicc igualando el dicc a su parte de la cadena 
        escrita en el documento mediante el contador  """

        stream_cargar = open ('yo_otros.txt', 'rt',encoding="utf-8")
        datos=stream_cargar.readlines()
        
        # print(datos)
        # print (len(kasino.maquinas))

        lista_maquinas=[]
        lista_deco =[]
        day=""
        money=""

        contador=0
        dia_o_dinero="dia"

        for i in datos[0]:
            # print(contador,i)
            if contador <8:
                lista_maquinas.append(i)
                contador+=1

            elif contador <17:
                lista_deco.append(i)
                contador+=1


            elif contador >= 17 and dia_o_dinero =="dia":
                if i =="D":
                    pass
                elif i =="M":
                    dia_o_dinero="dinero"
                else:
                    day+=i
            elif contador >= 17 and dia_o_dinero == "dinero":
                money+=i
                
            

        # print("lm",lista_maquinas)
        # print ("ld",lista_deco)
        # print(day,money)

        contador=0
        for i in kasino.maquinas:
            kasino.maquinas[i]=int(lista_maquinas[contador])
            contador+=1

        contador=0
        for i in kasino.decoracion:
            kasino.decoracion[i]=int(lista_deco[contador])
            contador+=1

        kasino.dia=int( day)
        kasino.dinero=int(money)
        

    def printea_money (self,x):

       
        letras=str(x)[::-1]
        resultado=""
        contador=0
        
        for i in letras:
            resultado+=i
            contador+=1
            
            if contador==3 and len(letras )>3:
                resultado+="."
                contador =0
        resultado = resultado[::-1]
        resultado=resultado.lstrip(".")
  
        return resultado

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O      TITULOS ASCI   """ 

    """ Todos los metodos de titulos asci hasta el final de esta clase (kasino) podrian ser funciones independientes pero las  pongo aqui para agruparlas """


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

    def titulo_constructor (self):

        print("""
                            
                    ░█████╗░░█████╗░███╗░░██╗░██████╗████████╗██████╗░██╗░░░██╗░█████╗░████████╗░█████╗░██████╗░
                    ██╔══██╗██╔══██╗████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
                    ██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░░░░██║░░░██████╔╝██║░░░██║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝
                    ██║░░██╗██║░░██║██║╚████║░╚═══██╗░░░██║░░░██╔══██╗██║░░░██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗
                    ╚█████╔╝╚█████╔╝██║░╚███║██████╔╝░░░██║░░░██║░░██║╚██████╔╝╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║
                    ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
                    """)


    def titulo_decoracion (self):

        print ("""
                                
                        ██████╗░███████╗░█████╗░░█████╗░██████╗░░█████╗░░█████╗░██╗░█████╗░███╗░░██╗
                        ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
                        ██║░░██║█████╗░░██║░░╚═╝██║░░██║██████╔╝███████║██║░░╚═╝██║██║░░██║██╔██╗██║
                        ██║░░██║██╔══╝░░██║░░██╗██║░░██║██╔══██╗██╔══██║██║░░██╗██║██║░░██║██║╚████║
                        ██████╔╝███████╗╚█████╔╝╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║╚█████╔╝██║░╚███║
                        ╚═════╝░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝
                        """)


    def titulo_estado (self) :

        print(""" 
                                        
                                ███████╗░██████╗████████╗░█████╗░██████╗░░█████╗░
                                ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
                                █████╗░░╚█████╗░░░░██║░░░███████║██║░░██║██║░░██║
                                ██╔══╝░░░╚═══██╗░░░██║░░░██╔══██║██║░░██║██║░░██║
                                ███████╗██████╔╝░░░██║░░░██║░░██║██████╔╝╚█████╔╝
                                ╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░╚════╝░""")


    def titulo_informe (self):

        print ("""
                                    
                            ██╗███╗░░██╗███████╗░█████╗░██████╗░███╗░░░███╗███████╗
                            ██║████╗░██║██╔════╝██╔══██╗██╔══██╗████╗░████║██╔════╝
                            ██║██╔██╗██║█████╗░░██║░░██║██████╔╝██╔████╔██║█████╗░░
                            ██║██║╚████║██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══╝░░
                            ██║██║░╚███║██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║███████╗
                            ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
                            """)

    def titulo_configuracion (self):

        print (""" 
                            
                    ░█████╗░░█████╗░███╗░░██╗███████╗██╗░██████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░██╗░█████╗░███╗░░██╗
                    ██╔══██╗██╔══██╗████╗░██║██╔════╝██║██╔════╝░██║░░░██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║
                    ██║░░╚═╝██║░░██║██╔██╗██║█████╗░░██║██║░░██╗░██║░░░██║██████╔╝███████║██║░░╚═╝██║██║░░██║██╔██╗██║
                    ██║░░██╗██║░░██║██║╚████║██╔══╝░░██║██║░░╚██╗██║░░░██║██╔══██╗██╔══██║██║░░██╗██║██║░░██║██║╚████║
                    ╚█████╔╝╚█████╔╝██║░╚███║██║░░░░░██║╚██████╔╝╚██████╔╝██║░░██║██║░░██║╚█████╔╝██║╚█████╔╝██║░╚███║
                    ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝
                    """)


    def titulo_semana (self):

        print(""" 
        
        
                                        
                                ░██████╗██╗░██████╗░██╗░░░██╗██╗███████╗███╗░░██╗████████╗███████╗
                                ██╔════╝██║██╔════╝░██║░░░██║██║██╔════╝████╗░██║╚══██╔══╝██╔════╝
                                ╚█████╗░██║██║░░██╗░██║░░░██║██║█████╗░░██╔██╗██║░░░██║░░░█████╗░░
                                ░╚═══██╗██║██║░░╚██╗██║░░░██║██║██╔══╝░░██║╚████║░░░██║░░░██╔══╝░░
                                ██████╔╝██║╚██████╔╝╚██████╔╝██║███████╗██║░╚███║░░░██║░░░███████╗
                                ╚═════╝░╚═╝░╚═════╝░░╚═════╝░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝

                                ░██████╗███████╗███╗░░░███╗░█████╗░███╗░░██╗░█████╗░
                                ██╔════╝██╔════╝████╗░████║██╔══██╗████╗░██║██╔══██╗
                                ╚█████╗░█████╗░░██╔████╔██║███████║██╔██╗██║███████║
                                ░╚═══██╗██╔══╝░░██║╚██╔╝██║██╔══██║██║╚████║██╔══██║
                                ██████╔╝███████╗██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║
                                ╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝""")



""" O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """

"""    CLASE OBJETOS                                                                                                                                                                 CLASE OBJETOS   """ 

""" O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O """ 

class objetos ():

    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O      CONSTRUCTOR    """ 

    def __init__(self):

        """ En el constructor de este objeto tenemos la lista de listas que printeara cada maquina en el -mapa-
        Tambien tenemos  """

        self.tragaperras = [["╔══","═══","══╗"],["║  ","T_P","  ║"],["╚══","═══","══╝"]]
        self.baccarat =  [["╔══","═══","═══","══╗"],["║ B","ACC","ARA","T ║"],["╚══","═══","═══","══╝"]]
        self.dados = [["╔══","═══","══╗"],["║  ","DA2","  ║"],["╚══","═══","══╝"]]
        self.ruleta = [["╔══","═══","══╗"],["║  ","   ","  ║"],["║  ","RUL","  ║"],["║  ","   ","  ║"],["╚══","═══","══╝"]]
        self.poker = [["╔══","═══","═══","══╗"],["║  ","   ","   ","  ║"],["║  "," PO","KER","  ║"],["║  ","   ","   ","  ║"],["╚══","═══","═══","══╝"]]
        self.b_jack =  [["╔══","═══","═══","══╗"],["║  ","BLA","CK ","  ║"],["║  ","  J","ACK","  ║"],["╚══","═══","═══","══╝"]]
        self.bingo = [["B ▀"," ▀ ","▀ B"],["I ▀"," ▀ ","▀ I"],["N ▀"," ▀ ","▀ N"],["G  ","▀▀▀","  G"],]
        self.carreras = [["H ▀"," ▀ ","▀ H"],["R ▀"," ▀ ","▀ R"],["U ▀"," ▀ ","▀ U"],["N  ","▀▀▀","  N"],]
        # [["H O"," R ","S E"],["R o"," o ","o R"],["U o"," o ","o U"],["N  ","▀▀▀","  N"],]

        #  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #  Las caracteristicas de abajo deberan de calibrarse al acabar el juego para conseguir una experiencia optima
        #  Tener en cuenta que si cambian estas hay que cambiar  self.catalogo de el metodo comprar de la clase kasino (l-170 +-)

        self.c_tragaperras = [250,10000]
        self.c_baccarat =  [300,13000]
        self.c_dados = [260,11000]
        self.c_ruleta = [420,18000]
        self.c_poker = [500,20000]
        self.c_b_jack =  [420,17000]
        self.c_bingo = [275,13000]
        self.c_carreras = [300,14000]


    """ O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O O  ENTREGA LISTA MAQUINA   """ 


    def entrega_lista_maquina (self,maquina):

        """ Este metodo se utiliza para exportar las listas de las maquinas que crea el constructor , se usaran en principio en el metodo coloca cosas de la clase display """

        if maquina == "tragaperras":
            return self.tragaperras

        elif maquina == "b_jack":
            return self.b_jack

        elif maquina == "poker":
            return self.poker

        elif maquina == "baccarat":
            return  self.baccarat

        elif maquina == "dados":
            return self.dados

        if maquina == "ruleta":
            return self.ruleta

        if maquina == "bingo":
            return self.bingo

        if maquina == "carreras":
            return self.carreras 
         

