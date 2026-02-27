# Gas Stations Locator México (CRE Data)
> **Geolocalizador de estaciones de gasolina en México**

-img-

---

## Overview / Resumen
**EN:** This project is a specialized Data Engineering tool that extracts gas station data from the Mexican Energy Regulatory Commission (CRE) via XML, processes it using Python/Pandas, and visualizes it through an interactive Streamlit web application. It features real-time distance calculation and interactive mapping.

**ES:** Este proyecto es una herramienta de Ingeniería de Datos que extrae información de estaciones de servicio de la Comisión Reguladora de Energía (CRE) mediante XML, la procesa con Python/Pandas y la visualiza en una aplicación web interactiva con Streamlit. Incluye cálculo de distancias en tiempo real y mapas interactivos.

---

## Key Features / Características Principales
**EN:**

* **ETL Pipeline**: Automated parsing of complex XML data into clean CSV formats.

* **Geospatial Analysis:** Real-time geocoding using Nominatim (OpenStreetMap) and Haversine distance calculations.

* **Dockerized Deployment:** Fully containerized application for consistent performance across any environment.

**ES:**

* **Pipeline ETL:** Procesamiento automatizado de datos XML complejos a formatos CSV limpios.

* **Análisis Geoespacial:** Geocodificación en tiempo real usando Nominatim y cálculos de distancia geodésica.

* **Despliegue Dockerizado:** Aplicación completamente contenedorizada para asegurar su funcionamiento en cualquier entorno.

-gif-

---

## Tech Stack / Tecnologías
**EN:** Python (Pandas, Geopy), Streamlit, Folium (Maps), Docker, XML Parsing.

**ES:** Python (Pandas, Geopy), Streamlit, Folium (Mapas), Docker, Parsing de XML.

---

## How to Run / Cómo Ejecutar
**EN:**

1. Clone the repo: ```git clone https://github.com/AbrahamRodriguez97/gas-stations-mexico-location.git```
2. Build Docker image: ```docker build -t gas-app .```
3. Run container: ```docker run -p 8501:8501 gas-app```

**ES:**

1. Clona el repo: ```git clone https://github.com/AbrahamRodriguez97/gas-stations-mexico-location.git```
2. Construye la imagen: ```docker build -t gas-app .```
3. Corre el contenedor: ```docker run -p 8501:8501 gas-app```

-console-

---
