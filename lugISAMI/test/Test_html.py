
from path import Path
from lugReader import lugHTML

testcases_dir = Path(__file__).dirname()/"testcases"

def extract_kt():
    """
    Comprueba el valor obtenido de kt.
    """

    html = lugHTML(filepath=testcases_dir, filename='LUG.czm')
    kt = html.find_kt()
    print(kt)

if __name__ == '__main__':

    extract_kt()