# Novati Service Desk + Chatbot

## Descripción

Proyecto desarrollado para la materia **Organización Empresarial** de la **Tecnicatura Universitaria en Programación** (UTN).

El proyecto consiste en la automatización del proceso de atención de un servicio técnico de informática mediante el modelado BPMN 2.0 y el desarrollo de dos aplicaciones integradas:

- **Chatbot de atención al cliente**, encargado de registrar turnos, consultar el estado de las reparaciones y derivar consultas al personal técnico.
- **Novati Service Desk**, sistema interno utilizado por el técnico para administrar turnos, órdenes de servicio, historial y seguimiento de las reparaciones.

Ambas aplicaciones comparten la misma base de datos implementada mediante archivos Microsoft Excel.

---

## Tecnologías utilizadas

- Python 3.11
- Tkinter
- OpenPyXL
- Microsoft Excel (.xlsx)
- BPMN 2.0

---

## Funcionalidades

### Chatbot

- Solicitud de turnos.
- Consulta del estado de las reparaciones.
- Derivación de consultas al técnico.
- Validación de datos ingresados por el usuario.
- Máquina de estados para controlar el flujo de conversación.

### Novati Service Desk

- Gestión de órdenes de servicio.
- Administración de turnos.
- Conversión de turnos en órdenes.
- Actualización de estados.
- Historial de cambios.
- Búsquedas y filtros.
- Dashboard con indicadores.

---

## Flujo del proceso

Cliente

↓

Chatbot

↓

Turnos.xlsx

↓

Novati Service Desk

↓

Órdenes.xlsx

↓

Seguimiento de la reparación

↓

Entrega del equipo

---

## Autores

Ramón Andrés Díaz

Tecnicatura Universitaria en Programación

Universidad Tecnológica Nacional

Ciclo Lectivo 2026