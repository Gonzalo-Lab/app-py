import pandas as pd
import streamlit as st
import numpy as np

# Función para cargar datos desde un archivo CSV
def cargar_datos(csv_file):
    return pd.read_csv(csv_file)

# Función para calcular las variables internas
def procesar_variables_internas(datos):
    escala_borg = datos['escala_borg'].mean()
    vfc = datos['vfc'].mean()
    test_hopper = datos['test_hopper'].mean()
    control_sueno = datos['control_sueno'].mean()
    return escala_borg, vfc, test_hopper, control_sueno

# Función para calcular la carga externa
def calcular_carga_externa(datos):
    distancia = datos['distancia'].sum()
    velocidad = datos['velocidad'].mean()
    aceleraciones = datos['aceleraciones'].sum()
    return distancia, velocidad, aceleraciones

# Función para calcular el gasto energético
def calcular_gasto_energetico(distancia, peso):
    return distancia * peso * 0.9  # Fórmula hipotética

# Función para calcular el estado de forma
def calcular_estado_de_forma(distancia, velocidad, aceleraciones):
    estado_de_forma = (distancia * 0.1) + (velocidad * 0.5) + (aceleraciones * 0.4)
    return estado_de_forma

# Función para evaluar el riesgo de lesión
def evaluar_riesgo_de_lesion(carga_externa, escala_borg, vfc, test_hopper, control_sueno):
    riesgo_lesion = (carga_externa * 0.5) + (escala_borg * 0.2) + (vfc * 0.1) + (test_hopper * 0.1) + (control_sueno * 0.1)
    return riesgo_lesion

# Interfaz de usuario con Streamlit
st.title("Aplicación de Control de Cargas para Futbolistas")

archivo_csv = st.file_uploader("Sube el archivo CSV de datos del WIMU Pro GPS", type=["csv"])

if archivo_csv:
    datos = cargar_datos(archivo_csv)
    distancia, velocidad, aceleraciones = calcular_carga_externa(datos)
    
    peso = st.number_input("Introduce el peso del jugador (kg)")
    gasto_energetico = calcular_gasto_energetico(distancia, peso)
    
    escala_borg = st.number_input("Introduce la escala de Borg", min_value=0, max_value=10, step=1)
    vfc = st.number_input("Introduce la variabilidad de la frecuencia cardiaca")
    test_hopper = st.number_input("Introduce el resultado del test de Hopper", min_value=0, max_value=100, step=1)
    control_sueno = st.number_input("Introduce el control del sueño", min_value=0, max_value=10, step=1)
    
    estado_de_forma = calcular_estado_de_forma(distancia, velocidad, aceleraciones)
    riesgo_lesion = evaluar_riesgo_de_lesion(distancia, escala_borg, vfc, test_hopper, control_sueno)
    
    st.write(f"Carga Externa: {distancia:.2f} m, {velocidad:.2f} m/s, {aceleraciones:.2f} aceleraciones")
    st.write(f"Gasto Energético: {gasto_energetico:.2f} kcal")
    st.write(f"Estado de Forma: {estado_de_forma:.2f}")
    st.write(f"Riesgo de Lesión: {riesgo_lesion:.2f}")
    st.write(f"Escala de Borg: {escala_borg}, VFC: {vfc}, Test de Hopper: {test_hopper}, Control del Sueño: {control_sueno}")

    st.line_chart(datos[['distancia', 'velocidad', 'aceleraciones']])
