
from Lug import Lug_generator
from path import Path
import os.path

testcases_dir = Path(__file__).dirname()/"testcases"

if __name__ == '__main__':

    filename = 'Lug_manual.xlsm'
    Lug = Lug_generator(filename, testcases_dir)
    hola = Lug.read_input(initial_row = 4, initial_column = 1, header_row=3, name_sheet = 'Analysis')
    hola2 = Lug.read_template()
    hola3 = Lug.write_output(output_filename='tonto')
    print('hola')
    # if os.path.isfile('myfile.txt'):
    #     os.remove('myfile.txt')
    # else:
    #     f = open("myfile.txt", "x")

# Lug.crear_input()
# Lug.correr_todo()
# Lug.obtenerKT_html()
