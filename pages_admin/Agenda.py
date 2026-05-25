import streamlit as st
import pandas as pd

st.subheader("📅 Agenda")

agenda = pd.DataFrame([
    {"Hora":"09:00","Cliente":"Juan Pérez","Técnico":"Carlos"},
    {"Hora":"11:30","Cliente":"Hotel Sol","Técnico":"Miguel"}
])

st.dataframe(agenda, use_container_width=True)
