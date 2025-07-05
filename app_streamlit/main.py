'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import altair as alt

st.title("RECOMENDACIÓN DE MANTENIMIENTO PREDICTIVO")
#return pd.read_csv("datos_ver.csv", delimiter=',')

st.set_page_config(layout="wide")
st.title("📊 DATOS A TIEMPO REAL")

@st.cache_data
def load_data():
    return pd.read_csv("datos_ver.csv", delimiter=',')

df = load_data()


import streamlit as st


# — Definición de descripciones (inglés y español)
DESCRIPCIONES = {
    "id": ("Engine ID", "ID del motor"),
    "cycle": ("Time cycle / operating cycle", "Ciclo de operación"),
    "s2": ("LPC outlet temperature", "Temperatura salida compresor baja presión"),
    "s3": ("HPC outlet temperature", "Temperatura salida compresor alta presión"),
    "s4": ("LPT outlet temperature", "Temperatura salida turbina baja presión"),
    "s7": ("HPC outlet pressure", "Presión salida compresor alta presión"),
    "s8": ("Physical fan speed", "Velocidad física del ventilador"),
    "s11": ("Static pressure at HPC outlet", "Presión estática salida compresor alta presión"),
    "s12": ("Fuel flow / Ps30", "Flujo de combustible relativo a Ps30"),
    "s13": ("Corrected fan speed", "Velocidad corregida del ventilador"),
    "s14": ("Corrected core speed", "Velocidad corregida del núcleo"),
    "s15": ("Bypass ratio", "Relación de bypass"),
    "s17": ("Bleed enthalpy", "Entalpía del sangrado"),
    "s20": ("HPT coolant bleed", "Flujo de refrigerante turbina alta presión"),
    "s21": ("LPT coolant bleed", "Flujo de refrigerante turbina baja presión"),
    "RUL": ("Remaining Useful Life", "Vida útil restante"),
    "label1": ("OK or Imminent Failure (binary)", "Etiqueta OK o fallo inminente"),
    "label2": ("OK, Moderate, or Critical", "Etiqueta OK, Moderado o Crítico")
}

# — Barra lateral: configuración y descripciones
st.sidebar.header("🔧 Configuración")
seleccion = st.sidebar.multiselect(
    "Variables a graficar", options=df.columns.tolist(), default=["s4", "s11", "s20"]
)
window_size = st.sidebar.slider("Tamaño de ventana X", 10, 500, 100, 10)
delay = st.sidebar.slider("Delay (segundos)", 0.0, 1.0, 0.2, 0.05)

# Mostrar descripciones en sidebar
if seleccion:
    st.sidebar.markdown("### 🧠 Descripción de variables")
    for var in seleccion:
        en, es = DESCRIPCIONES.get(var, ("", "Sin descripción"))
        st.sidebar.markdown(f"**{var}** — {en} — {es}")

# — Streaming de datos con gráfico y tabla
if seleccion:
    chart_placeholder = st.empty()
    table_placeholder = st.empty()

    for i in range(len(df)):
        start = max(0, i - window_size + 1)
        slice_df = df.iloc[start:i+1][seleccion].copy()
        slice_df.index = df.iloc[start:i+1].index  # índice original

        # Gráfico Altair con control de dominio X
        slice_reset = slice_df.reset_index().rename(columns={"index": "idx"})
        chart = alt.Chart(slice_reset).transform_fold(
            seleccion, as_=['variable', 'valor']
        ).mark_line().encode(
            alt.X('idx:Q', scale=alt.Scale(domain=[start, start + window_size - 1]), title='Índice'),
            alt.Y('valor:Q', title='Valor'),
            color='variable:N'
        ).properties(width=700, height=400)

        chart_placeholder.altair_chart(chart, use_container_width=True)

        window_df = df.iloc[start:i+1][["cycle"] + seleccion]
        table_placeholder.dataframe(window_df)

        time.sleep(delay)

   #-----------------------------------------------------------------------------------    
       #MENSAJE



# Definir descripciones de estados
ESTADOS = {
    0: ("OK", "Estado óptimo del motor"),
    1: ("Moderado", "Mantenimiento recomendado"),
    2: ("Crítico", "Mantenimiento necesario")
}

# Configuración de ventana
window_size = 100
delay = 0.2

# Iterar sobre los datos
for i in range(len(df)):
    # Obtener el valor de label2
    label2_value = df.iloc[i]["label2"]

    # Obtener el mensaje de estado correspondiente
    estado, descripcion = ESTADOS.get(label2_value, ("Desconocido", "Estado no definido"))

    # Mostrar el mensaje de estado en la cabecera
    st.header(f"Estado del motor: **{estado}**")
    st.subheader(descripcion)

    # Graficar los datos
    start = max(0, i - window_size + 1)
    slice_df = df.iloc[start:i+1][["cycle", "s4", "s11", "s20"]].copy()
    slice_df.index = df.iloc[start:i+1].index  # Índice original

    # Crear gráfico
    chart = alt.Chart(slice_df.reset_index()).mark_line().encode(
        x='cycle:Q',
        y='s4:Q',
        color='variable:N'
    ).transform_fold(
        ['s4', 's11', 's20'],
        as_=['variable', 'valor']
    ).properties(width=700, height=400)

    # Mostrar gráfico
    st.altair_chart(chart, use_container_width=True)

    # Esperar antes de la siguiente iteración
    time.sleep(delay)
'''
import streamlit as st
import pandas as pd
import time
import altair as alt

st.set_page_config(layout="wide")
st.title("📊 RECOMENDACIÓN DE MANTENIMIENTO PREDICTIVO")

@st.cache_data
def load_data():
    return pd.read_csv("datos_ver.csv", delimiter=",")

df = load_data()

# Descripciones solo en español
DESCRIP_ES = {
    "s4": "Temperatura salida turbina baja presión",
    "s11": "Presión estática salida compresor alta presión",
    "s20": "Flujo de refrigerante turbina alta presión"
}

import streamlit as st
import pandas as pd
import time
import altair as alt

st.set_page_config(layout="wide")
st.title("📊 RECOMENDACIÓN DE MANTENIMIENTO PREDICTIVO")

@st.cache_data
def load_data():
    return pd.read_csv("datos_ver.csv", delimiter=",")

df = load_data()

# Descripciones en español
DESCRIP_ES = {
    "s4": "Temperatura salida turbina baja presión",
    "s11": "Presión estática salida compresor alta presión",
    "s20": "Flujo de refrigerante turbina alta presión"
}

# Estados según label2
ESTADOS = {
    0: ("OK", "Estado óptimo"),
    1: ("Moderado", "Mantenimiento recomendado"),
    2: ("Crítico", "Mantenimiento necesario")
}

# Sidebar: configuración
sel = st.sidebar.multiselect("Variables a graficar", df.columns.tolist(), default=["s4","s11","s20"])
window = st.sidebar.slider("Ventana (valores X)", 10, 500, 100, step=10)
delay = st.sidebar.slider("Delay entre steps (seg)", 0.0, 1.0, 0.2, step=0.05)

# Mostrar descripciones en español
if sel:
    st.sidebar.markdown("### 🧠 Descripción de variables")
    for v in sel:
        desc = DESCRIP_ES.get(v, "Sin descripción en español")
        st.sidebar.markdown(f"**{v}** — {desc}")

# Métricas (solo Moderado y Crítico)
col_mod, col_cri = st.columns(2)
m_mod = col_mod.metric("Moderado", "0")
m_cri = col_cri.metric("Crítico", "0")

# Placeholders
header = st.empty()
chart_ph = st.empty()
table_ph = st.empty()

# Contadores
c_mod = c_cri = 0

for i in range(len(df)):
    label = int(df.at[i, "label2"])
    estado, desc = ESTADOS[label]

    # Actualizar métricas
    if label == 1:
        c_mod += 1
        m_mod.metric("Moderado", str(c_mod))
    elif label == 2:
        c_cri += 1
        m_cri.metric("Crítico", str(c_cri))

    # Mensaje en cabecera
    header.markdown(f"<h2 style='text-align:center'>{estado} — {desc}</h2>", unsafe_allow_html=True)

    # Ventana del gráfico
    start = max(0, i - window + 1)
    df_slice = df.iloc[start:i+1][sel].copy()
    df_slice.reset_index(inplace=True)

    chart = alt.Chart(df_slice).transform_fold(
        sel, as_=["variable", "valor"]
    ).mark_line().encode(
        x=alt.X("index:Q", scale=alt.Scale(domain=[start, start+window-1]), title="Índice"),
        y=alt.Y("valor:Q", title="Valor"),
        color="variable:N"
    ).properties(width=800, height=400)

    chart_ph.altair_chart(chart, use_container_width=True)
    table_ph.dataframe(df.iloc[start:i+1][["cycle"] + sel])

    time.sleep(delay)
