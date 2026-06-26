import tkinter as tk
from tkinter import ttk
from datos import obtener_turnos
from datos import convertir_turno_a_orden
from tkinter import messagebox

def abrir_turnos(recargar_ordenes):

    ventana = tk.Toplevel()

    ventana.title("Turnos Pendientes")

    ventana.geometry("1000x600")

    ventana.resizable(False, False)

    ventana.grab_set()

    titulo = tk.Label(
        ventana,
        text="Turnos Pendientes",
        font=("Segoe UI", 18, "bold")
    )

    columnas = (
        "Turno",
        "Cliente",
        "Equipo",
        "Fecha",
        "Hora"
    )

    tabla_turnos = ttk.Treeview(
        ventana,
        columns=columnas,
        show="headings"
    )

    tabla_turnos.pack(fill="both", expand=True, padx=15, pady=10)

    titulo.pack(pady=15)

    for columna in columnas:
        tabla_turnos.heading(columna, text=columna)
        tabla_turnos.column("Turno", width=80, anchor="center")
        tabla_turnos.column("Cliente", width=250)
        tabla_turnos.column("Equipo", width=250)
        tabla_turnos.column("Fecha", width=120, anchor="center")
        tabla_turnos.column("Hora", width=100, anchor="center")

    def cargar_turnos():

        for item in tabla_turnos.get_children():
            tabla_turnos.delete(item)

        turnos = obtener_turnos()

        for turno in turnos:

            tabla_turnos.insert(
                "",
                "end",
                values=(
                    turno[0],                       # ID Turno
                    turno[3],                       # Cliente
                    f"{turno[5]} {turno[6]}",       # Equipo + Marca
                    turno[1],                       # Fecha
                    turno[2]                        # Hora
                )
            )
    def convertir_turno():

        seleccion = tabla_turnos.selection()

        if not seleccion:
            messagebox.showwarning(
                "Novati Service Desk",
                "Seleccione un turno."
            )
            return

        datos = tabla_turnos.item(seleccion[0], "values")

        turnos = obtener_turnos()

        for turno in turnos:

            if str(turno[0]) == str(datos[0]):

                convertir_turno_a_orden(turno)
                recargar_ordenes()

                break

        cargar_turnos()

        messagebox.showinfo(
            "Novati Service Desk",
            "Turno convertido en Orden correctamente."
        )

    cargar_turnos()

    frame_botones = tk.Frame(ventana)

    frame_botones.pack(pady=15)

    btn_convertir = tk.Button(
        frame_botones,
        text="Convertir a Orden",
        width=20,
        command=convertir_turno
    )

    btn_convertir.pack(side="left", padx=10)

    btn_cerrar = tk.Button(
        frame_botones,
        text="Cerrar",
        width=20,
        command=ventana.destroy
    )

    btn_cerrar.pack(side="left", padx=10)



    