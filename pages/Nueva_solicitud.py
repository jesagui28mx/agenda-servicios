import streamlit as st

st.title("📝 Nueva Solicitud")

nombre=st.text_input("Nombre")

telefono=st.text_input("Teléfono")

direccion=st.text_area("Dirección")

servicio=st.selectbox(
"Tipo de servicio",
[
"Mantenimiento",
"Instalación",
"Reparación"
]
)

equipos=st.number_input(
"Cantidad equipos",
min_value=1
)

fecha=st.date_input(
"Fecha deseada"
)

if st.button("Guardar solicitud"):
    st.success("Solicitud registrada")
