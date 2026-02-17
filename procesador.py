def procesar_mensaje(mensaje):
    if mensaje == "":
        return "Mensaje vacío"
    
    return f"Servidor recibió: {mensaje.upper()}"
