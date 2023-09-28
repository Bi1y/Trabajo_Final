from usuario import Usuario
from reporte_financiero import ReporteFinanciero
from datetime import datetime
import os
import sys


def cargar_usuario():
    if os.path.exists("data/usuarios.txt"):
        with open("data/usuarios.txt", "r") as archivo:
            nombre_usuario = archivo.read().strip()
        return Usuario(nombre_usuario)
    else:
        return None


def registrar_usuario():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    with open("data/usuarios.txt", "w") as archivo:
        archivo.write(nombre_usuario)
    return Usuario(nombre_usuario)


def editar_usuario():
    nombre_usuario = input("Ingrese su nuevo nombre de usuario: ")
    with open("data/usuarios.txt", "w") as archivo:
        archivo.write(nombre_usuario)
    return Usuario(nombre_usuario)


def eliminar_usuario():
    if os.path.exists("data/usuarios.txt"):
        os.remove("data/usuarios.txt")

    if os.path.exists("data/transacciones.xlsx"):
        os.remove("data/transacciones.xlsx")

    if os.path.exists("data/metas_ahorro.xlsx"):
        os.remove("data/metas_ahorro.xlsx")

    print("Usuario eliminado exitosamente.")
    return None


def menu_principal(usuario):
    while True:
        print(f"Bienvenido, {usuario.nombre}!")
        print("\nMenú Principal:")
        print("1. Añadir Gasto")
        print("2. Añadir Ingreso")
        print("3. Ver Resumen Financiero")
        print("4. Ver Historial de Transacciones")
        print("5. Establecer Meta de Ahorro")
        print("6. Generar Informe Financiero")
        print("7. Editar Usuario")
        print("8. Eliminar Usuario")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            fecha = datetime.now()
            descripcion = input("Descripción: ")
            categoria = input("Categoría: ")
            monto = float(input("Monto: "))
            usuario.agregar_transaccion(fecha, descripcion, categoria, monto, tipo="gasto")

            print("Gasto registrado exitosamente.")

        elif opcion == "2":
            fecha = datetime.now()
            descripcion = input("Descripción: ")
            categoria = input("Categoría: ")
            monto = float(input("Monto: "))
            usuario.agregar_transaccion(fecha, descripcion, categoria, monto, tipo="ingreso")
            print("Ingreso registrado exitosamente.")

        elif opcion == "3":
            resumen = usuario.obtener_resumen_financiero()
            print("\nResumen Financiero:")
            print(f"Total de Gastos: ${resumen['total_gastos']:.2f}")
            print(f"Total de Ingresos: ${resumen['total_ingresos']:.2f}")
            print(f"Balance: ${resumen['balance']:.2f}")

        elif opcion == "4":
            usuario.ver_historial_transacciones()

        elif opcion == "5":
            descripcion = input("Descripción de la meta: ")
            monto_objetivo = float(input("Monto objetivo: "))
            fecha_limite = input("Fecha límite (YYYY-MM-DD): ")
            usuario.establecer_meta_ahorro(descripcion, monto_objetivo, fecha_limite)
            print("Meta de ahorro establecida.")

        elif opcion == "6":
            fecha_hora_actual = datetime.now()
            nombre_informe = fecha_hora_actual.strftime("Informe_%Y-%m-%d_%H-%M-%S.txt")
            usuario.generar_informe_financiero(nombre_informe)

            print(f"Informe generado exitosamente como '{nombre_informe}'")

        elif opcion == "7":
            usuario = editar_usuario()
            print("Usuario editado exitosamente.")

        elif opcion == "8":
            usuario = eliminar_usuario()
            while True:
                print("\nMenú Inicial:")
                print("1. Iniciar Sesión")
                print("2. Registrarse")
                print("3. Salir")

                opcion_inicial = input("Seleccione una opción: ")

                if opcion_inicial == "1":
                    usuario = cargar_usuario()
                    if usuario is None:
                        print("No se encontró un usuario registrado.")
                        continue
                    else:
                        print(f"Bienvenido, {usuario.nombre}!")
                        menu_principal(usuario)
                elif opcion_inicial == "2":
                    usuario = registrar_usuario()
                    menu_principal(usuario)
                elif opcion_inicial == "3":
                    if opcion_inicial == "3":
                        sys.exit()
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")

        elif opcion == "9":
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    usuario = cargar_usuario()

    if usuario is None:
        print("No se encontró un usuario registrado.")
        usuario = registrar_usuario()

    menu_principal(usuario)

