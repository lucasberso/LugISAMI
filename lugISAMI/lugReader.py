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

import os
from bs4 import BeautifulSoup
from wrappers import extract_file
from wrappers import find_extension

class lugHTML():
    """
    Clase desarrollada para trabajar con el html o czm proporcionado por ISAMI.

    """
    def __init__(self, input_file):
        """
        Inicializa el archivo de entrada con nombre y ruta. Comprobación del tipo de fichero, debe ser czm o html.

        input_file: Ruta de entrada del archivo.

        """
        self.input_file = input_file
        self.parsed_html, self.html_path, self.parsed_html_dic = None, [], {} # Información almacenada.
        self.file_extension = os.path.splitext(self.input_file)[1]
        self.filepath = os.path.dirname(self.input_file)
        if self.file_extension not in ('.html', '.czm'): # Comprueba si el tipo de archivo suministrado es adecuado.
            raise IOError('File not supported. Please, provide a czm or html file.')

    def parse_html(self):
        """
        Obtiene los datos almacenados en el fichero html o czm. En caso de proporcionar un fichero czm, lo descomprime
        y localiza los correspondientes html.

        """
        if self.file_extension == '.czm': # Caso de fichero comprimido czm.
            folder_path = extract_file(self.input_file) # Descomprime el archivo de entrada.
            self.html_path = find_extension(folder_path, '.html') # Busca el html en el directorio de extracción.
        else: # Caso de html proporcionado directamente.
            self.html_path.append(self.input_file)
        if not self.html_path: # En caso de que no exista ningún html.
            raise IOError('html file not found.')
        for path in self.html_path: # Almacena cada uno de los html parseados en un diccionario.
            html_file = open(path, encoding="utf8") # Almacena los datos del html.
            parsed_html = BeautifulSoup(html_file, "lxml")  # Hay que instalar lxml.
            self.parsed_html_dic.update({os.path.splitext(os.path.basename(path))[0]:parsed_html})

    def find_kt(self, html):
        """
        Busca dentro del fichero html la información correspondiente al factor de intensidad de esfuerzos (SIF).

        html: Debe proporcionarse el html previamente parseado.

        """
        tag, kt_value = html.findAll('th'), None # Recupera las etiquetas tipo th del archivo html.
        for i in range(0, len(tag)): # Itera a lo largo de las etiquetas th.
            if tag[i].string[0:2] == 'Kt': # Busca la etiqueta th correspondiente al kt.
                kt_value = float(tag[i].next_sibling.contents[0])
        if kt_value is None: # Informa en caso de que no se haya almacenado ningún valor de kt.
            print("Not found Kt value.")
        return kt_value

    def read_tables(self, html):
        # De momento únicamente lee tabla donde las etiquetas están a la izquierda y el valor a la derecha. Tablas n x 2.
        d, table_count = {}, 0
        tables = html.findAll('table')
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

    def write_output(self, output_path, output_filename):
        """
        Escribe un fichero tipo txt con el nombre del caso de estudio y su correspondiente kt.

        output_filename: Nombre del fichero de salida.

        """
        self.output_file = output_path + '/' + output_filename
        if os.path.isfile(self.output_file + '.txt'):  # Creación del archivo txt de salida.
            os.remove(self.output_file + '.txt')
        file = open(self.output_file + '.txt', "x")

        self.parse_html() # Obtiene los html de entrada.
        file.writelines('# TOOL VERSION: 1.0 #')
        for id in self.parsed_html_dic: # Escribe la salida en el txt con el nombre del caso y kt correspondiente.
            file.writelines('-----------------------------------\n')
            header = id + "\n"
            file.writelines(header)
            file.writelines('-----------------------------------\n')
            tables = self.read_tables(self.parsed_html_dic[id])
            info = tables[0]
            for i in info:
                file.writelines(i + " = " + str(info[i]) + "\n")
            kt = self.find_kt(self.parsed_html_dic[id])
            file.writelines(" Kt = " + str(kt) + "\n")
        file.close()