
from path import Path
from lugReader import lugHTML


testcases_dir = Path(__file__).dirname()+"/testcases"

def write_txt():

    filename = 'LUG_3.czm'
    input_file = testcases_dir + "/" + filename
    html = lugHTML(input_file=input_file)
    html.write_output(output_path=testcases_dir, output_filename='prueba')

if __name__ == '__main__':

    write_txt()