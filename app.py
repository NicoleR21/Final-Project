import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Portafolio - Nicole Rojas Conde", layout="wide")



df = pd.read_csv('Dataset.csv')

st.title("Análisis de Licencias de Cannabis - Nicole Stephanie Rojas Conde")
st.markdown("""
    *Abogada - https://www.linkedin.com/in/nicole-rojas-conde-457a65339?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app*  
    Bienvenido a mi portafolio interactivo de análisis de datos. 
    Este gráfico muestra la evolución de las licencias otorgadas y solicitudes de licencias de cannabis.
""")

ordered=True

# Crear gráfico de barras
try:
    unique_years = df["Año"].unique()
    for year in unique_years:
        fig, ax = plt.subplots(figsize=(8, 6))
        df_year = df[df["Año"] == year]
        
        ax.bar(df_year["Mes"], df_year["Cantidad total de Licencias Otorgadas (por primera vez)"], 
               color="green", label=f"Licencias Otorgadas ({year})")
        
        ax.set_xlabel("Mes")
        ax.set_ylabel("Cantidad de Licencias")
        ax.set_title(f"Licencias Otorgadas por Mes en {year}")
        ax.grid(axis="y")
        ax.legend()
        
        # Cambiar orientación de las etiquetas en el eje X a vertical
        ax.set_xticks(range(len(df_year["Mes"])))
        ax.set_xticklabels(df_year["Mes"], rotation=90, ha="center")
        
        # Mostrar gráfico en Streamlit
        st.pyplot(fig)
except Exception as e:
    st.error(f"Se produjo un error al generar los gráficos: {e}")

# Mostrar tabla de datos en la aplicación
st.write("### Dataset Utilizado")
st.dataframe(df)
