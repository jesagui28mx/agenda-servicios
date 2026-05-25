import streamlit as st
import pandas as pd
import os

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

df = pd.read_csv(DATA_PATH)

if df.empty:
    st.warning("Todavía no hay solicitudes registradas.")
    st.stop()
