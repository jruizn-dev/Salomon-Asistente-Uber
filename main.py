from utilidades import saludo_personalizado, calcular_ganancia_uber
from gestion_datos import guardar_historial

 while True:
        pedido = escuchar()

        
        if 'buenos días' in pedido or 'buenas tardes' in pedido or 'buenas noches' in pedido:
            saludo_personalizado(pedido) # <--- Aquí le mandas el dato
               

        elif 'ingresos del día' in pedido or 'cuales son los ingresos del día' in pedido:
            # Solo llamamos a la función, ella hará el resto del trabajo
            calcular_ganancia_uber()

        elif 'guardar ingreso' in pedido:
        # Aquí llamarías a tu nueva función
        guardar_historial("Ganancia del día: 875 pesos")

        else:
            print(f"Comando '{pedido}' no reconocido.")
            # Opcional: puedes hacer que Salomon diga que no entendió