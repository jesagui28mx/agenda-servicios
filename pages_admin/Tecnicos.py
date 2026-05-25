import streamlit as st
import pandas as pd

st.subheader("👨‍🔧 Técnicos")

tecnicos = pd.DataFrame([
    {"Nombre":"Carlos","Zona":"Norte","Estado":"Disponible"},
    {"Nombre":"Miguel","Zona":"Centro","Estado":"Ocupado"}
])

st.dataframe(tecnicos, use_container_width=True)
