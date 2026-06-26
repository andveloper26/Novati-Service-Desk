import tkinter as tk
from tkinter import scrolledtext
from datos import guardar_turno, buscar_orden

# ==========================
# VENTANA
# ==========================

ventana = tk.Tk()

ventana.title("Grupo Novati - Chatbot")

ventana.geometry("450x700")

ventana.configure(bg="#ECE5DD")


# ==========================
# VARIABLES
# ==========================

estado = "MENU"

datos_turno = {
    "cliente": "",
    "celular": "",
    "equipo": "",
    "marca": "",
    "modelo": "",
    "falla": ""
}

def mostrar_menu():

    escribir_bot("")

    escribir_bot("Seleccione una opción:")

    escribir_bot("1 - Solicitar Turno")

    escribir_bot("2 - Consultar Estado")

    escribir_bot("3 - Hablar con un Técnico")

# ==========================
# CHAT
# ==========================

chat = scrolledtext.ScrolledText(
    ventana,
    width=50,
    height=28,
    font=("Segoe UI",11),
    state="disabled",
    wrap="word"
)

chat.pack(
    padx=10,
    pady=10,
    fill="both",
    expand=True
)


# ==========================
# ENTRADA
# ==========================

frame = tk.Frame(
    ventana,
    bg="#ECE5DD"
)

frame.pack(fill="x", padx=10, pady=10)


entrada = tk.Entry(
    frame,
    font=("Segoe UI",12)
)

entrada.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0,10)
)


# ==========================
# FUNCIONES
# ==========================

def escribir_bot(texto):

    chat.config(state="normal")

    chat.insert(tk.END, "🤖 Bot: " + texto + "\n\n")

    chat.config(state="disabled")

    chat.see(tk.END)


def escribir_usuario(texto):

    chat.config(state="normal")

    chat.insert(tk.END, "👤 Usted: " + texto + "\n\n")

    chat.config(state="disabled")

    chat.see(tk.END)

def procesar():

    global estado

    mensaje = entrada.get().strip()

    if mensaje == "":
        return

    entrada.delete(0, tk.END)

    escribir_usuario(mensaje)

    # ==========================
    # MENU
    # ==========================

    if estado == "MENU":

        if mensaje == "1":
            estado = "NOMBRE"
            escribir_bot("Ingrese su nombre y apellido:")
            return

        elif mensaje == "2":
            estado = "CONSULTA"
            escribir_bot("Ingrese el número de orden:")
            return

        elif mensaje == "3":
            estado = "TECNICO"
            escribir_bot("Describa brevemente su consulta para derivarla a un técnico.")
            return

        else:
            mostrar_menu()
            return

    # ==========================
    # NOMBRE
    # ==========================

    if estado == "NOMBRE":

        if len(mensaje) < 5:

            escribir_bot("Ingrese su nombre y apellido completo.")

            return

        datos_turno["cliente"] = mensaje

        estado = "CELULAR"

        escribir_bot("Ingrese su número de celular:")

        return

    # ==========================
    # CELULAR
    # ==========================

    if estado == "CELULAR":

        if (not mensaje.isdigit()) or len(mensaje) < 8:

            escribir_bot("Ingrese un número de celular válido.")

            return

        datos_turno["celular"] = mensaje

        estado = "EQUIPO"

        escribir_bot("Seleccione el equipo:")

        escribir_bot("1 - Notebook")
        escribir_bot("2 - PC de escritorio")
        escribir_bot("3 - Impresora")
        escribir_bot("4 - Monitor")
        escribir_bot("5 - All In One")

        return

    # ==========================
    # EQUIPO
    # ==========================

    if estado == "EQUIPO":

        equipos = {
            "1":"Notebook",
            "2":"PC de escritorio",
            "3":"Impresora",
            "4":"Monitor",
            "5":"All In One"
        }

        if mensaje not in equipos:

            escribir_bot("Seleccione una opción válida.")

            return

        datos_turno["equipo"] = equipos[mensaje]

        estado = "MARCA"

        escribir_bot("Ingrese la marca:")

        return

    # ==========================
    # MARCA
    # ==========================

    if estado == "MARCA":

        if len(mensaje) < 2:

            escribir_bot("Ingrese una marca válida.")

            return

        datos_turno["marca"] = mensaje

        estado = "MODELO"

        escribir_bot("Ingrese el modelo:")

        return

    # ==========================
    # MODELO
    # ==========================

    if estado == "MODELO":

        if len(mensaje) < 2:

            escribir_bot("Ingrese un modelo válido.")

            return

        datos_turno["modelo"] = mensaje

        estado = "FALLA"

        escribir_bot("Describa la falla del equipo:")

        return

    # ==========================
    # FALLA
    # ==========================

    if estado == "FALLA":

        datos_turno["falla"] = mensaje

        guardar_turno(
            datos_turno["cliente"],
            datos_turno["celular"],
            datos_turno["equipo"],
            datos_turno["marca"],
            datos_turno["modelo"],
            datos_turno["falla"]
        )

        escribir_bot("━━━━━━━━━━━━━━━━━━━━━━━━")

        escribir_bot("✅ TURNO REGISTRADO")

        escribir_bot(f"Cliente: {datos_turno['cliente']}")

        escribir_bot(f"Equipo: {datos_turno['equipo']}")

        escribir_bot(f"Marca: {datos_turno['marca']}")

        escribir_bot("Estado: Pendiente")

        escribir_bot("")

        escribir_bot("Un representante confirmará la fecha y horario de recepción del equipo.")

        escribir_bot("Una vez ingresado al laboratorio podrá consultar el estado de la reparación mediante el número de Orden de Servicio.")

        escribir_bot("━━━━━━━━━━━━━━━━━━━━━━━━")

        datos_turno.clear()

        datos_turno.update({
            "cliente":"",
            "celular":"",
            "equipo":"",
            "marca":"",
            "modelo":"",
            "falla":""
        })

        estado = "MENU"

        mostrar_menu()

        return

    # ==========================
    # CONSULTA
    # ==========================

    if estado == "CONSULTA":

        orden = buscar_orden(mensaje)

        if orden:

            escribir_bot("━━━━━━━━━━━━━━━━━━━━━━━━")

            escribir_bot(f"Orden Nº {orden[0]}")

            escribir_bot(f"Cliente: {orden[3]}")

            escribir_bot(f"Equipo: {orden[5]} {orden[6]}")

            escribir_bot(f"Estado actual: {orden[9]}")

            escribir_bot("━━━━━━━━━━━━━━━━━━━━━━━━")

        else:

            escribir_bot("No se encontró esa orden.")

        estado = "MENU"

        mostrar_menu()

    # ==========================
    # TECNICO
    # ==========================

    if estado == "TECNICO":

        escribir_bot("✅ Su consulta fue registrada.")

        escribir_bot("Un técnico de Grupo Novati se comunicará con usted a la brevedad.")

        estado = "MENU"

        mostrar_menu()

        return

# ==========================
# BOTÓN
# ==========================

btn = tk.Button(
    frame,
    text="Enviar",
    width=10,
    command=procesar
)

btn.pack(side="right")

entrada.bind("<Return>", lambda event: procesar())


# ==========================
# MENSAJE INICIAL
# ==========================

escribir_bot("¡Hola! Soy el asistente virtual de Grupo Novati.")

escribir_bot("Seleccione una opción:")

escribir_bot("1️. Solicitar Turno")

escribir_bot("2️. Consultar Estado")

escribir_bot("3️. Hablar con un Técnico")


ventana.mainloop()