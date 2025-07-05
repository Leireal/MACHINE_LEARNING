import pandas as pd
import pickle
import time
import altair as alt
import streamlit as st

st.set_page_config(layout="wide")
st.title("📊 RECOMENDACIÓN DE MANTENIMIENTO PREDICTIVO")

# -----------------------------
# Cargar modelo entrenado
# -----------------------------
@st.cache_resource
def load_model():
    with open("../models/modelo_RandomForest.pkl", "rb") as f:
        modelo = pickle.load(f)
    return modelo

# -----------------------------
# Cargar datos y hacer predicción
# -----------------------------
@st.cache_data
def load_data_and_predict():
    df = pd.read_csv("../data/processed/datos_treal.csv")

    # Preprocesamiento: eliminar columnas no usadas por el modelo
    X_nuevo = df.drop(columns=["id", "cycle"], errors='ignore')

    # Cargar modelo y predecir
    modelo = load_model()
    df["pred_label2"] = modelo.predict(X_nuevo)

    return df

df = load_data_and_predict()

# -----------------------------
# Diccionarios para visualización
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
# Sidebar de configuración
# -----------------------------
sel = st.sidebar.multiselect("Variables a graficar", df.columns.tolist(), default=["s4", "s11", "s20"])
window = st.sidebar.slider("Ventana (valores X)", 10, 500, 100, step=10)
delay = st.sidebar.slider("Delay entre pasos (seg)", 0.0, 1.0, 0.2, step=0.05)

# Mostrar descripciones de variables
if sel:
    st.sidebar.markdown("### 🧠 Descripción de variables")
    for v in sel:
        desc = DESCRIP_ES.get(v, "Sin descripción")
        st.sidebar.markdown(f"**{v}** — {desc}")

# -----------------------------
# Contadores y visualización
# -----------------------------
header = st.empty()
chart_ph = st.empty()
table_ph = st.empty()

c_mod = c_cri = 0

for i in range(len(df)):
    label = int(df.at[i, "pred_label2"])
    estado, desc = ESTADOS[label]

    # Actualizar métricas
    if label == 1:
        c_mod += 1
    elif label == 2:
        c_cri += 1

    # Mostrar estado actual
    header.markdown(f"<h2 style='text-align:center'>{estado} — {desc}</h2>", unsafe_allow_html=True)

    # Datos para graficar
    start = max(0, i - window + 1)
    df_slice = df.iloc[start:i+1][sel].copy()
    df_slice.reset_index(inplace=True)

    chart = alt.Chart(df_slice).transform_fold(
        sel, as_=["variable", "valor"]
    ).mark_line().encode(
        x=alt.X("index:Q", scale=alt.Scale(domain=[start, start + window - 1]), title="Índice"),
        y=alt.Y("valor:Q", title="Valor"),
        color="variable:N"
    ).properties(width=800, height=400)

    chart_ph.altair_chart(chart, use_container_width=True)
    table_ph.dataframe(df.iloc[start:i+1][["cycle"] + sel])

    time.sleep(delay)
