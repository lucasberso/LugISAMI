
from lugWriter import lugInput
from path import Path

testcases_dir = Path(__file__).dirname()

if __name__ == '__main__':
    # Script para comprobar los datos obetidos por la librería LugISAMI.
    filename = '../Lug_template.xlsm'  # Nombre del archivo Excel con los datos de entrada.
    input_file = testcases_dir + "/" + filename
    Lug = lugInput(input_file) # Inicializa la librería con el archivo input y la ruta.
    # Extrae los datos de la pestaña análisis.
    analysis = Lug.read_input(initial_row = 4, initial_column = 1, header_row=3, name_sheet = 'Analysis')
    # Extrae todos los datos del Excel de entrada.
    dicts = Lug.read_template()
    # Proporciona el archivo input de ISAMI.
    Lug.write_output(testcases_dir, 'Result_test_class_2')

