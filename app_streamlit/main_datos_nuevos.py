import pandas as pd
import pickle
import time
import altair as alt
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(layout="wide")
st.title("📊 RECOMENDACIÓN DE MANTENIMIENTO PREDICTIVO")

# -----------------------------
# Cargar modelo entrenado
# -----------------------------
@st.cache_resource
def load_model():
    with open("../models/modelo_RandomForest.pkl", "rb") as f:
        return pickle.load(f)

# -----------------------------
# Cargar y procesar datos
# -----------------------------
@st.cache_data
def load_data_and_predict():
    df_raw = pd.read_csv("../data/raw/MANTENIMIENTO_PREDICTIVO_AVION/PM_test.csv")
    df_norma = df_raw.copy()

    # Normalizar
    var_excl = ['id', 'cycle']
    normalizar = df_raw.select_dtypes(include='number').columns.difference(var_excl)
    scaler = MinMaxScaler()
    df_norma[normalizar] = scaler.fit_transform(df_raw[normalizar])

    # Entradas para predicción
    drop_cols = ["id", "cycle", "setting1", "setting2", "setting3", "s1",
                 "s5", "s6", "s9", "s10", "s16", "s18", "s19"]
    X_nuevo = df_norma.drop(columns=drop_cols, errors='ignore')

    # Modelo y predicción
    modelo = load_model()
    df_norma["pred_label2"] = modelo.predict(X_nuevo)
    df_norma["pred_proba"] = modelo.predict_proba(X_nuevo).max(axis=1)

    return df_norma

# -----------------------------
# Cargar datos normalizados con predicciones
# -----------------------------
df = load_data_and_predict()

# -----------------------------
# Diccionarios
# -----------------------------
DESCRIP_ES = {
    "id": "ID del motor",
    "cycle": "Ciclo de operación",
    "s2": "Temperatura salida compresor baja presión",
    "s3": "Temperatura salida compresor alta presión",
    "s4": "Temperatura salida turbina baja presión",
    "s7": "Presión salida compresor alta presión",
    "s8": "Velocidad física del ventilador",
    "s9": "Presión del ventilador",
    "s11": "Presión estática salida compresor alta presión",
    "s12": "Flujo de combustible relativo a Ps30",
    "s13": "Velocidad corregida del ventilador",
    "s14": "Velocidad corregida del núcleo",
    "s15": "Relación de bypass",
    "s17": "Entalpía del sangrado",
    "s20": "Flujo de refrigerante turbina alta presión",
    "s21": "Flujo de refrigerante turbina baja presión",
    "RUL": "Vida útil restante",
    "label1": "Etiqueta OK o fallo inminente",
    "label2": "Etiqueta original",
    "pred_label2": "Predicción del modelo"
}

ESTADOS = {
    0: ("🟢 OK", "Estado óptimo"),
    1: ("🟡 Moderado", "Mantenimiento recomendado"),
    2: ("🔴 Crítico", "Mantenimiento urgente")
}

# -----------------------------
# Sidebar
# -----------------------------
sel = st.sidebar.multiselect("Variables a graficar", df.columns.tolist(), default=["s4", "s11", "s20", "pred_label2"])
window = st.sidebar.slider("Ventana (valores X)", 10, 500, 100, step=10)
delay = st.sidebar.slider("Delay entre pasos (seg)", 0.0, 1.0, 0.2, step=0.05)

if sel:
    st.sidebar.markdown("### 🧠 Descripción de variables")
    for v in sel:
        desc = DESCRIP_ES.get(v, "Sin descripción")
        st.sidebar.markdown(f"**{v}** — {desc}")

# -----------------------------
# Visualización
# -----------------------------
header = st.empty()
chart_ph = st.empty()
table_ph = st.empty()

for i in range(len(df)):
    label = int(df.at[i, "pred_label2"])
    prob = df.at[i, "pred_proba"]
    estado, desc = ESTADOS[label]

    # Estado con probabilidad
    header.markdown(
        f"<h2 style='text-align:center'>{estado} — {desc} (Probabilidad: {prob*100:.1f}%)</h2>",
        unsafe_allow_html=True
    )

    # Ventana de datos
    start = max(0, i - window + 1)
    df_slice = df.iloc[start:i+1].reset_index()

    # Gráfico
    chart = alt.Chart(df_slice).transform_fold(
        sel, as_=["variable", "valor"]
    ).mark_line().encode(
        x=alt.X("index:Q", title="Índice"),
        y=alt.Y("valor:Q", title="Valor (normalizado)"),
        color="variable:N"
    ).properties(width=800, height=400)

    chart_ph.altair_chart(chart, use_container_width=True)

    # Tabla de datos normalizados
    table_ph.dataframe(df.iloc[start:i+1][["cycle"] + sel])

    time.sleep(delay)

