import math 

def calcular_propina_porcentaje(monto_cuenta, porcentaje):
    """
    Calcula el monto de la propina basado en un porcentaje.
    Valida que los valores sean positivos.
    """
    if monto_cuenta < 0 or porcentaje < 0:
        raise ValueError("El monto y el porcentaje deben ser positivos.")
    return monto_cuenta * (porcentaje / 100)

def calcular_propina_fija(monto_cuenta, monto_propina):
    """
    Calcula la propina usando un monto fijo específico. 
    """
    if monto_cuenta < 0 or monto_propina < 0:
        raise ValueError("Los montos deben ser positivos.")
    return monto_propina

def dividir_cuenta(monto_total, num_personas):
    """
    Divide el total (cuenta + propina) entre el número de personas.
    Retorna el monto por persona redondeado a 2 decimales.
    """
    if num_personas <= 0:
        raise ValueError("El número de personas debe ser al menos 1.")
    
    monto_por_persona = monto_total / num_personas
    return round(monto_por_persona, 4)