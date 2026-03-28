

def formatear_moneda(cantidad):
    """Formatea un número como moneda con el símbolo $."""
    return f"${cantidad:,.2f}"

def menu_interactivo():
    """
    Interfaz de usuario en terminal para capturar datos y mostrar resultados.
    Incluye manejo de errores con try-except.
    """
    print("--- 🧮 CALCULADORA DE PROPINAS INTERACTIVA ---")
    
    try:
        cuenta = float(input("Ingrese el total de la cuenta: "))
        
        print("\nOpciones de propina:")
        print("1. Porcentaje (ej. 10%, 15%, 20%)")
        print("2. Monto fijo")
        opcion = input("Seleccione una opción (1 o 2): ")

        propina = 0.0
        if opcion == '1':
            pct = float(input("Ingrese el porcentaje de propina: "))
            propina = calcular_propina_porcentaje(cuenta, pct)
        elif opcion == '2':
            fijo = float(input("Ingrese el monto fijo de propina: "))
            propina = calcular_propina_fija(cuenta, fijo)
        else:
            print("Opción no válida. Se usará 0 de propina.")

        personas = int(input("¿Entre cuántas personas se divide la cuenta? "))
        
        total_con_propina = cuenta + propina
        pago_individual = dividir_cuenta(total_con_propina, personas)

        print("\n--- RESUMEN DE PAGO ---")
        print(f"Subtotal:      {formatear_moneda(cuenta)}")
        print(f"Propina:       {formatear_moneda(propina)}")
        print(f"Total General: {formatear_moneda(total_con_propina)}")
        print(f"Por persona:   {formatear_moneda(pago_individual)}")
        print("-----------------------")

    except ValueError as e:
        print(f"\n❌ Error de entrada: {e}. Por favor, use números válidos.") 
        print(f"\n⚠️ Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    menu_interactivo()