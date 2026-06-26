import tkinter as tk
from tkinter import messagebox
from datos import guardar_orden, obtener_siguiente_orden
from datetime import datetime


def abrir_nueva_orden():

    ventana = tk.Toplevel()

    ventana.title("Nueva Orden")

    ventana.geometry("700x600")

    ventana.resizable(False, False)

    ventana.grab_set()

# =========================
# TÍTULO
# =========================

    titulo = tk.Label(
    ventana,
    text="Nueva Orden de Servicio",
    font=("Segoe UI", 18, "bold")
    )

    titulo.pack(pady=20)

    frame_datos = tk.Frame(ventana)

    frame_datos.pack(padx=20, pady=10, fill="x")

    lbl_cliente = tk.Label(
    frame_datos,
    text="Cliente:"
    )

    lbl_cliente.grid(
        row=0,
        column=0,
        sticky="w",
        pady=5
    )

    entry_cliente = tk.Entry(
        frame_datos,
        width=40
    )

    entry_cliente.grid(
        row=0,
        column=1,
        pady=5
    )

    lbl_celular = tk.Label(
    frame_datos,
    text="Celular:"
    )

    lbl_celular.grid(
        row=1,
        column=0,
        sticky="w",
        pady=5
    )

    entry_celular = tk.Entry(
        frame_datos,
        width=40
    )

    entry_celular.grid(
        row=1,
        column=1,
        pady=5
    )

    lbl_equipo = tk.Label(
    frame_datos,
    text="Tipo de Equipo:"
    )

    lbl_equipo.grid(
        row=2,
        column=0,
        sticky="w",
        pady=5
    )

    combo_equipo = tk.StringVar()

    cmb_equipo = tk.OptionMenu(
        frame_datos,
        combo_equipo,
        "Notebook",
        "PC de escritorio",
        "Impresora",
        "Monitor",
        "All In One"
    )

    cmb_equipo.config(width=25)

    cmb_equipo.grid(
        row=2,
        column=1,
        sticky="w",
        pady=5
    )

    combo_equipo.set("Notebook")

    lbl_marca = tk.Label(
        frame_datos,
        text="Marca:"
    )

    lbl_marca.grid(
        row=3,
        column=0,
        sticky="w",
        pady=5
    )

    entry_marca = tk.Entry(
        frame_datos,
        width=40
    )

    entry_marca.grid(
        row=3,
        column=1,
        pady=5
    )

    lbl_modelo = tk.Label(
        frame_datos,
        text="Modelo:"
    )

    lbl_modelo.grid(
        row=4,
        column=0,
        sticky="w",
        pady=5
    )

    entry_modelo = tk.Entry(
        frame_datos,
        width=40
    )

    entry_modelo.grid(
        row=4,
        column=1,
        pady=5
    )

    lbl_falla = tk.Label(
    frame_datos,
    text="Descripción de la falla:"
    )

    lbl_falla.grid(
        row=5,
        column=0,
        sticky="nw",
        pady=5
    )

    txt_falla = tk.Text(
        frame_datos,
        width=40,
        height=5
    )

    txt_falla.grid(
        row=5,
        column=1,
        pady=5
    )

    # =========================
    # BOTONES
    # =========================

    def guardar_orden_click():

        cliente = entry_cliente.get()

        celular = entry_celular.get()

        equipo = combo_equipo.get()

        marca = entry_marca.get()

        modelo = entry_modelo.get()

        falla = txt_falla.get("1.0", tk.END).strip()

        numero = obtener_siguiente_orden()

        ahora = datetime.now()

        fecha = ahora.strftime("%d/%m/%Y")

        hora = ahora.strftime("%H:%M")

        mensaje = f"""

    Cliente: {cliente}

    Celular: {celular}

    Equipo: {equipo}

    Marca: {marca}

    Modelo: {modelo}

    Falla: {falla}
    """
        guardar_orden(
            numero,
            fecha,
            hora,
            cliente,
            celular,
            equipo,
            marca,
            modelo,
            falla,
            "Ingresado",
            ""
        )

        messagebox.showinfo(
            "Novati Service Desk",
            f"Orden N° {numero} guardada correctamente."
        )

        ventana.destroy()

    frame_botones = tk.Frame(ventana)

    frame_botones.pack(pady=20)

    btn_guardar = tk.Button(
        frame_botones,
        text="Guardar Orden",
        width=18,
        command=guardar_orden_click
    )

    btn_guardar.pack(
        side="left",
        padx=10
    )

    btn_cancelar = tk.Button(
        frame_botones,
        text="Cancelar",
        width=18,
        command=ventana.destroy
    )

    btn_cancelar.pack(
        side="left",
        padx=10
    )