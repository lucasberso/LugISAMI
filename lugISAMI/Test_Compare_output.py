
from Lug import Lug_generator
from path import Path

testcases_dir = Path(__file__).dirname()/"testcases/comparison"

if __name__ == '__main__':

    filename = 'Lug_comparison_1.xlsm'
    Lug = Lug_generator(filename, testcases_dir)
    Lug.write_output(output_filename='Lug_comparison_python_1')

    f1=open(testcases_dir + "/"+ "Lug_comparison_1.py", "r")
    f2=open(testcases_dir + "/"+ "Lug_comparison_python_1.txt", "r")

    i = 0

    for line1 in f1:
        i += 1
        for line2 in f2:
            # matching line1 from both files
            if line1 == line2:
                # print IDENTICAL if similar
                print("Line ", i, ": IDENTICAL")
            else:
                print("Line ", i, ":")
                # else print that line from both files
                print("\tFile 1:", line1, end='')
                print("\tFile 2:", line2, end='')
            break
    # closing files
    f1.close()
    f2.close()