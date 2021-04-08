
from path import Path
from lugReader import lugHTML
import tkinter as tk
import time
import sys
import subprocess
import sys


if __name__ == '__main__':

    testcases_dir = Path(__file__).dirname()+"/test/testcases"

    filename = 'LUG_3.czm'
    input_file = testcases_dir + "/" + filename
    html = lugHTML(input_file=input_file)
    html.write_output(output_path=testcases_dir, output_filename='prueba')
