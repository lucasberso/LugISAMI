#
# Authors:
# Pablo Arcediano,
# Lucas Bernacer Soriano,
# Ángela Blazquez,
# Héctor Dionisio,
# Javier Vela
#
# Copyright (c) 2021, Altran
#

import zipfile
import os.path
import shutil

def extract_file(input_file):
    """
    Extrae un archivo de entrada en una carpeta creada con su nombre + "_extracted".
    """
    clean_filename, filename = os.path.splitext(input_file)[0], os.path.basename(input_file)
    extraction_path = clean_filename + '_extracted'
    if os.path.exists(extraction_path): # Creación de la carpeta de extracción.
        print('Eliminada carpeta: %s' % extraction_path)
        shutil.rmtree(extraction_path)

    with zipfile.ZipFile(input_file, 'r') as z: # Descomprime el archivo de entrada en la nueva carpeta.
        z.extractall(extraction_path)
    print('Se ha descomprimido %s en: %s' % (filename , extraction_path))
    return extraction_path # Proporciona la ruta donde se han extraido los ficheros.

def find_extension(filepath, file_extension):
    """
    Busca en un directorio archivos con la extensión proporcionada. Devuelve una lista con las rutas de los archivos.
    """
    out_path = []
    for root, dirs, files in os.walk(filepath):
        for name in files: # Bucle a lo largo de los archivos en los directorios.
            filename, extension = os.path.splitext(name)
            if extension == file_extension: # Comprueba la extensión de cada archivo.
               out_path.append(os.path.join(root, name).replace("\\","/")) # Almacena la ruta de los archivos coincidentes.
    print('%d archivo/s con extensión %s encontrado/s en la carpeta: %s' % (len(out_path), file_extension, filepath))
    if out_path: # Proporciona la lista de rutas en caso de encontrar archivos con la misma extensión.
        return out_path