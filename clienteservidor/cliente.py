import grpc
import mail_pb2
import mail_pb2_grpc
import tkinter
from tkinter import *




#tkinter.Label(ventana, text="Registrar").grid(row=0)
#tkinter.Label(ventana, text="Iniciar sesion").grid(row=1)
#label1.pack(side=tkinter.LEFT)
#ventana.mainloop()




def run2():
    
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = mail_pb2_grpc.CorreoStub(channel)

        ventana=tkinter.Tk()
        ventana.geometry("400x200")
        
        
        #tkinter.Label(ventana, text="Registrar").grid(row=0)
        #tkinter.Label(ventana, text="Iniciar sesion").grid(row=1)

        #app=Window(ventana,stub)
        tkinter.Button(ventana,text="Registrar",width=25,command=lambda: registro(ventana)).grid(row=0,column=1)
        tkinter.Button(ventana,text="Iniciar sesion",width=25,command=lambda: cambio_Login(ventana)).grid(row=1,column=1)
        def cambio_Login(ventana):
            ventana.destroy()
            ventana1=tkinter.Tk()
            ventana1.geometry("400x200")
            tkinter.Label(ventana1, text="Usuario").grid(row=0,column=0)
            tkinter.Label(ventana1, text="Contrasena").grid(row=1,column=0)
            e1 = Entry(ventana1)
            e2= Entry(ventana1)
            e1.grid(row=0,column=1)
            e2.grid(row=1,column=1)
            tkinter.Button(ventana1,text="Login",width=25,
                           command=lambda: login(ventana1,e1.get(),e2.get())).grid(row=2,column=0)
            tkinter.Button(ventana1,text="Register",width=25,
                           command=lambda: registro(ventana1)).grid(row=5,column=2)
            ventana1.mainloop()
            
           #
            #
            #ventana.mainloop()
        def registro(ventana):
            ventana.destroy()
            ventana1=tkinter.Tk()
            ventana1.geometry("400x200")
            tkinter.Label(ventana1, text="Usuario").grid(row=0,column=0)
            tkinter.Label(ventana1, text="Contrasena").grid(row=1,column=0)
            e1 = Entry(ventana1)
            e2= Entry(ventana1)
            e1.grid(row=0,column=1)
            e2.grid(row=1,column=1)
            tkinter.Button(ventana1,text="Registrar",width=25,
                           command=lambda: registrar(ventana1,e1.get(),e2.get())).grid(row=2,column=0)
            ventana1.mainloop()

        def registrar(ventana1,texto1,texto2):#int(texto2)
            aux=stub.RegistrarUsuario(mail_pb2.RegistroUsuario(nombre=texto1 ,contra=int(texto2)))
            if aux.success:
                print("se pudo")
                tkinter.Label(ventana1, text="Se pudo registrar").grid(row=4,column=0)
                tkinter.Button(ventana1,text="Iniciar sesion",width=25,
                               command=lambda: cambio_Login(ventana1)).grid(row=5,column=1)
            else:
                print("no se pudo")
                registro(ventana1)

        def login(ventana1,texto1,texto2):
            aux=stub.Login_Usuario(mail_pb2.LoginUsuario(nombre=texto1,contra=int(texto2)))
            if aux.success:
                print("se pudo")
                tkinter.Label(ventana1, text="Se pudo loggear").grid(row=4,column=0)
                inicio(ventana1,texto1)
                
            else:
                print("no se pudo")
                tkinter.Label(ventana1, text="No pudo loggear").grid(row=4,column=0)
                
            
        def inicio(ventana,texto1):
            ventana.destroy()
            ventana2=tkinter.Tk()
            ventana2.geometry("400x200")
            tkinter.Label(ventana2, text="Escoga accion").grid(row=0,column=0)
            tkinter.Button(ventana2,text="ENVIAR",width=25,
                           command= lambda: enviar(ventana2,texto1)).grid(row=1,column=1)
            tkinter.Button(ventana2,text="BANDJEA SALIDA",width=25).grid(row=2,column=1)
            tkinter.Button(ventana2,text="BANDEJA ENTRADA",width=25,
                           command= lambda: leer(ventana2,texto1)).grid(row=3,column=1)
            tkinter.Button(ventana2,text="BORRAR",width=25).grid(row=4,column=1)
    
        def leer(ventana,usuario):#usuario es quine soy
            dic={}#para gardar nombre d mails con su id
            ventana.destroy()
            ventana4=tkinter.Tk()
            ventana4.geometry("400x200")
            tkinter.Label(ventana4, text="Bandeja entrada").grid(row=0,column=0)
            tkinter.Label(ventana4, text="Tienes estos mails: ").grid(row=1,column=0)
            i=2
            xAlex=stub.Leer_Correo(mail_pb2.Usuario(nombre=usuario))
            dic={}
            for mail in xAlex:
                dic[mail.id]=(mail.nombreRemitente,mail.contenido,mail.tema)
                print("Nombre Destinatario: ", mail.nombreDest, "Contenido: ", mail.contenido,
                "Nombre remitente: ", mail.nombreRemitente," Estado ",mail.estado,
                    " Tema: ", mail.tema, " ID: ",mail.id)
                tkinter.Label(ventana4, text=mail.id).grid(row=i,column=1)
                
                i+=1
            
            e1=Entry(ventana4)
            e1.grid(row=1,column=1)
            e2=Entry(ventana4)
            e2.grid(row=6,column=0)
            tkinter.Button(ventana4,text="Consulta",width=25,
                               command= lambda: leer2(ventana4,e1.get(),dic,usuario)).grid(row=1,column=2)
            tkinter.Button(ventana4,text="Borrar",width=25,
                               command= lambda: borrar(ventana4,e2.get(),dic,usuario)).grid(row=5,column=0)
            tkinter.Button(ventana4,text="Regresar",width=25,
                               command= lambda: inicio(ventana4,usuario)).grid(row=0,column=2)
            def borrar(ventana,idd,dic,usuario):
                print("borrar")
                stub.borrar(mail_pb2.Usuario(nombre=usuario,id=int(idd)))
                inicio(ventana,usuario)
            
            
            def leer2(ventana4,idd,dic,usuario):
                ventana4.destroy()
                #debo mostrar mail
                ventana5=tkinter.Tk()
                ventana5.geometry("400x200")
                a=""
                b=""
                c=""
                for key,value in dic.items():
                    print(key,value)
                    if key==int(idd):
                        a=value[0]
                        b=value[1]
                        c=value[2]
                        print(value[0],value[1],value[2])
                tkinter.Label(ventana5, text="Tema").grid(row=0,column=0)
                tkinter.Label(ventana5, text="Remitente ").grid(row=1,column=0)
                tkinter.Label(ventana5, text="Contenido").grid(row=2,column=0)
                tkinter.Label(ventana5, text=a).grid(row=0,column=1)
                tkinter.Label(ventana5, text=b).grid(row=1,column=1)
                tkinter.Label(ventana5, text=c).grid(row=2,column=1)
                tkinter.Button(ventana5,text="Regresar",width=25,
                               command= lambda: inicio(ventana5,usuario)).grid(row=0,column=2)
                #debo actualizar (enviar rpc con id del que se leyo) y el usuario
                stub.actualizar(mail_pb2.Usuario(nombre=usuario,id=int(idd)))
                print("leer2")
            
        def enviar(ventana,usuario):
            ventana.destroy()
            ventana3=tkinter.Tk()
            ventana3.geometry("400x200")
            tkinter.Label(ventana3, text="Llene campos").grid(row=0,column=0)

            tkinter.Label(ventana3, text="Destinatario").grid(row=1,column=0)
            e1 = Entry(ventana3)
            tkinter.Label(ventana3, text="Contenido").grid(row=2,column=0)
            e2= Entry(ventana3)
            tkinter.Label(ventana3, text="Remitente").grid(row=3,column=0)
            e3=Entry(ventana3)
            tkinter.Label(ventana3, text="Tema").grid(row=4,column=0)
            e4=Entry(ventana3)
        
            e1.grid(row=1,column=1)
            e2.grid(row=2,column=1)
            e3.grid(row=3,column=1)
            e4.grid(row=4,column=1)
            tkinter.Button(ventana3,text="ENVIAR",width=25,
                           command= lambda: envia(ventana3,e1.get(),e2.get(),
                                                   e3.get(),e4.get())).grid(row=5,column=1)
            tkinter.Button(ventana3,text="Regresar",width=25,
                               command= lambda: inicio(ventana3,usuario)).grid(row=0,column=2)
            def envia(ventana,texto1,texto2,texto3,texto4):
                aux=stub.Enviar_Correo(mail_pb2.Correos(nombreDest=texto1,contenido=texto2,nombreRemitente=texto3,
                                                tema=texto4))
                if aux.success:
                    print("se pudo")
                    tkinter.Label(ventana3, text="Se pudo enviar").grid(row=6,column=0)
                    #inicio(ventana3)
                else:
                    print("no se pudo enbviar")
                    tkinter.Label(ventana3, text="No se pudo enviar").grid(row=6,column=0)

            #ventana3.mainloop()

            
            
            


        ventana.mainloop()
            
        
       # m=actualizar(xAlex)
        #print("espaciouf  ")

        #for mail in m:
         #   print("Nombre Destinatarioo: ", mail.nombreDest, "Contenido: ", mail.contenido,
          #   "Nombre remitente: ", mail.nombreRemitente," Estado ",mail.estado,
           #     " Tema: ", mail.tema, " ID: ",mail.id)

       #for mail in xAlex:
       #la atualizacion la llevo a cabo del lado del cliente
       #cambiando su atributo estado a True
        #otra opcion es que actualizar bandeja no envie un stream de correos sino, el nombre
        #dele propietario de la bandeja y las id de los mails que leyo
        #y ya el servidor se emcarga de que esos mails su estado sea True      
       # stub.actualizar_bandeja(m)
def run3():
    print("Intentando decir hola")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = mail_pb2_grpc.CorreoStub(channel)
        #aqui estaba diHola
        respuesta = stub.AuthenticationRequest(mail_pb2.HelloRequest(name="Octavio",lugar="mexico",anio=1985,contra=13))
        print("El cliente recibio", respuesta.message)
        stub.RegistrarUsuario(mail_pb2.RegistroUsuario(nombre="aaa",contra=1001))      
def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = mail_pb2_grpc.CorreoStub(channel)
        print("Intentando registrar")
    
        stub.RegistrarUsuario(mail_pb2.RegistroUsuario(nombre="Pedro22", contra=1010))
        stub.RegistrarUsuario(mail_pb2.RegistroUsuario(nombre="Alex55", contra=1001))
        stub.RegistrarUsuario(mail_pb2.RegistroUsuario(nombre="Elisa", contra=1010))
        stub.RegistrarUsuario(mail_pb2.RegistroUsuario(nombre="James", contra=1000))
        stub.RegistrarUsuario(mail_pb2.RegistroUsuario(nombre="Elisa", contra=1100))
        stub.RegistrarUsuario(mail_pb2.RegistroUsuario(nombre="Pam", contra=1110))
        stub.RegistrarUsuario(mail_pb2.RegistroUsuario(nombre="Andy13", contra=1100))
        stub.Login_Usuario(mail_pb2.LoginUsuario(nombre="Alex55",contra=1001))
        stub.Login_Usuario(mail_pb2.LoginUsuario(nombre="Alex55",contra=1011))
        stub.Login_Usuario(mail_pb2.LoginUsuario(nombre="Alex",contra=1001))
        stub.Enviar_Correo(mail_pb2.Correos(nombreDest="Alex55",
                                                contenido="este es un mail",nombreRemitente="Pedro22",
                                                tema="urgente"))
        stub.Enviar_Correo(mail_pb2.Correos(nombreDest="Alex55",
                                                contenido="este es un mail2",nombreRemitente="Elisa",
                                                tema="otro tema"))
        stub.Enviar_Correo(mail_pb2.Correos(nombreDest="Alex55",
                                                contenido="este es un mail3",nombreRemitente="James",
                                                tema="casual"))
        stub.Enviar_Correo(mail_pb2.Correos(nombreDest="Alex55",
                                                contenido="este es un mail de james a alex",
                                                nombreRemitente="James",tema="casual"))
        stub.Enviar_Correo(mail_pb2.Correos(nombreDest="Elisa",
                                                contenido="este es un mail de james a Elisa",
                                                nombreRemitente="James",tema="casual"))
        stub.Enviar_Correo(mail_pb2.Correos(nombreDest="Alex",
                                                contenido="este es un mail2",nombreRemitente="Elisa",tema="nopasa"))
        stub.Enviar_Correo(mail_pb2.Correos(nombreDest="Alex55",
                                                contenido="este es un mail3",nombreRemitente="Andy13",
                                                tema="trabajo"))
        xAlex=stub.Leer_Correo(mail_pb2.Usuario(nombre="Alex55"))

        
        for mail in xAlex:
            print("Nombre Destinatario: ", mail.nombreDest, "Contenido: ", mail.contenido,
             "Nombre remitente: ", mail.nombreRemitente," Estado ",mail.estado,
                " Tema: ", mail.tema, " ID: ",mail.id)
        xAlex2=stub.actualizar(mail_pb2.Usuario(nombre="Alex55",id=2))
        for mail in xAlex2:
            print("Nombre Destinatario0: ", mail.nombreDest, "Contenido: ", mail.contenido,
             "Nombre remitente: ", mail.nombreRemitente," Estado ",mail.estado,
                " Tema: ", mail.tema, " ID: ",mail.id)
        xAlex2=stub.actualizar(mail_pb2.Usuario(nombre="Alex55",id=3))
        for mail in xAlex2:
            print("Nombre Dstinatario0o: ", mail.nombreDest, "Contenido: ", mail.contenido,
             "Nombre remitente: ", mail.nombreRemitente," Estado ",mail.estado,
                " Tema: ", mail.tema, " ID: ",mail.id)
        xAlex2=stub.borrar(mail_pb2.Usuario(nombre="Alex55",id=3))
        for mail in xAlex2:
            print("Nombre Dstinatarioo: ", mail.nombreDest, "Contenido: ", mail.contenido,
             "Nombre remitente: ", mail.nombreRemitente," Estado ",mail.estado,
                " Tema: ", mail.tema, " ID: ",mail.id)
        xAlex2=stub.bandejaSalida(mail_pb2.Usuario(nombre="James"))
        for mail in xAlex2:
            print("bandeja de salida de James")
            print("Nombre Remitente: ", mail.nombreDest, "Contenido: ", mail.contenido,
             "Nombre dest: ", mail.nombreRemitente," Estado ",mail.estado,
                " Tema: ", mail.tema, " ID: ",mail.id)


if __name__ == "__main__":
    #run3()
    
    run2()
    #run()
    #t1 = threading.Thread(target=run)
    #t2 = threading.Thread(target=run)
    #t3 = threading.Thread(target=run1)
    #t4 = threading.Thread(target=run1)
    #t5 = threading.Thread(target=run1)
    #t6 = threading.Thread(target=run1)

    #t1.start()
    #t2.start()
    #t3.start()
    #t4.start()
    #t5.start()
    #t6.start()
    