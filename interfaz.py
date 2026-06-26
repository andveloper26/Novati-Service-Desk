import tkinter as tk
from tkinter import ttk
from ventana_nueva_orden import abrir_nueva_orden
from datos import obtener_ordenes
from ventana_detalle import abrir_detalle
from tkinter import messagebox
from ventana_turnos import abrir_turnos
from datos import obtener_estadisticas

ventana = tk.Tk()

ventana.title("Novati Service Desk")
ventana.geometry("1400x800")
ventana.configure(bg="#F4F6F9")


# =========================
# ENCABEZADO
# =========================

header = tk.Frame(
    ventana,
    bg="#1F4E79",
    height=80
)

header.pack(fill="x")

titulo = tk.Label(
    header,
    text="NOVATI SERVICE DESK",
    bg="#1F4E79",
    fg="white",
    font=("Segoe UI", 24, "bold")
)

titulo.pack(pady=(10,0))

subtitulo = tk.Label(
    header,
    text="Sistema de Gestión de Servicio Técnico - Grupo Novati",
    bg="#1F4E79",
    fg="white",
    font=("Segoe UI",11)
)

subtitulo.pack()

# =========================
# CONTENEDOR PRINCIPAL
# =========================

contenedor = tk.Frame(
    ventana,
    bg="#F4F6F9"
)

contenedor.pack(fill="both", expand=True, padx=15, pady=15)


# =========================
# PANEL SUPERIOR
# =========================

panel_superior = tk.Frame(
    contenedor,
    bg="white",
    height=70
)

panel_superior.pack(fill="x")

panel_superior.pack_propagate(False)


# =========================
# PANEL CENTRAL
# =========================

panel_central = tk.Frame(
    contenedor,
    bg="white"
)

panel_central.pack(fill="both", expand=True, pady=10)

# =========================
# TABLA DE ÓRDENES
# =========================

columnas = (
    "Orden",
    "Cliente",
    "Equipo",
    "Estado",
    "Fecha"
)

tabla = ttk.Treeview(
    panel_central,
    columns=columnas,
    show="headings"
)

scroll = ttk.Scrollbar(
    panel_central,
    orient="vertical",
    command=tabla.yview
)

tabla.configure(yscrollcommand=scroll.set)

scroll.pack(side="right", fill="y")
tabla.pack(fill="both", expand=True, padx=10, pady=10)

for columna in columnas:
    tabla.heading(columna, text=columna)

tabla.column("Orden", width=80, anchor="center")
tabla.column("Cliente", width=250)
tabla.column("Equipo", width=250)
tabla.column("Estado", width=180)
tabla.column("Fecha", width=120, anchor="center")

# =========================
# PANEL INFERIOR
# =========================

panel_inferior = tk.Frame(
    contenedor,
    bg="white",
    height=70
)

panel_inferior.pack(fill="x")

panel_inferior.pack_propagate(False)

# =========================
# BOTONES PRINCIPALES
# =========================

def ver_turnos():
    abrir_turnos(cargar_ordenes)
    actualizar_dashboard()

btn_turnos = ttk.Button(
    panel_inferior,
    text="📅 Turnos Pendientes",
    command=ver_turnos
)

btn_turnos.pack(
    side="left",
    padx=20,
    pady=15
)


btn_nueva = ttk.Button(
    panel_inferior,
    text="➕ Nueva Orden",
    command=abrir_nueva_orden
)

btn_nueva.pack(
    side="left",
    padx=10
)

def ver_detalle():

    seleccion = tabla.selection()

    if not seleccion:
        messagebox.showwarning(
            "Novati Service Desk",
            "Seleccione una orden."
        )
        return

    datos = tabla.item(seleccion[0], "values")

    abrir_detalle(
        datos,
        cargar_ordenes,
        actualizar_dashboard
    )

btn_detalle = ttk.Button(
    panel_inferior,
    text="👁 Ver Detalle",
    command=ver_detalle
)

btn_detalle.pack(
    side="left",
    padx=10
)

# =========================
# BUSCADOR
# =========================

lbl_buscar = tk.Label(
    panel_superior,
    text="Buscar:",
    bg="white",
    font=("Segoe UI", 11, "bold")
)


combo_estado = ttk.Combobox(
    panel_superior,
    values=[
        "Todos",
        "Ingresado",
        "En revisión",
        "Presupuestado",
        "En proceso",
        "Reparado listo para entregar",
        "Pendiente de retiro",
        "Entregado",
        "En conflicto",
        "En depósito"
    ],
    state="readonly",
    width=25
)

# =========================
# TARJETAS DEL DASHBOARD
# =========================

frame_tarjetas = tk.Frame(
    panel_superior,
    bg="white"
)

frame_tarjetas.pack(side="right", padx=20)

card_turnos = tk.Frame(
    frame_tarjetas,
    bg="#3498DB",
    width=140,
    height=50
)

card_turnos.pack(side="left", padx=5)

card_turnos.pack_propagate(False)

lbl_turnos = tk.Label(
    card_turnos,
    text="Turnos\n0",
    bg="#3498DB",
    fg="white",
    font=("Segoe UI", 10, "bold")
)

lbl_turnos.pack(expand=True)

card_ordenes = tk.Frame(
    frame_tarjetas,
    bg="#F39C12",
    width=140,
    height=50
)

card_ordenes.pack(side="left", padx=5)

card_ordenes.pack_propagate(False)

lbl_ordenes = tk.Label(
    card_ordenes,
    text="Órdenes\n0",
    bg="#F39C12",
    fg="white",
    font=("Segoe UI", 10, "bold")
)

lbl_ordenes.pack(expand=True)

card_listos = tk.Frame(
    frame_tarjetas,
    bg="#27AE60",
    width=140,
    height=50
)

card_listos.pack(side="left", padx=5)

card_listos.pack_propagate(False)

lbl_listos = tk.Label(
    card_listos,
    text="Listos\n0",
    bg="#27AE60",
    fg="white",
    font=("Segoe UI", 10, "bold")
)

lbl_listos.pack(expand=True)

card_conflictos = tk.Frame(
    frame_tarjetas,
    bg="#E74C3C",
    width=140,
    height=50
)

card_conflictos.pack(side="left", padx=5)

card_conflictos.pack_propagate(False)

lbl_conflictos = tk.Label(
    card_conflictos,
    text="Conflictos\n0",
    bg="#E74C3C",
    fg="white",
    font=("Segoe UI", 10, "bold")
)

lbl_conflictos.pack(expand=True)

def buscar(event=None):

    texto = entry_buscar.get().lower()

    for item in tabla.get_children():
        tabla.delete(item)

    ordenes = obtener_ordenes()

    for orden in ordenes:

        numero = str(orden[0]).lower()
        cliente = str(orden[3]).lower()
        equipo = f"{orden[5]} {orden[6]}".lower()
        estado = str(orden[9]).lower()

        estado_filtro = combo_estado.get()

        if estado_filtro != "Todos" and orden[9] != estado_filtro:
            continue

        if (
            texto in numero
            or texto in cliente
            or texto in equipo
            or texto in estado
        ):

            tabla.insert(
                "",
                "end",
                values=(
                    orden[0],
                    orden[3],
                    f"{orden[5]} {orden[6]}",
                    orden[9],
                    orden[1]
                )
            )

def filtrar_estado(event=None):

    estado = combo_estado.get()

    if estado == "Todos":
        cargar_ordenes()
        return

    for item in tabla.get_children():
        tabla.delete(item)

    ordenes = obtener_ordenes()

    for orden in ordenes:

        if orden[9] == estado:

            tabla.insert(
                "",
                "end",
                values=(
                    orden[0],
                    orden[3],
                    f"{orden[5]} {orden[6]}",
                    orden[9],
                    orden[1]
                )
            )

combo_estado.current(0)
combo_estado.bind("<<ComboboxSelected>>", filtrar_estado)

combo_estado.pack(side="left")

def cargar_ordenes():

    for item in tabla.get_children():
        tabla.delete(item)

    ordenes = obtener_ordenes()

    for orden in ordenes:

        tabla.insert(
            "",
            "end",
            values=(
                orden[0],                                   # Número
                orden[3],                                   # Cliente
                f"{orden[5]} {orden[6]}",                   # Equipo + Marca
                orden[9],                                   # Estado
                orden[1]                                    # Fecha
            )
        )

def actualizar_dashboard():

    turnos, ordenes, listos, conflictos = obtener_estadisticas()

    lbl_turnos.config(text=f"Turnos\n{turnos}")

    lbl_ordenes.config(text=f"Órdenes\n{ordenes}")

    lbl_listos.config(text=f"Listos\n{listos}")

    lbl_conflictos.config(text=f"Conflictos\n{conflictos}")

lbl_buscar.pack(side="left", padx=(20,5), pady=20)

entry_buscar = ttk.Entry(
    panel_superior,
    width=40
)

entry_buscar.pack(side="left")
entry_buscar.bind("<KeyRelease>", buscar)

cargar_ordenes()
actualizar_dashboard()

lbl_estado = tk.Label(
    panel_superior,
    text="Estado:",
    bg="white",
    font=("Segoe UI",11,"bold")
)

lbl_estado.pack(side="left", padx=(30,5))

def iniciar_aplicacion():

    cargar_ordenes()
    actualizar_dashboard()

    ventana.mainloop()