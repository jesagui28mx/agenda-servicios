import streamlit as st

st.set_page_config(
    page_title="Aires FC | Panel Interno",
    page_icon="🛠️",
    layout="wide"
)

st.title("🛠️ Aires FC | Panel Interno")

pagina=st.sidebar.selectbox(
    "Menú",
    [
        "Dashboard",
        "Agenda",
        "Técnicos",
        "Historial",
        "Nueva Solicitud"
    ]
)

if pagina=="Dashboard":
    exec(open("pages_admin/Dashboard.py").read())

elif pagina=="Agenda":
    exec(open("pages_admin/Agenda.py").read())

elif pagina=="Técnicos":
    exec(open("pages_admin/Tecnicos.py").read())

elif pagina=="Historial":
    exec(open("pages_admin/Historial.py").read())

elif pagina=="Nueva Solicitud":
    exec(open("pages_admin/Nueva_solicitud.py").read())
