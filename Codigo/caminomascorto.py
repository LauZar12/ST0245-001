##Camino mas corto
## Laura Danniela Zárate Guerrero
## Santiago Arias Higuita
import pandas as pd
import numpy as np
import networkx as nx
df = pd.read_csv("calles_de_medellin_con_acoso.csv", sep=';')
df.head()

KK = nx.from_pandas_edgelist(df,source='origin',target='destination',edge_attr='length')
##Profesor, de momento mostramos implementación que fue lo que se pidió para la segunda entrega, las coordenadas se ponen manualmente pero si funciona la busqueda y graficacion del camino.
djk_path= nx.dijkstra_path(KK, source='(-75.5728593, 6.2115169)', target='(-75.5739582, 6.2081811)', weight='length')
print(djk_path) 
from folium import plugins
import folium
import os
m = folium.Map ([6.2115169,-75.5728593 ], zoom_start = 10) 
location =[[6.2115169,-75.5728593 ], [6.2116756,-75.5732903], [6.211705, -75.5733588], [6.2109569, -75.5736973], [6.210466, -75.5738684], [6.2101752, -75.5739697], [6.2094339, -75.5742281], [6.2081811, -75.5739582]]
route = folium.PolyLine(location,color = 'red',weight = 3,opacity = 0.8).add_to (m)
##Si quiere probarlo por favor cambie la ruta donde se guarda el archivo en su computador.
m.save (os.path.join (r'C:\Users\DANNIELA\Desktop',' Heatmap4.html '))