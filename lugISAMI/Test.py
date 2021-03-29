
from Lug import Lug_generator
from path import Path
import os.path

testcases_dir = Path(__file__).dirname()/"testcases"

if __name__ == '__main__':

    # filename = testcases_dir / 'excel_template.xlsx'
    filename = 'excel_template.xlsx'
    filename = 'Lug_manual.xlsm'

    Lug = Lug_generator(filename, testcases_dir)
    Lug.read_input()

    if os.path.isfile('myfile.txt'):
        os.remove('myfile.txt')
    else:
        f = open("myfile.txt", "x")

# Lug.crear_input()
# Lug.correr_todo()
# Lug.obtenerKT_html()
