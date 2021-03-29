import openpyxl
from path import Path
testcases_dir = Path(__file__).dirname()/"testcases"
if __name__ == '__main__':

    filename = 'Lug_manual.xlsm'
    book= openpyxl.load_workbook(testcases_dir+ '/'+ filename)
    sheet = book["Materials"]
    print(book.sheetnames)
