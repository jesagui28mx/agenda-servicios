import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(
    page_title="Aires FC | Solicitar Servicio",
    page_icon="❄️",
    layout="centered"
)

DATA_PATH = "data/servicios.csv"

st.title("❄️ Aires FC")
st.subheader("Solicita tu servicio")

with st.form("form_solicitud"):
    nombre = st.text_input("Nombre completo")
    telefono = st.text_input("Teléfono / WhatsApp")
    direccion = st.text_area("Dirección")
    
    servicio = st.selectbox(
        "Tipo de servicio",
        ["Mantenimiento", "Instalación", "Reparación", "Revisión"]
    )
    
    equipos = st.number_input("Cantidad de equipos", min_value=1, step=1)
    fecha_deseada = st.date_input("Fecha deseada")
    horario = st.selectbox(
        "Horario preferido",
        ["Mañana", "Mediodía", "Tarde"]
    )
    comentarios = st.text_area("Comentarios adicionales")

    enviar = st.form_submit_button("Solicitar servicio")

if enviar:
    os.makedirs("data", exist_ok=True)

    nuevo = {
        "folio": f"AFC-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion,
        "servicio": servicio,
        "equipos": equipos,
        "fecha_deseada": fecha_deseada,
        "horario": horario,
        "comentarios": comentarios,
        "tecnico": "",
        "estatus": "Pendiente"
    }

    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
    else:
        df = pd.DataFrame([nuevo])

    df.to_csv(DATA_PATH, index=False)

    st.success("Solicitud enviada correctamente.")
    st.info(f"Tu folio es: {nuevo['folio']}")
    st.write("Aires FC se pondrá en contacto contigo para confirmar la cita.")
