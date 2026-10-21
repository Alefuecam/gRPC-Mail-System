from concurrent import futures
import json
from venv import logger
import grpc
import mail_pb2_grpc #contenedor, donde despliego servicio
import mail_pb2
import pickle
import Guardador        
my=[(1,2),(3.78,9.56),("study","alex")]


class Proyecto2(mail_pb2_grpc.CorreoServicer):

    folioUsuarios=0
    folioCorreos=0

    db={}
    saturacion={}
    bandejaSalida={}
    bandejaSal={}
    usuarios={}
    cantidadMail={} #este me va aservir para saber si alguien ya tiene 5 mails en bandeja
    bandeja={} # este diccionario tendra de llave el nombre de un destinatario y una lista de mails como valor
    #esta lista tendra el nombre del remitente y el contenido
    abc={"uno":[("tal",2)],"dos":[("tal2",3),("tal22",4)]}
    with open('filename.pickle', 'rb') as handle:
        db = pickle.load(handle)
    print(db['usuarios'])
    print(db['saturacion'])
    print(db['cantidadMail'])
    print(db['bandeja'])
    
    def checkKey(dic,key):
        if key in dic.keys():
            return True
        else:
            return False

    def RegistrarUsuario(self, request, context):
        lista1=[("tan",2)]
        lista=[]
        lista.append(("tal3",66))
        Proyecto2.abc["tres"]=lista
        Proyecto2.abc.get("uno").append(("asd",55))
        Proyecto2.abc["dos"]=lista1
        with open('filename.pickle', 'rb') as handle:
            Proyecto2.db = pickle.load(handle)
        Proyecto2.usuarios=Proyecto2.db['usuarios']
        print(Proyecto2.usuarios)
        print(Proyecto2.db['usuarios'])
        #en caso de que servidor se caiga para que haya persistencia
        #accedo a file siempre


        #for key,value in Proyecto2.abc.items():
         #   print(key,value)
        if Proyecto2.checkKey(Proyecto2.usuarios,request.nombre):#ya existe
           print("ya existe ese usuario cambialo")
           return mail_pb2.Status(success=False)
        else:
            Proyecto2.usuarios[request.nombre]= request.contra
            Proyecto2.cantidadMail[request.nombre]=0 #inicializo numero de mails a 0
            Proyecto2.saturacion[request.nombre]=0
            Proyecto2.db['cantidadMail']=Proyecto2.cantidadMail
            Proyecto2.db['usuarios']=Proyecto2.usuarios
            Proyecto2.db['saturacion']=Proyecto2.saturacion

            listaTupla=[]
            listaTupla.append(("inicio","zero",False,"tema",-1))
            #listaTupla1=[]
            #listaTupla1.append(("inicio","zero",False,"tema",-1))
            Proyecto2.bandeja[request.nombre]=listaTupla
            Proyecto2.db['bandeja']=Proyecto2.bandeja
            #Proyecto2.bandejaSal[request.nombre]=listaTupla
            #Proyecto2.bandejaSalida[request.nombre]=listaTupla1
            #for usuario in Proyecto2.usuarios.values(): 
             #   print(len( Proyecto2.usuarios.values()), type(usuario), usuario)
            for key,value in Proyecto2.bandeja.items():
                print("bandeja entrada de todos")
                print(key,value)
            with open('filename.pickle', 'wb') as handle:
                pickle.dump(Proyecto2.db, handle, protocol=pickle.HIGHEST_PROTOCOL)
            
            return mail_pb2.Status(success=True)
            
    #para el login busco el nombre de usuario en el diccionario y veo si coincide con contrasena
    def Login_Usuario(self,request,context):
        with open('filename.pickle', 'rb') as handle:
            Proyecto2.db = pickle.load(handle)
            Proyecto2.usuarios=Proyecto2.db['usuarios']
        a=request.nombre
        b=Proyecto2.usuarios.get(a)
        #for key,value in Proyecto2.usuarios.items():
         #   print(key,value)
        if b==request.contra:
            print("se pudo logear")
            return mail_pb2.Status(success=True)
        else:
            print("contra incorrcta o usuario incorrecto")
            return mail_pb2.Status(success=False)
    def Enviar_Correo(self,request,context):
        with open('filename.pickle', 'rb') as handle:
            Proyecto2.db = pickle.load(handle)
        Proyecto2.usuarios=Proyecto2.db['usuarios']
        print("usuariosdb",Proyecto2.db['usuarios'])
        print("usuarioslocal",Proyecto2.usuarios)
        Proyecto2.cantidadMail=Proyecto2.db['cantidadMail']
        Proyecto2.saturacion=Proyecto2.db['saturacion']
        print("saturaciondb",Proyecto2.db['saturacion'])
        print("saturacionlocal",Proyecto2.saturacion)
        print("cantidaddb",Proyecto2.db['cantidadMail'])
        print("cantidadlocal",Proyecto2.cantidadMail)
        #checo si destinatario existe
        Proyecto2.bandeja=Proyecto2.db['bandeja']
        if Proyecto2.checkKey(Proyecto2.usuarios,request.nombreDest):
            print("entre a primer if")
            Proyecto2.cantidadMail[request.nombreDest]+=1 #aumento mails en bandeja
            print("entre los dos")
            Proyecto2.saturacion[request.nombreRemitente]+=1
            print('sigoaqui')
            Proyecto2.db['cantidadMail']=Proyecto2.cantidadMail
            Proyecto2.db['saturacion']=Proyecto2.saturacion
            with open('filename.pickle', 'wb') as handle:
                pickle.dump(Proyecto2.db, handle, protocol=pickle.HIGHEST_PROTOCOL)
            #si llego a 6 paro porque ya esta lleno
            #en este caso debo avisar a emisor que fallo
            if Proyecto2.saturacion[request.nombreRemitente]>5:
                print("bandeja salida llena")
                return mail_pb2.Status(success=False)
            if Proyecto2.cantidadMail[request.nombreDest]>5:
                print("bandeja entrada llena")
                return mail_pb2.Status(success=False)
            print("sigo en primer if")
            Proyecto2.folioCorreos+=1
            Proyecto2.bandeja[request.nombreDest].append((request.nombreRemitente,request.contenido,False,
                                                          request.tema,Proyecto2.folioCorreos))
            #Proyecto2.bandejaSal[request.nombreRemitente].append((request.nombreDest,request.contenido,
             #                                                  False, request.tema,Proyecto2.folioCorreos))
            
            print("bandeja de entrada")
            for key,value in Proyecto2.bandeja.items(): 
                print(key,value)
            print("bandeja de salida")    
            #for key,value in Proyecto2.bandejaSal.items():
             #   print(key,value)
            
            #Proyecto2.db['usuarios']=Proyecto2.usuarios
            
            Proyecto2.db['bandeja']=Proyecto2.bandeja
            with open('filename.pickle', 'wb') as handle:
                pickle.dump(Proyecto2.db, handle, protocol=pickle.HIGHEST_PROTOCOL)
            return mail_pb2.Status(success=True)
        else:
            print("no existe destinatario")
            return  mail_pb2.Status(success=False)
    def Leer_Correo(self, request, context): # regresa listado de mails (bandeja), recibe Usuario
        with open('filename.pickle', 'rb') as handle:
            Proyecto2.db = pickle.load(handle)
        Proyecto2.bandeja=Proyecto2.db['bandeja']
        lista=Proyecto2.bandeja[request.nombre] #lista es una lista de tuplas
        aux={}
        inc=1
        for x,y,z,w,v in lista:
            aux[inc]=mail_pb2.Correos(nombreDest=request.nombre,contenido=y,nombreRemitente=x,estado=z,
                                 tema=w,id=v)
            inc+=1
            #print(x,y,z,w,v)
        #print(lista[1][0],len(lista))
        for tal in aux.values():
            yield tal
    #funcion actualizar recibe nombre de usuario e ID, asi sabes que mail leyo
    #(el id corresponde a mail que leyo), de esta forma puedo cambiar en el diccionario bandeja
    #el estado de dicho mail a True
    #el nombre de usuario es la llave de mi dicccionario, o sea la bandeja de ese usuario
    
    def actualizar(self, request, context):
        lista=Proyecto2.bandeja[request.nombre] #lista es una lista de tuplas
        i=0
        for x,y,z,w,v in lista:
            if v==request.id:
                Proyecto2.bandeja[request.nombre][i]=(x,y,True,w,v)
            i+=1
        for key,value in Proyecto2.bandeja.items():
                print(key,value)
        #sig parte es solo para regersar bandeja (stream Correos)
        aux={}
        inc=1
        for x,y,z,w,v in lista:
            aux[inc]=mail_pb2.Correos(nombreDest=request.nombre,contenido=y,nombreRemitente=x,estado=z,
                                 tema=w,id=v)
            inc+=1
            #print(x,y,z,w,v)
        
        for tal in aux.values():
            yield tal    
    def borrar(self, request, context):
        #por alguna razon no me deja borrar elemento tuple de lista, se que tuple es inmitable
        #pero la lista no lo es
        #voy a tener que reemplzar lista entera
        with open('filename.pickle', 'rb') as handle:
            Proyecto2.db = pickle.load(handle)
        Proyecto2.bandeja=Proyecto2.db['bandeja']
        lista=Proyecto2.bandeja[request.nombre] #lista es una lista de tuplas
        listaAux=[]
        i=0
        print("request id",request.id)
        for x,y,z,w,v in lista:
            
            if v!=request.id:
                #print(v)
                listaAux.append((x,y,z,w,v))
                
        Proyecto2.bandeja[request.nombre]=listaAux
        Proyecto2.db['bandeja']=Proyecto2.bandeja
        with open('filename.pickle', 'wb') as handle:
            pickle.dump(Proyecto2.db, handle, protocol=pickle.HIGHEST_PROTOCOL)
        for key,value in Proyecto2.bandeja.items():
                print(key,value)
        #sig parte es solo para regersar bandeja (stream Correos)
        aux={}
        inc=1
        for x,y,z,w,v in listaAux:
            aux[inc]=mail_pb2.Correos(nombreDest=request.nombre,contenido=y,nombreRemitente=x,estado=z,
                                 tema=w,id=v)
            inc+=1
            #print(x,y,z,w,v)
        
        for tal in aux.values():
            yield tal

    def bandejaSalida(self,request,context):
        lista=Proyecto2.bandejaSal[request.nombre] #lista es una lista de tuplas
        aux={}
        inc=1
        for x,y,z,w,v in lista:
            aux[inc]=mail_pb2.Correos(nombreDest=request.nombre,contenido=y,nombreRemitente=x,estado=z,
                                 tema=w,id=v)
            inc+=1
            #print(x,y,z,w,v)
        #print(lista[1][0],len(lista))
        for tal in aux.values():
            yield tal
        
    #la funcion actualizar bandeja desempaca los correos y actualiza la bandeja,
    #esto es para saber si ya se leyo algun correo
    #puedo borrar la llave del diccionario bandeja y la vuelvo a llenar
    def actualizar_bandeja(self,requestIterator,context):
        bandera=True
        aux=0
        listaTupla=[]
        listaTupla.append(("inicio","zero",False,"tema","id"))
         #la bandeja son mails de disitos usuarios al
        #mismo destinatario, por eso el nombre del destinatario
        #es el propitario de esa bandeja y usaremos su nombre para borrar esa llave del dicc
        #y poder acralizarlo despeues
        for mail in requestIterator:
            if bandera==True:
                 del Proyecto2.bandeja[mail.nombreDest]
                 bandera=False
                 aux=mail.nombreDest
                 Proyecto2.bandeja[aux]=listaTupla
            Proyecto2.bandeja[aux].append((mail.nombreRemitente,mail.contenido,mail.estado,
                                           mail.tema,mail.id))
        print("bandeja en actualizar")    
        for key,value in Proyecto2.bandeja.items():
                print(key,value)

        return  mail_pb2.Status(success=False)
        

    
         


def run():
    puerto="50051"
    servidor= grpc.server(futures.ThreadPoolExecutor(max_workers=10)) #10 hilos 
    mail_pb2_grpc.add_CorreoServicer_to_server(Proyecto2(),servidor) #vinculo entre contenedor y clase que definimos
    servidor.add_insecure_port("[::]:"+puerto) #simbolo es local host
    print("arrnacando servidor")
    servidor.start()
    #para asegurarame de que no muera luego luego
    servidor.wait_for_termination()
if __name__=="__main__":
    run()
    #ofrece_servicios()

    #creo un diccionario de nombre:lista, donde lista son mails
    #cuando envio mail uso el nombreDest como llave y un append
    #Asignar_Mail es el que vincula al remitente y destinatario
    #enviar mail puede acceder al dest y usar append en dicha lista