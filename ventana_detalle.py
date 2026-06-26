import tkinter as tk
from datos import actualizar_estado
from datos import actualizar_estado, guardar_historial
from tkinter import messagebox


def abrir_detalle(datos, recargar_tabla, actualizar_dashboard):

    ventana = tk.Toplevel()

    ventana.title("Detalle de la Orden")

    ventana.geometry("700x500")

    ventana.resizable(False, False)

    ventana.grab_set()

    titulo = tk.Label(
        ventana,
        text="Detalle de la Orden",
        font=("Segoe UI", 18, "bold")
    )

    titulo.pack(pady=20)

    frame = tk.Frame(ventana)

    frame.pack(fill="both", padx=20, pady=20)

    tk.Label(
        frame,
        text=f"N° Orden: {datos[0]}",
        font=("Segoe UI", 11)
    ).pack(anchor="w", pady=5)

    tk.Label(
        frame,
        text=f"Cliente: {datos[1]}",
        font=("Segoe UI", 11)
    ).pack(anchor="w", pady=5)

    tk.Label(
        frame,
        text=f"Equipo: {datos[2]}",
        font=("Segoe UI", 11)
    ).pack(anchor="w", pady=5)

    tk.Label(
        frame,
        text=f"Estado: {datos[3]}",
        font=("Segoe UI", 11)
    ).pack(anchor="w", pady=5)

    def guardar_estado():

        numero_orden = int(datos[0])

        nuevo_estado = estado.get()

        actualizar_estado(numero_orden, nuevo_estado)

        guardar_historial(
            numero_orden,
            nuevo_estado,
            "",
            "Técnico"
        )

        recargar_tabla()
        actualizar_dashboard()

        messagebox.showinfo(
            "Novati Service Desk",
            "Estado actualizado correctamente."
        )

        ventana.destroy()

    tk.Label(
        frame,
        text=f"Fecha: {datos[4]}",
        font=("Segoe UI", 11)
    ).pack(anchor="w", pady=5)

    tk.Label(
        frame,
        text="Estado:",
        font=("Segoe UI", 11, "bold")
    ).pack(anchor="w", pady=(20, 5))

    estado = tk.StringVar()

    cmb_estado = tk.OptionMenu(
        frame,
        estado,
        "Ingresado",
        "En revisión",
        "Presupuestado",
        "En proceso",
        "Listo para entregar",
        "Entregado",
        "En conflicto",
        "En depósito"
    )

    estado.set(datos[3])

    cmb_estado.pack(anchor="w")

    btn_actualizar = tk.Button(
        frame,
        text="Actualizar Estado",
        width=20,
        command=guardar_estado
    )

    btn_actualizar.pack(pady=20)