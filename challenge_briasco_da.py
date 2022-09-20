# Para la creación de carpetas
import os
import pandas as pd
import requests

# Direccion de descarga
carpeta_descarga = 'C:/Users/maria/Desktop/challenge_alkemy/'

# Creación de las direcciones de descarga y asignación de nombre de los archivos.
dir_museo = carpeta_descarga + 'museos/2022-junio/'
nombre_archivo_museos = 'museos-30-06-2022.csv'
if not os.path.exists(dir_museo):
    os.makedirs(dir_museo)

dir_cine = carpeta_descarga + 'cine/2022-junio/'
nombre_archivo_cine = 'cine-30-06-2022.csv'
if not os.path.exists(dir_cine):
    os.makedirs(dir_cine)

dir_biblioteca = carpeta_descarga + 'bibliotecas/2022-junio/'
nombre_archivo_bibliotecas = 'bibliotecas-30-06-2022.csv'
if not os.path.exists(dir_biblioteca):
    os.makedirs(dir_biblioteca)

direcciones_archivos = [dir_museo + nombre_archivo_museos, dir_cine + nombre_archivo_cine,
                        dir_biblioteca + nombre_archivo_bibliotecas]

# Links de descargas
url_museos = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a' \
             '-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'
url_cine = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-' \
           'fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
url_biblioteca = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-' \
                 'fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'


# Función para descargar las bases de datos con dirección de descarga y nombre.
def descarga_base_datos(
        link_descarga, direccion_descarga,
        nombre_descarga):
    path_final = direccion_descarga + nombre_descarga
    desc = requests.get(link_descarga)
    desc.encoding = 'utf-8'
    with open(path_final, 'wb') as f:
        f.write(desc.content)

# Descarga de bases de datos


descarga_base_datos(url_museos,dir_museo,nombre_archivo_museos)
descarga_base_datos(url_cine,dir_cine,nombre_archivo_cine)
descarga_base_datos(url_biblioteca,dir_biblioteca,nombre_archivo_bibliotecas)

# Procesamiento de datos.

csv_museo = pd.read_csv(dir_museo + nombre_archivo_museos)

csv_cine = pd.read_csv(dir_cine + nombre_archivo_cine)

csv_biblioteca = pd.read_csv(dir_biblioteca + nombre_archivo_bibliotecas)

# Renombramiento de las columnas
# Podría haberse hecho con una función que se encargue de hacerlo automáticamente para optimizar el proceso.
renom_col_museo = {
    'Cod_Loc': 'cod_localidad',
    'IdProvincia': 'id_provincia',
    'IdDepartamento': 'id_departamento',
    'direccion': 'domicilio',
    'categoria': 'categoría',
    'CP': 'código postal',
    'telefono': 'número de teléfono',
    'Mail': 'mail',
    'Web': 'web',
}
renom_col_cine = {
    'Cod_Loc': 'cod_localidad',
    'IdProvincia': 'id_provincia',
    'IdDepartamento': 'id_departamento',
    'Categoría': 'categoría',
    'Provincia': 'provincia',
    'Localidad': 'localidad',
    'Dirección': 'domicilio',
    'CP': 'código postal',
    'Teléfono': 'número de teléfono',
    'Mail': 'mail'
}
renom_col_bibliotecas = {
    'Cod_Loc': 'cod_localidad',
    'IdProvincia': 'id_provincia',
    'IdDepartamento': 'id_departamento',
    'Categoría': 'categoría',
    'Provincia': 'provincia',
    'Localidad': 'localidad',
    'Dirección': 'domicilio',
    'CP': 'código postal',
    'Teléfono': 'número de teléfono',
    'Mail': 'mail'
}
csv_museo = csv_museo.rename(columns = renom_col_museo)
csv_cine = csv_cine.rename(columns = renom_col_cine)
csv_biblioteca = csv_biblioteca.rename(columns = renom_col_bibliotecas)

# Creación de única tabla con renombres
# Armo una lista para contener los csv.
tabla_salida = list()
tabla_salida.append(csv_biblioteca)
tabla_salida.append(csv_cine)
tabla_salida.append(csv_museo)
# Tomo la lista y genero una sola para guardarla en la dirección especificada.
ruta_salida = carpeta_descarga + 'Tabla_Salida.csv'
pd.concat(tabla_salida,axis = 0).to_csv(ruta_salida)