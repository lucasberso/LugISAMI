
# ----------------------- Librerias importadas

#import numpy as np
#import xlsxwriter
#import xlrd
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
        initial_row = 3
        final_row = ws.max_row
        initial_column = 2
        final_column = ws.max_column - 1
        dictio ={}
        headers = ['Load','Angle']
        if initial_row == final_row:
            vector = [initial_row]
        else:
            vector = list(range(initial_row,final_row))
        for i in vector:
            print(i)
            for j in range(initial_column, final_column):
                pass
        print('Hola')

    def write_output(self):

        # f = open("myfile.txt", "x")
        # f.writelines("########################\n")
        # f.writelines("# ISAMI VERSION: 8.0.0 #\n")
        # f.writelines("# ANALYSIS: LUG        #\n")
        # f.writelines("# Mode: SAA            #\n")
        # f.writelines("# Written by: ALTRAN   #\n")
        # f.writelines("# Date: 25/01/14       #\n")
        # f.writelines("########################\n")
