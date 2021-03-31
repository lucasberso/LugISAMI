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

import os.path
from bs4 import BeautifulSoup
from wrappers import extract_file

class lugHTML():
    """
    Clase desarrollada para trabajar con el html proporcionado por ISAMI.

    """
    def __init__(self, filepath, filename):
        """
        Inicializa el archivo de entrada con nombre y ruta. Comprobación del tipo de fichero.

        filepath: Ruta del fichero de entrada.
        filename: Nombre del fichero de entrada.

        """
        self.filepath, self.filename = filepath, filename
        self.input_file = self.filepath + '/' + self.filename # Ruta completa del archivo.
        self.parsed_html = None # Información almacenada en el archivo html.
        clean_filename, self.file_extension = os.path.splitext(self.input_file)
        if self.file_extension not in ('.html', '.czm'): # Comprueba si el tipo de archivo suministrado es adecuado.
            raise IOError('Extensión no soportada. Por favor, proporcione un archivo czm o html.')

    def extract_parse_html(self):
        """
        Obtiene los datos almacenados en el fichero html. En caso de proporcionar un fichero czm, lo descomprime
        y localiza el correspondiente html.

        """
        self.html_path = None # Ruta del archivo html de lectura.
        if self.file_extension == '.czm': # Caso de fichero comprimido czm.
            folder_path = extract_file(self.filepath, self.filename) # Descomprime el archivo de entrada.
            for root, dirs, files in os.walk(folder_path): # Búsqueda del html almacenado dentro del czm.
                for name in files: # Bucle a lo largo de los archivos en los directorios.
                    filename, file_extension = os.path.splitext(name)
                    if file_extension == '.html': # Comprueba la extensión de cada archivo.
                        self.html_path = os.path.join(root, name)
            if self.html_path is None: # Error en caso de no encontrar un archivo html.
                raise IOError('Archivo html no encontrado en la carpeta: %s' % folder_path)
        else: # Caso con html proporcionado directamente.
            self.html_path = self.filepath/self.filename
        html_file = open(self.html_path, encoding="utf8") # Almacena los datos del html.
        self.parsed_html = BeautifulSoup(html_file, "html.parser")

    def find_kt(self):
        """
        Busca dentro del fichero html la información correspondiente a los factores de intensidad de esfuerzos.

        """
        if not self.parsed_html: # Obtiene la información del archivo html en caso de no haberla obtenido previamente.
            self.extract_parse_html()
        tag = self.parsed_html.findAll('th') # Recupera las etiquetas tipo th del archivo html.
        kt_value = None
        for i in range(0, len(tag)): # Itera a lo largo de las etiquetas th.
            if tag[i].string[0:2] == 'Kt': # Busca la etiqueta th correspondiente al kt.
                kt_value = float(tag[i].next_sibling.contents[0])
        if kt_value is None: # Informa en caso de que no haya almacenado ningún valor de kt.
            print("Valor de Kt no encontrado.")
        return kt_value