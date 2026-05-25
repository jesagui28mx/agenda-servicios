import streamlit as st

st.title("📊 Dashboard")

col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric("Programados","8")

with col2:
    st.metric("Completados","5")

with col3:
    st.metric("Pendientes","2")

with col4:
    st.metric("Reprogramados","1")

st.divider()

st.subheader("Servicios próximos")

st.table([
{
"Hora":"09:00",
"Cliente":"Juan Pérez",
"Servicio":"Mantenimiento",
"Técnico":"Carlos"
},
{
"Hora":"11:30",
"Cliente":"Hotel Sol",
"Servicio":"Instalación",
"Técnico":"Miguel"
}
])
