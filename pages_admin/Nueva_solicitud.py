import streamlit as st

st.subheader("📝 Nueva solicitud")

st.text_input("Cliente")
st.selectbox(
    "Servicio",
    ["Mantenimiento","Instalación","Reparación"]
)

st.button("Guardar")
