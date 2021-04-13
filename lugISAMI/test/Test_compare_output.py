
from lugWriter import lugInput
from path import Path

def compare_txt(f1,f2):
    """
    Función que compara el contenido línea por línea de dos archivos de texto.
    f1: Primer archivo de texto.
    f2: Segundo archivo de texto.

    """
    i = 0
    for line1 in f1:
        i += 1
        for line2 in f2:
            if line1 == line2:
                print("Line ", i, ": IDENTICAL")
            else:
                print("Line ", i, ":")
                print("\tFile 1:", line1, end='')
                print("\tFile 2:", line2, end='')
            break
    f1.close()
    f2.close()

def compare_1():
    """
    Primer caso de estudio para comparar el archivo de entrada a ISAMI generado por la macro de Excel y la
    librería LugISAMI. Incluye únicamente un escenario a resolver por ISAMI.

    """
    testcases_dir = Path(__file__).dirname() / "testcases/comparison/1"
    # filename = 'Lug_comparison_1_template.xlsm'

    # Lug = lugInput(testcases_dir + "/" + filename)
    # Lug.write_output(testcases_dir, 'Lug_comparison_1_python')

    f1 = open(testcases_dir + "/" + "Test_1.py", "r")
    f2 = open(testcases_dir + "/" + "Test_2.py", "r")

    compare_txt(f1, f2)

def compare_2():
    """
    Segundo caso de estudio para comparar el archivo de entrada a ISAMI generado por la macro de Excel y la
    librería LugISAMI. Incluye dos escenarios a resolver por ISAMI.

    """
    testcases_dir = Path(__file__).dirname() / "testcases/comparison/2"
    filename = 'Lug_comparison_2_template.xlsm'

    Lug = lugInput(testcases_dir, filename)
    Lug.write_output(output_filename='Lug_comparison_2_python')

    f1 = open(testcases_dir + "/" + "Lug_comparison_2_macro.py", "r")
    f2 = open(testcases_dir + "/" + "Lug_comparison_2_python.py", "r")

    compare_txt(f1, f2)

def compare_3():
    """
    Tercer caso de estudio para comparar el archivo de entrada a ISAMI generado por la macro de Excel y la
    librería LugISAMI. Incluye tres escenarios a resolver por ISAMI.

    """
    testcases_dir = Path(__file__).dirname() / "testcases/comparison/3"
    filename = 'Lug_comparison_3_template.xlsm'

    Lug = lugInput(testcases_dir, filename)
    Lug.write_output(output_filename='Lug_comparison_3_python')

    f1 = open(testcases_dir + "/" + "Lug_comparison_3_macro.py", "r")
    f2 = open(testcases_dir + "/" + "Lug_comparison_3_python.py", "r")

    compare_txt(f1, f2)

if __name__ == '__main__':

    compare_1()
    # compare_2()
    # compare_3()
