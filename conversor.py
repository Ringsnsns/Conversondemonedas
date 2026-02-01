import streamlit as st

st.title("conversor de Lempiras a Dolares")

lempiras=st.number_input("Ingrese la cantidad de lempiras", min_value=0.0)

if st.button ("procesar"):
    dolares=lempiras/26.00
    st.write("El equivalente es")