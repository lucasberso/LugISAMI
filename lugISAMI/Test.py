
from Lug import Lug_generator
from path import Path

testcases_dir = Path(__file__).dirname()/"testcases"

if __name__ == '__main__':

    # filename = testcases_dir / 'excel_template.xlsx'
    filename = 'excel_template.xlsx'

    Lug = Lug_generator(filename, testcases_dir)
    Lug.read_input()

# Lug.crear_input()
# Lug.correr_todo()
# Lug.obtenerKT_html()
