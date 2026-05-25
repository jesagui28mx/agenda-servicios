import streamlit as st

st.subheader("📊 Dashboard")

col1,col2,col3,col4=st.columns(4)

col1.metric("Programados","8")
col2.metric("Completados","5")
col3.metric("Pendientes","2")
col4.metric("Reprogramados","1")
