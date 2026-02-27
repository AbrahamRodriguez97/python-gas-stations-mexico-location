import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium
from streamlit_folium import st_folium

# Configuración de la página
st.set_page_config(page_title="Gasolineras MX", layout="wide")

st.title("Localizador de Gasolineras en México")
st.markdown("Busca las estaciones de servicio más cercanas a tu ubicación.")

# 1. Cargar datos (con caché para que sea rápido)
@st.cache_data
def load_data():
    return pd.read_csv('data/gasolineras_limpio.csv')

df = load_data()

# 2. Barra lateral para filtros
st.sidebar.header("Configuración de búsqueda")
direccion = st.sidebar.text_input("Ingresa tu dirección:", "Palacio de Bellas Artes, CDMX")
num_estaciones = st.sidebar.slider("Número de gasolineras a mostrar", 1, 20, 10)

if direccion:
    try:
        # 3. Geocodificación
        geolocator = Nominatim(user_agent="gasolineras_mx_app")
        location = geolocator.geocode(direccion)
        
        if location:
            user_coords = (location.latitude, location.longitude)
            
            # 4. Cálculo de distancias
            df['distancia_km'] = df.apply(
                lambda row: geodesic(user_coords, (row['latitud'], row['longitud'])).km, 
                axis=1
            )
            
            cercanas = df.sort_values(by='distancia_km').head(num_estaciones)
            
            # 5. Visualización
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.subheader(f"Top {num_estaciones} más cercanas")
                st.dataframe(cercanas[['nombre', 'distancia_km']].rename(columns={'nombre': 'Gasolinera', 'distancia_km': 'Distancia (km)'}))
            
            with col2:
                # Crear Mapa
                m = folium.Map(location=user_coords, zoom_start=14)
                folium.Marker(user_coords, popup="Tú estás aquí", icon=folium.Icon(color='blue')).add_to(m)
                
                for _, row in cercanas.iterrows():
                    folium.Marker(
                        location=[row['latitud'], row['longitud']],
                        popup=f"{row['nombre']} ({round(row['distancia_km'], 2)} km)",
                        icon=folium.Icon(color='red', icon='gas-pump', prefix='fa')
                    ).add_to(m)
                
                # Mostrar mapa en Streamlit
                st_folium(m, width=700, height=500)
        else:
            st.error("No se encontró la dirección. Intenta ser más específico (ej: agrega 'Mexico').")
            
    except Exception as e:
        st.error(f"Hubo un error: {e}")