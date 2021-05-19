from clases_tycoon import *
ka=kasino()
ka.crear_mapa()

# from random import randrange

# for i in range (10):
#     suerte = randrange(7,15)/10
#     print (suerte)









a= "200000"
b=a[::-1]
print(b)















# def cargar_mapa ():

#         """ Usamos este metodo para igualar la variable mapa kasino a lo escrito en el metodo casino.guardar en 1 documento y asi rcuperar datos .
#         separamos el str con un split usando las X escritas , recorremos el str y usamos las comas para recuperar los elementos de la lineas de mapa, [][] es decir de
#         la lista de listas.La S nos distingue entre las dos mitades del mapa, luegojuntamos las dos mitades en un solo mapa otra vez , cerramos el stream
#         y hacemos return de el mapa cargado  """

#         stream_cargar = open ('yo_mapa.txt', 'rt',encoding="utf-8")
#         mapa=stream_cargar.readlines()
#         for i in mapa:
#             print ("".join(i))
#         a = mapa[0].split("X")
#         mapa__I=[]
#         mapa__D=[]
#         # for i in a:
#         #     print (i)
#         toca = "izda"
#         for lista in a:
#             pasar="X"
#             linea1=[]
#             trozo=""
#             for i in lista:
#                 if pasar=="X":
                
#                     borrar = ["[","'"]
#                     if i in borrar:
#                         pass
#                     elif i == "," or i == "]":
#                         linea1.append(trozo)
#                         trozo=""
#                         pasar="V"
#                     elif i == "S":
#                         toca="dxa"
#                     else:
#                         trozo+=i

#                 else:
#                     pasar="X"
#                     pass
#             if toca == "izda":
#                 mapa__I.append(linea1)
#             else:
#                 mapa__D.append(linea1)

#         # NO SE XQ ME QUITA 1 ESPACIO LA ESCRITURA,LO ARREGLO ABAJO
#         # mapa__I[0][0] ='         ╔'
#         # mapa__D[0][0] =' ═══'
        



#         mapa_cargado=[]

#         for i in range (len(mapa__I)):
            


#             # mapa_cargado.extend(mapa__I[i]+mapa__D[i])
#             mapa_cargado.append(mapa__I[i]+mapa__D[i]) 

#         print (mapa_cargado[0][0]) 
#         print (kasino.mapa[0][0])

#         print (mapa_cargado[5][0],"A") 
#         print (kasino.mapa[5][0],"A")

#         for i in mapa_cargado:
#             print ("".join(i))


#         stream_cargar=(close)
#         return  mapa_cargado

#         # print(len(mapa_cargado[0]))
#         # for i in mapa_cargado:
#         #     print(i)
#         # print(len(kasino.mapa[0]))
#         # for i in kasino.mapa:
#         #     print(i)





# cargar_mapa()






































# def guardar_otras (maquinas,decoracion,dia,dinero):#dicc,dicc,int,int

#     stream_guardar = open("yo_otros.txt","wt",encoding="utf-8")
#     for i in maquinas:
#         stream_guardar.write(str(kasino.maquinas[i]))

#     for i in decoracion:
#             stream_guardar.write(str(kasino.decoracion[i]))

#     stream_guardar.write(str(kasino.dia))
#     stream_guardar.write(str(kasino.dinero))


# guardar_otras(kasino.maquinas,kasino.decoracion,kasino.dia,kasino.dinero)













































# for i in kasino.decoracion:
#     print(i)


# def cargar_otras():

#     stream_cargar = open ('yo_otros.txt', 'rt',encoding="utf-8")
#     datos=stream_cargar.readlines()
    
#     # print(datos)
#     # print (len(kasino.maquinas))

#     lista_maquinas=[]
#     lista_deco =[]
#     day=0
#     money=0

#     contador=0

#     for i in datos[0]:
#         print(contador,i)
#         if contador <8:
#             lista_maquinas.append(i)
#             contador+=1

#         elif contador <17:
#             lista_deco.append(i)
#             contador+=1
#         elif contador == 17:
#             day = int(i)
#         elif contador == 18:
#             money = int(i)

#     print("lm",lista_maquinas)
#     print ("ld",lista_deco)
#     print(day,money)

#     contador=0
#     for i in kasino.maquinas:
#         kasino.maquinas[i]=int(lista_maquinas[contador])
#         contador+=1
#     for i in kasino.decoracion:
#         kasino.decoracion[i]=int(lista_deco[contador])
#         contador+=1
#     kasino.dia= day
#     kasino.dinero=money
        
# cargar_otras()












































# def guardar2 (mapa):

#     mapa_izda=[]
#     mapa_dxa=[]
#     trozo3=[]
#     trozo4=[]

#     for i in mapa:
#         mapa_izda.append ( i [0:19] )
#         mapa_dxa.append ( i [19:40] )

#     stream_guardar = open("yo.txt","wt",encoding="utf-8")

#     for i in mapa_izda:

#             stream_guardar.write(str(i)+" X ")

#     primero = True    
#     for i in mapa_dxa:
#             if primero == True:
#                  stream_guardar.write(" S "+str(i)+" X ")
#                  primero = False
#             else:
#                 stream_guardar.write(str(i)+" X ")




# guardar2 (kasino.mapa)









# def cargar ():
    
#     stream_cargar = open ('yo.txt', 'rt',encoding="utf-8")
#     mapa=stream_cargar.readlines()
    
#     a = mapa[0].split("X")
#     mapa__I=[]
#     mapa__D=[]
#     # for i in a:
#     #     print (i)
#     toca = "izda"
#     for lista in a:
#         pasar="X"
#         linea1=[]
#         trozo=""
#         for i in lista:
#             if pasar=="X":
            
#                 borrar = ["[","'"]
#                 if i in borrar:
#                     pass
#                 elif i == "," or i == "]":
#                     linea1.append(trozo)
#                     trozo=""
#                     pasar="V"
#                 elif i == "S":
#                     toca="dxa"
#                 else:
#                     trozo+=i

#             else:
#                 pasar="X"
#                 pass
#         if toca == "izda":
#             mapa__I.append(linea1)
#         else:
#             mapa__D.append(linea1)

#     # NO SE XQ ME QUITA 1 ESPACIO LA ESCRITURA,LO ARREGLO ABAJO
#     mapa__I[0][0] ='         ╔'
#     mapa__D[0][0] =' ═══'

#     # print(len(mapa__I[0]))
#     # for i in mapa__I:
#     #     print(i)
#     # print(len(mapa__D[0]))
#     # for i in mapa__D:
#     #     print(i)

#     mapa_cargado=[]
#     for i in range (len(mapa__I)):
#         mapa_cargado.append(mapa__I[i]+mapa__D[i]) 

#     print(len(mapa_cargado[0]))
#     for i in mapa_cargado:
#         print(i)
#     print(len(kasino.mapa[0]))
#     for i in kasino.mapa:
#         print(i)
    
# cargar()




    # pasar="X"
    # linea1=[]
    # trozo=""

    # for i in a[0]:
    #     if pasar=="X":
            
    #         borrar = ["[","'"]
    #         if i in borrar:
    #             pass
    #         elif i == "," or i == "]":
    #             linea1.append(trozo)
    #             trozo=""
    #             pasar="V"
    #         else:
    #             trozo+=i

    #     else:
    #         pasar="X"
    #         pass



    # print (linea1)
    # print(kasino.mapa[0])




