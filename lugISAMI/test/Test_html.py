
from path import Path
from lugReader import lugHTML
from wrappers import find_extension

testcases_dir = Path(__file__).dirname()+"/testcases"

def extract_kt():
    """
    Comprueba el valor obtenido de kt.
    """

    html = lugHTML(filepath=testcases_dir, filename='LUG.czm')
    kt = html.find_kt()
    tablas = html.read_tables()
    print(kt)
    files = find_extension(testcases_dir,'.czm')
    # print('Hola')

if __name__ == '__main__':

    extract_kt()