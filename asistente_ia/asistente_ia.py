import webbrowser
import pyttsx3
from datetime import datetime

# --- CONFIGURACIÓN DE VOZ MEJORADA ---
def hablar(texto):
    print(f"Salomon dice: {texto}")
    try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        
        # --- BUSCADOR DE RAÚL ---
        for voz in voices:
            # Buscamos "Raul" en el nombre de la voz
            if "Raul" in voz.name or "Microsoft Raul" in voz.name:
                engine.setProperty('voice', voz.id)
                break 
        # ------------------------

        engine.setProperty('rate', 175) # Un poco más rápido para que suene natural
        engine.setProperty('volume', 1.0)
        engine.say(texto)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"Error de audio: {e}")

def escuchar():
    print("\n--- 🧠 Salomon esperando orden (Escribe tu comando) ---")
    consulta = input("Tú: ").lower().strip()
    return consulta

# --- FUNCIÓN MAESTRA DE ARCHIVOS ---
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
                    for n in notas[-3:]: # Solo las últimas 3
                        hablar(n.strip())
                else:
                    hablar("No hay notas guardadas.")
    except FileNotFoundError:
        hablar("Aún no tienes una bitácora creada.")
    except Exception as error_tecnico:
        print(f"Error crítico: {error_tecnico}")

# --- CREAMOS LA FUNCIÓN TRAFICO ---

def abrir_trafico():
    hablar("Revisando el tráfico en Ciudad de México para los Uber.")
    webbrowser.open("https://www.google.com/maps/@19.4326,-99.1332,12z/data=!5m1!1e1")

# --- FUNCION SALUDO PERSONALIZADO ---

def saludo_personalizado(pedido_recibido): # <--- Aquí recibe el dato
    hora_actual = datetime.now().strftime('%H:%M')
    if 'buenos días' in pedido_recibido:
        hablar(f"Buenos días Jonathan, son las {hora_actual}. ¿En qué te puedo ayudar?")
    elif 'buenas tardes' in pedido_recibido:
        hablar(f"Buenas tardes Jonathan, son las {hora_actual}. ¿En qué te puedo ayudar?")
    elif 'buenas noches' in pedido_recibido:
        hablar(f"Buenas noches Jonathan, son las {hora_actual}. ¿En qué te puedo ayudar?")

# --- BUSQUEDA EN GOOGLE ---

def buscar_en_google(consulta):
    hablar(f"Buscando {consulta} en Google para ti.")
    # Formateamos el texto para que sea una URL válida
    url = f"https://www.google.com/search?q={consulta}"
    webbrowser.open(url)

# --- CICLO PRINCIPAL ---

if __name__ == "__main__":
    hablar("Hola Jonathan, sistema Salomon activado. ¿Qué dominaremos hoy?")
    
    while True:
        pedido = escuchar()

        if 'terminar' in pedido or 'adiós' in pedido or 'cerrar' in pedido:
            hablar("Entendido, cerrando sistemas. ¡Hasta pronto, Jonathan!")
            break
            
        elif 'quién eres' in pedido or 'quien eres' in pedido:
            hablar("Soy Salomon, tu asistente personal diseñado para dominar el código y potenciar tu ingeniería.")
            
        elif 'haki' in pedido:
            hablar("El Haki es una fuerza espiritual. ¡Sigue entrenando tu código para alcanzar el nivel de un Yon-ko!")

        elif 'abre youtube' in pedido:
            hablar("Abriendo YouTube, disfruta del contenido.")
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
            saludo_personalizado(pedido) # <--- Aquí le mandas el dato
                
        elif 'qué hora es' in pedido or 'hora' in pedido:
         hora_actual = datetime.now().strftime('%H:%M')
         hablar(f"Son las {hora_actual}, Jonathan. ¿Vas a revisar algo de la flota o prefieres estudiar?")

        elif 'modo estudio' in pedido:
            hablar("Activando modo estudio. Abriendo portal UTEL y GitHub. ¡A darle con todo, Ingeniero!")
            webbrowser.open("https://aula.utel.edu.mx/")
            webbrowser.open("https://github.com/jruizn-dev") # Tu perfil profesional

        # ... (otros comandos)

        elif 'anota' in pedido or 'escribe' in pedido:
            # Extraemos el mensaje (lo que sigue después de la palabra clave)
            nota = pedido.replace("anota", "").replace("escribe", "").strip()
            if nota:
                # LLAMADA A LA FUNCIÓN: Acción "escribir" y el texto
                manejar_archivo("escribir", nota)
            else:
                hablar("¿Qué quieres que anote en la bitácora?")

        elif 'lee las notas' in pedido or 'qué tengo anotado' in pedido:

            # LLAMADA A LA FUNCIÓN: Solo acción "leer"
            manejar_archivo("leer")

        elif 'busca' in pedido or 'qué es' in pedido:
            # Si dices "busca qué es un objeto en Java", Salomon buscará eso
            termino = pedido.replace("busca", "").replace("qué es", "").strip()
            if termino:
                buscar_en_google(termino)
            else:
                hablar("¿Qué término te gustaría que investigue?")

        else:
            print(f"Comando '{pedido}' no reconocido.")
            # Opcional: puedes hacer que Salomon diga que no entendió

