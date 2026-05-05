
def saludo_personalizado(pedido_recibido):
    hora_actual = datetime.now().strftime('%H:%M')
    # Identificamos el saludo base
    if 'buenos días' in pedido_recibido:
        saludo = "Buenos días"
    elif 'buenas tardes' in pedido_recibido:
        saludo = "Buenas tardes"
    else:
        saludo = "Buenas noches"
    
    hablar(f"{saludo} Jonathan, son las {hora_actual}. ¿En qué te puedo ayudar?")

def calcular_ganancia_uber():
    try:
        # 1. Nueva entrada: Metas dinámicas
        hablar("¿Cuál es la meta de ingresos para hoy, Jonathan?")
        meta_diaria = float(input("Ingresa tu meta del día: "))
        
        hablar("¿Cuánto fue el ingreso total del día en la aplicación?")
        ingreso_bruto = float(input("Ingresa el monto total: "))
        
        hablar("¿Cuánto gastaste en gasolina hoy?")
        gasolina = float(input("Ingresa el gasto de gasolina: "))
        
        # 2. Cálculos
        comision_uber = ingreso_bruto * 0.25
        ganancia_neta = ingreso_bruto - comision_uber - gasolina
        
        # 3. Lógica de decisión comparando con la variable dinámica
        if ganancia_neta >= meta_diaria:
            sobrante = ganancia_neta - meta_diaria
            hablar(f"¡Excelente! Superaste la meta de {meta_diaria} por {sobrante:.2f} pesos.")
        else:
            faltante = meta_diaria - ganancia_neta
            hablar(f"Buen esfuerzo, pero faltaron {faltante:.2f} pesos para alcanzar tu meta de {meta_diaria}.")
            
    except ValueError:
        hablar("Error: Por favor, asegúrate de ingresar solo números.")

