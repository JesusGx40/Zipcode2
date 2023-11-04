import pandas as pd
import os
import django
from .models import Registros
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

def importar_datos_desde_excel(ruta_archivo):
    
    # Lee el archivo de Excel
    datos_excel = pd.read_excel(ruta_archivo)

    # Itera sobre cada fila y guarda los datos en la base de datos
    for index, fila in datos_excel.iterrows():
        codigo_postal = Registros(
            d_codigo=fila['d_codigo'],
            d_asenta=fila['d_asenta'],
            d_tipo_asenta=fila['d_tipo_asenta'],
            d_mnpio=fila['d_mnpio'],
            d_estado=fila['d_estado'],
            d_ciudad=fila['d_ciudad'],
            d_CP=fila['d_CP'],
            c_estado=fila['c_estado'],
            c_oficina=fila['c_oficina'],
            c_CP=fila['c_CP'],
            c_tipo_asenta=fila['c_tipo_asenta'],
            c_mnpio=fila['c_mnpio'],
            id_asenta_cpcons=fila['id_asenta_cpcons'],
            d_zona=fila['d_zona'],
            c_cve_ciudad=fila['c_cve_ciudad']
        )
        codigo_postal.save()


importar_datos_desde_excel('datos/NL.xls')