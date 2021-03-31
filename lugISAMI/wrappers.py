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

def extract_file(filepath, filename):
    """
    Extrae un archivo de entrada en una carpeta creada con su nombre + "_extracted".
    """
    clean_filename, file_extension = os.path.splitext(filename)
    extraction_path = filepath / clean_filename + '_extracted'
    if os.path.exists(extraction_path):
        print('Eliminada carpeta: %s' % extraction_path)
        shutil.rmtree(extraction_path)

    with zipfile.ZipFile(filepath / filename, 'r') as z:
        z.extractall(extraction_path)
    print('Se ha descomprimido %s en: %s' % (filename, extraction_path))
    return extraction_path
