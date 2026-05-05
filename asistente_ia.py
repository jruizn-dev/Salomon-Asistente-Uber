import speech_recognition as sr
import asyncio
import edge_tts
import os
import webbrowser
from datetime import datetime

# --- FUNCIONES DE VOZ (ASÍNCRONAS) ---
def hablar(texto):
    print(f"Salomon dice: {texto}")
    # Usamos asyncio.run para ejecutar la función asíncrona desde código normal
    asyncio.run(hablar_async(texto))

async def hablar_async(texto):
    voz = "es-MX-JorgeNeural" 
    archivo_salida = "salida.mp3"
    
    # Generamos el archivo
    comunicador = edge_tts.Communicate(texto, voz)
    await comunicador.save(archivo_salida)
    
    # Reproducimos el archivo
    os.system(f"start {archivo_salida}")

# --- FUNCIÓN DE ENTRADA (MODO TEXTO) ---
def escuchar():
    r = sr.Recognizer()
    
    # --- INTENTO DE ESCUCHA (VOZ) ---
    try:
        with sr.Microphone() as source:
            print("\n👂 Salomón escuchando (o escribe tu orden)...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            # Damos 4 segundos para detectar voz
            audio = r.listen(source, timeout=4, phrase_time_limit=10)
            
        print("🤖 Procesando audio...")
        consulta = r.recognize_google(audio, language="es-MX")
        print(f"Salomón entendió: {consulta}")
        return consulta.lower()
        
    except Exception as e:
        # --- FALLBACK AL TECLADO ---
        # Si falla el micro, el timeout, o el reconocimiento, venimos aquí
        print("\n⚠️ No detecté voz (o hubo error). Cambiando a modo texto.")
        consulta = input("Tú (Teclado): ").lower().strip()
        return consulta

# --- LÓGICA DE COMANDOS ---
def procesar_comando(pedido):
    if 'terminar' in pedido or 'adiós' in pedido or 'cerrar' in pedido or 'salir' in pedido:
        return False
        
    elif 'quién eres' in pedido or 'quien eres' in pedido:
        hablar("Soy Salomon, tu asistente personal.")
        
    elif 'haki' in pedido:
        hablar("El Haki es una fuerza espiritual. ¡Sigue entrenando!")

    elif 'abre youtube' in pedido:
        webbrowser.open("https://www.youtube.com")

    elif 'mi universidad' in pedido:
        hablar("Abriendo el portal de la UTEL. ¡A darle con todo al estudio!")
        webbrowser.open("https://aula.utel.edu.mx/")
            
    elif 'mi github' in pedido:
        hablar("Abriendo tu repositorio en GitHub. Es hora de subir ese código.")
        webbrowser.open("https://github.com/")

    elif 'tráfico' in pedido or 'dame el trafico' in pedido:
        abrir_trafico()

    elif 'buenos días' in pedido or 'buenas tardes' in pedido or 'buenas noches' in pedido:
        saludo_personalizado(pedido)
                
    elif 'qué hora es' in pedido or 'hora' in pedido:
        hora_actual = datetime.now().strftime('%H:%M')
        hablar(f"Son las {hora_actual}, Jonathan. ¿Vas a revisar algo de la flota o prefieres estudiar?")

    elif 'modo estudio' in pedido:
        hablar("Activando modo estudio. Abriendo portal UTEL y GitHub. ¡A darle con todo, Ingeniero!")
        webbrowser.open("https://aula.utel.edu.mx/")
        webbrowser.open("https://github.com/jruizn-dev")

    elif 'anota' in pedido or 'escribe' in pedido:
        nota = pedido.replace("anota", "").replace("escribe", "").strip()
        if nota:
            manejar_archivo("escribir", nota)
        else:
            hablar("¿Qué quieres que anote en la bitácora?")

    elif 'lee las notas' in pedido or 'qué tengo anotado' in pedido:
        manejar_archivo("leer")

    elif 'ingresos del día' in pedido or 'cuales son los ingresos del día' in pedido:
        calcular_ganancia_uber()

    elif 'busca' in pedido or 'qué es' in pedido:
        termino = pedido.replace("busca", "").replace("qué es", "").strip()
        if termino:
            buscar_en_google(termino)
        else:
            hablar("¿Qué término te gustaría que investigue?")


    # Ejemplo de lógica para añadir a procesar_comando
    elif 'modo teclado' in pedido:
       hablar("Cambiando a modo teclado. Escribe tus órdenes.")
       return "teclado" # Retornamos un estado

    elif 'modo voz' in pedido:
       hablar("Regresando a modo voz.")
       return "voz"

    else:
        with open("pendientes.txt", "a") as f:
            f.write(pedido + "\n")
        hablar("Eso aún no lo tengo programado, pero lo he anotado en mi lista de aprendizaje.")
    
    return True

def obtener_entrada(modo_actual):
    if modo_actual == "voz":
        return escuchar_con_voz() # Tu función original con el try/except
    else:
        return input("Tú (Teclado): ")

# --- FUNCIONES DE APOYO (MAESTRA) ---
def manejar_archivo(accion, texto=""):
    nombre_archivo = "bitacora_salomon.txt"
    try:
        if accion == "escribir":
            with open(nombre_archivo, "a", encoding="utf-8") as f:
                fecha = datetime.now().strftime('%d/%m/%Y %H:%M')
                f.write(f"[{fecha}] {texto}\n")
            hablar(f"Anotado en la bitácora: {texto}")
        elif accion == "leer":
            with open(nombre_archivo, "r", encoding="utf-8") as f:
                notas = f.readlines()
                if notas:
                    hablar("Estas son las últimas notas:")
                    for n in notas[-3:]:
                        hablar(n.strip())
                else:
                    hablar("No hay notas guardadas.")
    except Exception as e:
        print(f"Error en bitácora: {e}")

def abrir_trafico():
    hablar("Revisando el tráfico en Ciudad de México para los Uber.")
    webbrowser.open("https://www.google.com/maps/@19.4326,-99.1332,12z/data=!5m1!1e1")

def saludo_personalizado(pedido_recibido):
    hora_actual = datetime.now().strftime('%H:%M')
    if 'buenos días' in pedido_recibido:
        saludo = "Buenos días"
    elif 'buenas tardes' in pedido_recibido:
        saludo = "Buenas tardes"
    else:
        saludo = "Buenas noches"
    hablar(f"{saludo} Jonathan, son las {hora_actual}. ¿En qué te puedo ayudar?")

def buscar_en_google(consulta):
    hablar(f"Buscando {consulta} en Google para ti.")
    url = f"https://www.google.com/search?q={consulta}"
    webbrowser.open(url)

def calcular_ganancia_uber():
    try:
        hablar("¿Cuál es la meta de ingresos para hoy, Jonathan?")
        meta_diaria = float(input("Ingresa tu meta del día: "))
        hablar("¿Cuánto fue el ingreso total del día en la aplicación?")
        ingreso_bruto = float(input("Ingresa el monto total: "))
        hablar("¿Cuánto gastaste en gasolina hoy?")
        gasolina = float(input("Ingresa el gasto de gasolina: "))
        
        comision_uber = ingreso_bruto * 0.25
        ganancia_neta = ingreso_bruto - comision_uber - gasolina
        
        if ganancia_neta >= meta_diaria:
            sobrante = ganancia_neta - meta_diaria
            hablar(f"¡Excelente! Superaste la meta por {sobrante:.2f} pesos.")
        else:
            faltante = meta_diaria - ganancia_neta
            hablar(f"Buen esfuerzo, pero faltaron {faltante:.2f} pesos.")
    except ValueError:
        hablar("Error: Por favor, asegúrate de ingresar solo números.")

# --- CICLO PRINCIPAL ---
if __name__ == "__main__":
    hablar("Hola Jonathan, sistema Salomon activado. ¿Qué dominaremos hoy?")
    while True:
        pedido = escuchar()
        continuar = procesar_comando(pedido)
        if not continuar:
            hablar("Cerrando sistemas. ¡Hasta pronto!")
            break
