#
# Authors:
# Pablo Arcediano,
# Lucas Bernacer Soriano,
# Ángela Blazquez,
# Héctor Dionisio,
# Javier Vela
#
# Copyright (c) 2021, Capgemini Engineering
#

from zipfile import ZipFile
import os.path
from shutil import rmtree

def extract_file(input_file):
    """
    Extrae un archivo de entrada en una carpeta creada con su nombre + "_extracted".
    """
    clean_filename, filename = os.path.splitext(input_file)[0], os.path.basename(input_file)
    extraction_path = clean_filename + '_extracted'
    if os.path.exists(extraction_path): # Creación de la carpeta de extracción.
        print('Deleted folder: %s' % extraction_path)
        rmtree(extraction_path)

    with ZipFile(input_file, 'r') as z: # Descomprime el archivo de entrada en la nueva carpeta.
        z.extractall(extraction_path)
    print('Unzipped %s in: %s' % (filename , extraction_path))
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
    print('%d file/s with extension %s has/have been found in: %s' % (len(out_path), file_extension, filepath))
    if out_path: # Proporciona la lista de rutas en caso de encontrar archivos con la misma extensión.
        return out_path

def read_sheet(initial_row, initial_column, header_row, name_sheet, book):
    """
    Obtiene de la hoja seleccionada por el usuario todos los datos encerrados por el rango de datos.

    initial_row: Fila inicial de comienzo los datos.
    initial_column: Columna inicial de comienzo los datos.
    header_row: Fila con el nombre de los campos a almacenar.
    name_sheet: Nombre de la hoja de datos.

    """
    sheet = book[name_sheet]
    final_row = sheet.max_row
    final_column = sheet.max_column
    input_global = {}
    for i in range(initial_row, final_row + 1):
        name = sheet.cell(i, initial_column).value
        if name is None: # Se salta las filas vacías.
            continue
        aux_dict = {}
        for j in range(initial_column, final_column + 1):
            if sheet.cell(header_row, j).value is None: # Se salta las columnas vacías.
                continue
            key = sheet.cell(header_row, j).value
            value = sheet.cell(i, j).value
            aux_dict.update({key: value})
        input_global.update({name: aux_dict})
    return input_global