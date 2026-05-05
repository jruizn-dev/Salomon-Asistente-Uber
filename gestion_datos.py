# gestion_datos.py

def guardar_historial(datos):
    # Abrimos el archivo en modo 'a' (append) para no borrar lo anterior
    with open("historial_finanzas.txt", "a") as archivo:
        archivo.write(datos + "\n")
