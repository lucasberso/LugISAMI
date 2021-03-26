
# Definir librerias necesarias
# from ... import ...

# Trabajar con orejetas
class Lug_generator(excel_filename, excel_path):
    #
    def __init__(self):
        """
        Inicialización de la clase
        """
        self.excel_filename=excel_filename
        self.excel_path=excel_path

    def crear_input(self):
        """
        Crea archivo input de ISAMI a partir de un Excel
        """
    def llamar_isami(self):
        """
        Llama a ISAMI para correr el archivo generado
        """
    def obtener_KT(self):
        """
        Post-procesa los KT almacenados en el HTML
        """
    def correr_todo(self):
        """
        Realiza el análisis completo
        """
        self.crear_input()
        self.llamar_isami()
        self.obtener_KT()