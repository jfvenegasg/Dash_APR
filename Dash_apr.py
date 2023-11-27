#from collections import namedtuple
#import altair as alt
import math
import pandas as pd
import streamlit as st
import streamlit_option_menu as menu
import os
import plotly.express as px
import folium 
from folium import plugins
from streamlit_folium import st_folium


st.set_page_config(layout="wide")



with st.sidebar:
    selected = menu.option_menu("Dash APR", ["Inicio","Ubicaciones","Analisis de beneficiarios"], 
        icons=['house', 'person-rolodex','person-rolodex'], menu_icon="cast", default_index=0)
    selected

if selected == "Inicio":
    st.title("Análisis geográfico para sistemas de agua potable rural en la región de los Ríos")

    #c=st.empty()
    #c.image("docker_1.png")

if selected == "Ubicaciones":
    
    col1,col2= st.columns(2)        
    map = folium.Map(location = [-39.925826, -73.114501], tiles = "OpenStreetMap", zoom_start = 10)

    #Acá estoy cargando el set de datos de la carpeta de documentos.
    datos = pd.read_excel('base_ssr.xlsx', sheet_name='Sistemas_APR',usecols="B:U",skiprows=2)

    #Valdivia
    datos_nombres_valdivia=list(datos.iloc[1963:1977,12])
    datos_lat_valdivia=datos.iloc[1963:1977,19] 
    datos_long_valdivia=datos.iloc[1963:1977,18]

    #Paillaco
    datos_nombres_paillaco=list(datos.iloc[1919:1930,12])
    datos_lat_paillaco=datos.iloc[1919:1930,19] 
    datos_long_paillaco=datos.iloc[1919:1930,18]

    #Los Lagos
    datos_nombres_loslagos=list(datos.iloc[1885:1903,12])
    datos_lat_loslagos=datos.iloc[1885:1903,19] 
    datos_long_loslagos=datos.iloc[1885:1903,18]

    #Corral
    datos_nombres_corral=list(datos.iloc[1873:1879,12])
    datos_lat_corral=datos.iloc[1873:1879,19] 
    datos_long_corral=datos.iloc[1873:1879,18]

    #Creación del par de coordenadas
    locations_valdivia = list(zip(datos_lat_valdivia, datos_long_valdivia))
    locations_paillaco = list(zip(datos_lat_paillaco, datos_long_paillaco))
    locations_loslagos = list(zip(datos_lat_loslagos, datos_long_loslagos))
    locations_corral = list(zip(datos_lat_corral, datos_long_corral))


    #Creación de las listas
    nombres = datos_nombres_valdivia+datos_nombres_paillaco+datos_nombres_loslagos+datos_nombres_corral
    locations=locations_valdivia+locations_paillaco+locations_loslagos+locations_corral

    #Acá agregamos un marcador con la ubicación de los punto APR
    for i in range(len(locations)):
        nombre=nombres[i]
        folium.Marker(location=locations[i],tooltip=nombre).add_to(map)
        
    for i in range(len(locations)):
        folium.CircleMarker(location=locations[i],radius=5).add_to(map)
    

    # Aáa estoy agregando un minimap en la esquina,para esto hay que cargar la función plugins desde la libreria folium
    minimap = plugins.MiniMap(position="bottomleft",toggle_display=True)
    map.add_child(minimap)
    st_folium(map, width=1200, height=550)    

if selected == "Analisis de beneficiarios":

    df1=pd.DataFrame()