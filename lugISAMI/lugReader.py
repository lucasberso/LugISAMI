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
from wrappers import find_extension

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
        self.parsed_html, self.html_path = None, None # Información almacenada en el archivo html y ruta.
        clean_filename, self.file_extension = os.path.splitext(self.input_file)
        if self.file_extension not in ('.html', '.czm'): # Comprueba si el tipo de archivo suministrado es adecuado.
            raise IOError('Extensión no soportada. Por favor, proporcione un archivo czm o html.')

    def parse_html(self):
        """
        Obtiene los datos almacenados en el fichero html. En caso de proporcionar un fichero czm, lo descomprime
        y localiza el correspondiente html.

        """
        if self.file_extension == '.czm': # Caso de fichero comprimido czm.
            folder_path = extract_file(self.filepath, self.filename) # Descomprime el archivo de entrada.
            html_path = find_extension(folder_path, '.html') # Busca el html en el directorio de extracción.
            if html_path:
                self.html_path = html_path[0]
        else: # Caso de html proporcionado directamente.
            self.html_path = self.filepath + "/" + self.filename
        if not self.html_path:
            raise IOError('Archivo html no encontrado.')
        html_file = open(self.html_path, encoding="utf8") # Almacena los datos del html.
        # self.parsed_html = BeautifulSoup(html_file, "html.parser")
        self.parsed_html = BeautifulSoup(html_file, "lxml") # HAY QUE INSTALAR LXML

    def find_kt(self):
        """
        Busca dentro del fichero html la información correspondiente a los factores de intensidad de esfuerzos.

        """
        if not self.parsed_html: # Obtiene la información del archivo html en caso de no haberla obtenido previamente.
            self.parse_html()
        tag = self.parsed_html.findAll('th') # Recupera las etiquetas tipo th del archivo html.
        kt_value = None
        for i in range(0, len(tag)): # Itera a lo largo de las etiquetas th.
            if tag[i].string[0:2] == 'Kt': # Busca la etiqueta th correspondiente al kt.
                kt_value = float(tag[i].next_sibling.contents[0])
        if kt_value is None: # Informa en caso de que no haya almacenado ningún valor de kt.
            print("Valor de Kt no encontrado.")
        return kt_value

    def read_tables(self):
        # De momento únicamente lee tabla donde las etiquetas están a la izquierda y el valor a la derecha. Tablas n x 2.
        d, table_count = {}, 0
        tables = self.parsed_html.findAll('table')
        for table in tables:
            lines = table.findAll('tr')
            d_aux = {}
            for line in lines:
                if len(line.findAll()) > 2:
                    continue
                header, result = line.findAll()[0].string, line.findAll()[1].string
                d_aux.update({header:result})
            if d_aux:
                d.update({table_count:d_aux})
                table_count = table_count + 1
        return d

