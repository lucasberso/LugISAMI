
from path import Path
from bs4 import BeautifulSoup

testcases_dir = Path(__file__).dirname()/ "testcases"

if __name__ == '__main__':

    # with zipfile.ZipFile(testcases_dir/'LUG.czm', 'r') as z:
    #     z.extractall(testcases_dir/"extract")

    html_path = testcases_dir / "extract\documentczm\initiation_lug\Fatigue-DFEM-Initiation-Lug\Fatigue-DFEM-Initiation-Lug.html"

    f = open(html_path, encoding="utf8")
    soup = BeautifulSoup(f, "html.parser")
    tag = soup.findAll('th')
    Kt = None
    for i in range(0,len(tag)):
        if tag[i].string == 'Kt FACTOR (1)  ':
            Kt = tag[i].next_sibling.contents[0]
            print(Kt)
    if Kt is None:
        print("Valor de Kt no encontrado.")

