import pandas as pd
import xml.etree.ElementTree as ET

def parse_cre_xml(file_path):
    # 1. Cargar y parsear el archivo XML
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    data = []
    
    # 2. Iterar sobre cada estación (nodo 'place')
    for place in root.findall('place'):
        place_id = place.get('id')
        name = place.find('name').text if place.find('name') is not None else "N/A"
        cre_id = place.find('cre_id').text if place.find('cre_id') is not None else "N/A"
        
        # Extraer coordenadas del sub-nodo 'location'
        location = place.find('location')
        if location is not None:
            lon = location.find('x').text if location.find('x') is not None else None
            lat = location.find('y').text if location.find('y') is not None else None
        else:
            lon, lat = None, None
            
        data.append({
            'id': place_id,
            'nombre': name.strip() if name else "N/A",
            'cre_id': cre_id.strip() if cre_id else "N/A",
            'latitud': float(lat) if lat else None,
            'longitud': float(lon) if lon else None
        })
    
    # 3. Convertir a DataFrame de Pandas
    df = pd.DataFrame(data)
    
    # 4. Limpieza básica: Eliminar filas sin coordenadas (no nos sirven para el mapa)
    df = df.dropna(subset=['latitud', 'longitud'])
    
    return df

# Ejecutar el proceso
if __name__ == "__main__":
    print("Leyendo archivo XML...")
    df_gasolineras = parse_cre_xml('data/estaciones.xml')
    
    print(f"Proceso terminado. Se encontraron {len(df_gasolineras)} estaciones con coordenadas.")
    
    # Guardar a CSV para los siguientes pasos
    df_gasolineras.to_csv('data/gasolineras_limpio.csv', index=False)
    print("Archivo 'gasolineras_limpio.csv' generado con éxito.")
    
    # Mostrar las primeras filas para verificar
    print(df_gasolineras.head())