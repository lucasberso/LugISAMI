
from Lug import Lug_generator

if __name__ == '__main__':

# filename = excel1.xls

Lug = Lug_generator(filename)
Lug.crear_input()
Lug.correr_todo()
Lug.obtenerKT_html()
