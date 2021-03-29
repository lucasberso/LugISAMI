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

import openpyxl
import os.path
from datetime import date

class Lug_generator():
    """
    Clase desarrolada para trabajar con orejetas en ISAMI.
    """

    # ----------------------- Inicialización
    def __init__(self, excel_filename, excel_path):
        """
        Inicializa la ruta, el nombre del fichero y lee el archivo Excel proporcionado.

        :str excel_filename: Nombre del fichero Excel de entrada.
        :str excel_path: Ruta del fichero Excel de entrada.
        """
        self.excel_filename = excel_filename
        self.excel_path = excel_path
        self.input_file = excel_path + '/' + excel_filename
        self.book = openpyxl.load_workbook(self.input_file, data_only = True)

    def read_input(self, initial_row = 4, initial_column = 2, header_row = 3, name_sheet = 'Analysis'):
        """
        Obtiene de la hoja seleccionada por el usuario todos los datos encerrados por el rango suministrado.

        :int initial_row: Fila inicial de comienzo los datos.
        :int initial_column: Columna inicial de comienzo los datos.
        :int header_row: Fila con el nombre de los campos a almacenar.
        :int name_sheet: Nombre de la hoja de datos.
        :return: Diccionario de salida con los datos extraidos de la hoja Excel.
        """
        sheet = self.book[name_sheet]
        final_row = sheet.max_row
        final_column = sheet.max_column
        input_global = {}
        for i in range(initial_row, final_row + 1):
            name = sheet.cell(i, initial_column).value
            aux_dict = {}
            for j in range(initial_column, final_column + 1):
                key = sheet.cell(header_row, j).value
                value = sheet.cell(i, j).value
                aux_dict.update({key: value})
            input_global.update({name: aux_dict})
        return input_global

    def read_template(self):
        """
        Lee del archivo de entrada Excel los datos procedentes de las pestañas análisis y materiales.
        """
        self.analysis_data = self.read_input(initial_row = 4, initial_column = 1, header_row = 3, name_sheet='Analysis')
        self.material_data = self.read_input(initial_row = 5, initial_column = 2, header_row = 4, name_sheet='Materials')

    def write_output(self, output_filename):

        self.read_template()

        if os.path.isfile(output_filename + '.txt'):
            os.remove(output_filename + '.txt')
        file = open(output_filename + '.txt', "x")
        today_date = date.today()

        file.writelines("########################\n")
        file.writelines("# ISAMI VERSION: 8.0.0 #\n")
        file.writelines("# ANALYSIS: LUG        #\n")
        file.writelines("# Mode: SAA            #\n")
        file.writelines("# Written by: ALTRAN   #\n")
        file.writelines("# Date: " + today_date.strftime("%d/%m/%Y") + "     #\n")
        file.writelines("########################\n")

    # def read_materials(self):
    #     """
    #     Función encargada de leer la pestaña de materiales en el libro Excel de entrada. Suministra un diccionario
    #     de salida que contiene todos los materiales y sus características.
    #
    #     """
    #     mat_sheet = self.book["Materials"]
    #     initial_row, final_row = 5, mat_sheet.max_row
    #     initial_column, final_column = 2, mat_sheet.max_column
    #     self.mat_global = {}
    #     for i in range(initial_row, final_row + 1):
    #         mat_name = mat_sheet.cell(i, initial_column).value
    #         aux_dict = {}
    #         for j in range(initial_column, final_column + 1):
    #             key = mat_sheet.cell(4, j).value
    #             value = mat_sheet.cell(i, j).value
    #             aux_dict.update({key: value})
    #         self.mat_global.update({mat_name: aux_dict})
    #     return self.mat_global
    # # def write_output(self):
    #
    #     # f = open("myfile.txt", "x")
    #     # f.writelines("########################\n")
    #     # f.writelines("# ISAMI VERSION: 8.0.0 #\n")
    #     # f.writelines("# ANALYSIS: LUG        #\n")
    #     # f.writelines("# Mode: SAA            #\n")
    #     # f.writelines("# Written by: ALTRAN   #\n")
    #     # f.writelines("# Date: 25/01/14       #\n")
    #     # f.writelines("########################\n")