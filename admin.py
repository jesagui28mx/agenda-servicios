import streamlit as st
import pandas as pd
import os
from pandas.errors import EmptyDataError

st.set_page_config(
    page_title="Aires FC | Panel Interno",
    page_icon="🛠️",
    layout="wide"
)

DATA_PATH = "data/servicios.csv"

st.title("🛠️ Aires FC | Panel Interno")

if not os.path.exists(DATA_PATH) or os.path.getsize(DATA_PATH) == 0:
    st.warning("Todavía no hay solicitudes registradas.")
    st.stop()

try:
    df = pd.read_csv(DATA_PATH)
except EmptyDataError:
    st.warning("Todavía no hay solicitudes registradas.")
    st.stop()

if df.empty:
    st.warning("Todavía no hay solicitudes registradas.")
    st.stop()

total = len(df)
pendientes = len(df[df["estatus"] == "Pendiente"])
asignados = len(df[df["estatus"] == "Asignado"])
completados = len(df[df["estatus"] == "Completado"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total solicitudes", total)
col2.metric("Pendientes", pendientes)
col3.metric("Asignadas", asignados)
col4.metric("Completadas", completados)

st.divider()

st.subheader("Solicitudes registradas")
st.dataframe(df, use_container_width=True)

st.divider()

st.subheader("Actualizar solicitud")

folios = df["folio"].tolist()
folio_sel = st.selectbox("Selecciona folio", folios)

registro = df[df["folio"] == folio_sel].iloc[0]

st.write("Cliente:", registro["nombre"])
st.write("Servicio:", registro["servicio"])
st.write("Fecha deseada:", registro["fecha_deseada"])

tecnico = st.text_input("Técnico asignado", value=str(registro.get("tecnico", "")))

estatus = st.selectbox(
    "Estatus",
    ["Pendiente", "Asignado", "Completado", "Cancelado", "Reprogramado"],
    index=["Pendiente", "Asignado", "Completado", "Cancelado", "Reprogramado"].index(registro["estatus"])
)

if st.button("Guardar cambios"):
    df.loc[df["folio"] == folio_sel, "tecnico"] = tecnico
    df.loc[df["folio"] == folio_sel, "estatus"] = estatus
    df.to_csv(DATA_PATH, index=False)

    st.success("Solicitud actualizada correctamente.")
    st.rerun()
