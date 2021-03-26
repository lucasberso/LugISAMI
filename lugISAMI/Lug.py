
# ----------------------- Librerias importadas

import numpy as np
import xlsxwriter
import xlrd
import openpyxl

class Lug_generator():
    """
    Clase desarrolada para trabajar con orejectas en ISAMI.
    """

    # ----------------------- Inicialización
    def __init__(self, excel_filename, excel_path):
        """
        Almacena la ruta y el nombre del fichero.
        """
        self.excel_filename = excel_filename
        self.excel_path = excel_path
        self.input_file = excel_path + '/' + excel_filename

    def read_input(self):

        input = openpyxl.load_workbook(self.input_file)
        ws = input.active

    #     """
    #     Crea archivo input de ISAMI a partir de un Excel
    #     """
    # def llamar_isami(self):
    #     """
    #     Llama a ISAMI para correr el archivo generado
    #     """
    # def obtener_KT(self):
    #     """
    #     Post-procesa los KT almacenados en el HTML
    #     """
    # def correr_todo(self):
    #     """
    #     Realiza el análisis completo
    #     """
    #     self.crear_input()
    #     self.llamar_isami()
    #     self.obtener_KT()