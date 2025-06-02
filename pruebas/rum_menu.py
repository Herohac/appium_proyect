from pruebas.pago import main as pago_main
from pruebas.test_login_apertura import main as login_main
from pruebas.test_venta_rapida import main as venta_rapida_main
from test.appium_driver import start_appium_driver
import os
import platform
import subprocess

def abrir_reporte():
    ruta_reporte = os.path.abspath("allure-report/index.html")
    sistema = platform.system()
    try:
        if sistema == "Windows":
            os.startfile(ruta_reporte)
        elif sistema == "Darwin":
            subprocess.run(["open", ruta_reporte])
        else:
            subprocess.run(["xdg-open", ruta_reporte])
        print(f"Reporte abierto: {ruta_reporte}")
    except Exception as e:
        print(f"No se pudo abrir el reporte automáticamente: {e}")

def menu():
    driver = start_appium_driver()
    try:
        while True:
            print("\nSeleccione tipo de venta:")
            print("1. Venta rápida")
            print("2. Venta por salón (pendiente)")
            print("3. Salir")

            venta_op = input("Opción: ")
            if venta_op == "3":
                print("Saliendo...")
                break
            if venta_op not in ["1", "2"]:
                print("Opción inválida.")
                continue

            print("\nSeleccione tipo de comprobante:")
            print("1. Factura")
            print("2. Boleta")
            print("3. Nota")

            comprobante_op = input("Opción: ")
            if comprobante_op not in ["1", "2", "3"]:
                print("Opción inválida.")
                continue

            comprobantes = {"1": "Factura", "2": "Boleta", "3": "Nota"}
            comprobante = comprobantes[comprobante_op]

            print("\nSeleccione medio de pago:")
            print("1. Efectivo")
            print("2. Tarjeta")
            print("3. Otros")
            print("4. Plin")
            print("5. Yape")
            print("6. Izipay")

            pago_op = input("Opción: ")
            if pago_op not in ["1", "2", "3", "4", "5", "6"]:
                print("Opción inválida.")
                continue

            medios_pago = {
                "1": "Efectivo",
                "2": "Tarjeta",
                "3": "Otros",
                "4": "Plin",
                "5": "Yape",
                "6": "Izipay",
            }
            metodo_pago = medios_pago[pago_op]
            tarjeta_tipo = None

            if metodo_pago.lower() == "tarjeta":
                tarjeta_tipo = input("Tipo de tarjeta (Crédito/Débito): ")

            print(f"\nEjecutando flujo: venta opción {venta_op} con comprobante {comprobante} y pago {metodo_pago}")

            login_main(driver)

            if venta_op == "1":
                venta_rapida_main(driver)
            else:
                print("Venta por salón aún no implementada.")

            pago_main(driver, comprobante=comprobante, metodo_pago=metodo_pago, tarjeta_tipo=tarjeta_tipo)

            # Abre reporte (puedes modificar la ruta si es necesario)
            abrir_reporte()

            cont = input("\n¿Desea realizar otra operación? (s/n): ").lower()
            if cont != "s":
                print("Finalizando programa.")
                break
    finally:
        driver.quit()

if __name__ == "__main__":
    menu()
