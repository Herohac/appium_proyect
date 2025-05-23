from pago import main as pago_main
from test_login_apertura import main as login_main
from test_venta_rapida import main as venta_rapida_main

def menu():
    print("Ejecutando inicio de sesión y apertura...")
    login_main()

    while True:
        print("\nSelecciona el tipo de venta:")
        print("1. Venta rápida")
        print("2. Venta por salón")
        print("3. Salir")

        venta = input("Opción: ")
        if venta == "1":
            venta_rapida_main()
        elif venta == "2":
            # Aquí llamas flujo venta por salón cuando esté listo
            pass
        elif venta == "3":
            break
        else:
            print("Opción inválida")
            continue

        print("\nSelecciona tipo de pago:")
        print("1. Efectivo")
        print("2. Tarjeta")
        print("3. Otros")
        print("4. Plin")
        print("5. Yape")
        print("6. Izipay")
        print("7. Salir")

        pago_op = input("Opción: ")
        if pago_op == "1":
            pago_main(comprobante="Boleta", metodo_pago="Efectivo", tarjeta_tipo=None)
        elif pago_op == "2":
            tarjeta_tipo = input("Tipo de tarjeta (Crédito/Débito): ")
            pago_main(comprobante="Factura", metodo_pago="Tarjeta", tarjeta_tipo=tarjeta_tipo)
        elif pago_op == "3":
            pago_main(comprobante="Boleta", metodo_pago="Otros", tarjeta_tipo=None)
        elif pago_op == "4":
            pago_main(comprobante="Nota", metodo_pago="Plin", tarjeta_tipo=None)
        elif pago_op == "5":
            pago_main(comprobante="Nota", metodo_pago="Yape", tarjeta_tipo=None)
        elif pago_op == "6":
            pago_main(comprobante="Nota", metodo_pago="Izipay", tarjeta_tipo=None)
        elif pago_op == "7":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
