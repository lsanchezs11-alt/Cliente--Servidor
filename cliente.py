from network.conexion_cliente import conectar_servidor

def iniciar_cliente():
    print("Cliente TCP iniciado")
    
    while True:
        mensaje = input("Escribe un mensaje: ")
        if mensaje.lower() == "salir":
            break
        
        respuesta = conectar_servidor(mensaje)
        print("Respuesta del servidor:", respuesta)
