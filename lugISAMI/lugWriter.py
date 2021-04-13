#
# Authors:
# Pablo Arcediano,
# Lucas Bernacer Soriano,
# Ángela Blazquez,
# Héctor Dionisio,
# Javier Vela
#
# Copyright (c) 2021, Capgemini Engineering
#

from openpyxl import load_workbook
import os.path
from datetime import date
from wrappers import read_sheet

class lugInput():
    """
    Clase desarrolada para trabajar con orejetas en ISAMI.

    """
    def __init__(self, input_file):
        """
        Inicializa la ruta, el nombre del fichero y lee el archivo Excel proporcionado.

        input_file: Ruta de entrada del archivo.

        """
        self.input_file = input_file
        self.book = load_workbook(self.input_file, data_only=True)
        self.analysis_data, self.material_data = {}, {}
        self.output_file = None

    def read_template(self):
        """
        Obtiene del archivo de entrada los datos procedentes de las pestañas análisis y materiales.

        """
        self.analysis_data =read_sheet(initial_row=4, initial_column=1, header_row=3, name_sheet='Analysis', book=self.book)
        material_data = read_sheet(initial_row=4, initial_column=1, header_row=3, name_sheet='Materials', book=self.book)
        self.material_data = dict(sorted(material_data.items())) # Ordena el diccionario de materiales.

    def write_output(self, output_path, output_filename):
        """
        Escribe el archivo de entrada a ISAMI una vez obtenida la información de entrada.

        output_path: Ruta del archivo de salida.
        output_filename: Nombre del archivo de salida.

        """
        self.read_template() # Recupera la información de las pestañas de análisis y materiales del Excel de entrada.
        self.output_file = output_path + '/' + output_filename
        if os.path.isfile(self.output_file + '.py'): # Creación del archivo de salida.
            os.remove(self.output_file + '.py')
        file = open(self.output_file + '.py', "x")
        today_date = date.today() # Fecha de creación del archivo de entrada a ISAMI.

        # Encabezado del archivo de entrada a ISAMI.
        file.writelines("########################\n")
        file.writelines("# ISAMI VERSION: 8.0.0 #\n")
        file.writelines("# ANALYSIS: LUG        #\n")
        file.writelines("# Mode: SAA            #\n")
        file.writelines("# Written by: ALTRAN   #\n")
        file.writelines("# Date: " + today_date.strftime("%d/%m/%Y") + "     #\n")
        file.writelines("######################\n")

        # Incluye las primeras líneas de materiales en el archivo.
        for keys in self.material_data.keys():
            file.writelines("MS.LoadMaterial("+ "'" + keys + "'" + "," + self.material_data[keys]["ISAMI Name"] + ","
                            + self.material_data[keys]["CODE"] + "," + self.material_data[keys]["User/Referenced"]
                            +")\n")
        file.writelines(" \n")

        cont = 1 # Contador en caso de múltiples casos de estudio.
        for keys in self.analysis_data.keys(): #Incluye la infromación de la pestaña análisis.
            # Define las etiquetas de las entradas a escribir en el archivo de salido.
            folder = ["Standar Pin","/Diameter","/Material","Standar Bush","Standar Bush","/BushExternalDiameter",
                      "/BushMaterial","/LugResultantForce","/LugResultantAngle","/LoadingRatio","/Width","/Length",
                      "/Thick","/ThickUnstudied","/PinOffsetX","/PinOffsetY","/SuperiorAngle",
                      "/InferiorAngle","/ShearType","/StructureMaterial","/Orientation_init"]
            dic_folder = {}
            for i in folder: # Comprueba si el valor es del tipo str y reemplaza el operador decimal.
                value = self.analysis_data[keys][i]
                if not isinstance(value,str):
                    value = str(self.analysis_data[keys][i]) #.replace('.', ',')
                else:
                    pass
                dic_folder.update({i:value})

            # Creación de líneas correspondientes a DPines.
            file.writelines("MS.CreateObject('DPines" + str(cont) + "','AirbusEO_DPin',[\n"
            "['/CsmMbr_Name','S:DPin" + str(cont) + "'],\n"
            "['/CsmMbr_Uptodate','B:TRUE'],\n"
            "['/Diameter','CaesamQty_LENGTH:" + dic_folder["/Diameter"] + ";mm'],\n"
            "['/Material','AirbusEO_TMaterial:" + dic_folder["/Material"] + "'],\n"
            "])\n \n\n")

            # Creación de líneas correspondientes a DBushes.
            file.writelines("MS.CreateObject('DBushes" + str(cont) + "','AirbusEO_DBush',[\n"
            "['/CsmMbr_Name','S:D_Bush" + str(cont) + "'],\n"
            "['/BushInternalDiameter','CaesamQty_LENGTH:" + dic_folder["/Diameter"] + ";mm'],\n"
            "['/BushExternalDiameter','CaesamQty_LENGTH:" + dic_folder["/BushExternalDiameter"] + ";mm'],\n"
            "['/BushMaterial','AirbusEO_TMaterial:" + dic_folder["/BushMaterial"] + "'],\n"
            "])\n \n")

            # Creación de líneas correspondientes a Geom.
            file.writelines("MS.CreateObject('Geom" + str(cont) + "','AirbusEO_DLugGeometry',[\n"
            "['/CsmMbr_Name','S:Geom'],\n"
            "['/LugType','Enum_LugType:SIMPLE'],\n"
            "['/Width','CaesamQty_LENGTH:" + dic_folder["/Width"] + ";mm'],\n"
            "['/Length','CaesamQty_LENGTH:" + dic_folder["/Length"] + ";mm'],\n"
            "['/Thick','CaesamQty_LENGTH:" + dic_folder["/Thick"] + ";mm'],\n"
            "['/ThickUnstudied','CaesamQty_LENGTH:" + dic_folder["/ThickUnstudied"] + ";mm'],\n"
            "['/LugPin','AirbusEO_DPin:DPines" + str(cont) + "'],\n"
            "['/LugBush','AirbusEO_DBush:DBushes" + str(cont) + "'],\n"
            "['/PinOffsetX','CaesamQty_LENGTH:" + dic_folder["/PinOffsetX"] + ";mm'],\n"
            "['/PinOffsetY','CaesamQty_LENGTH:" + dic_folder["/PinOffsetY"] + ";mm'],\n"
            "['/SuperiorAngle','CaesamQty_PLANE_ANGLE:" + dic_folder["/SuperiorAngle"] + ";deg'],\n"
            "['/InferiorAngle','CaesamQty_PLANE_ANGLE:" + dic_folder["/InferiorAngle"] + ";deg'],\n"
            "['/NotchedLength','CaesamQty_LENGTH:20;mm'],\n"
            "['/ShearType','Enum_ToggleShearType:" + dic_folder["/ShearType"] + "'],\n"
            "['/StructureMaterial','AirbusEO_TMaterial:" + dic_folder["/StructureMaterial"] + "'],\n"
            "])\n \n")

            # Creación de líneas correspondientes a Loading.
            file.writelines("MS.CreateObject('Loading" + str(cont) + "','AirbusEO_DLugLoading',[\n"
            "['/CsmMbr_Name','S:Loading'],\n"
            "['/LoadingType','Enum_LoadingType:NO_COEFFICIENT'],\n"
            "['/LugForceLoadingType','Enum_TogglePHForceLoadingType:RESULTANT AND ANGLE'],\n"
            "['/LugCoefficientForceX','D:20'],\n"
            "['/LugCoefficientForceY','D:30'],\n"
            "['/LugForceX','CaesamQty_FORCE:10000;N'],\n"
            "['/LugForceY','CaesamQty_FORCE:10000;N'],\n"
            "['/LugCoefficientResultantForce','D:100'],\n"
            "['/LugResultantForce','CaesamQty_FORCE:" + dic_folder["/LugResultantForce"] + ";N'],\n"
            "['/LugResultantAngle','CaesamQty_PLANE_ANGLE:" + dic_folder["/LugResultantAngle"] + ";deg'],\n"
            "['/NbParameters','I:32'],\n"
            "['/LoadingRatio','D:" + dic_folder["/LoadingRatio"] + "'],\n"
            "['/NbClasses','I:1'],\n"
            "['/Compression','Enum_ToggleCompression:Smin'],\n"
            "['/UserSmin','CaesamQty_PRESSURE:0;MPa'],\n"
            "['/PropagationComputation','CaesamEnum_YesNo:No'],\n"
            "['/MLPDesign','CaesamEnum_YesNo:No'],\n"
            "['/LoadRedistributionFactor','D:1']\n"
            "])\n \n")

            # Creación de líneas correspondientes a Law.
            file.writelines("MS.CreateObject('Law" + str(cont) + "','AirbusEO_DFatigueLawGeoDependent',[\n"
            "['/CsmMbr_Name','S:Law'],\n"
            "['/IsCracked','S:No'],\n"
            "['/LawType','Enum_ToggleLawTypeGeoDependent:Fatigue Law'],\n"
            "['/DamageCalculationMethod','Enum_ToggleDamageCalculationMethod:LOCAL STRESS ANALYSIS'],\n"
            "['/FatigueLaw','Enum_ToggleFatigueLaw:AFI LAW'],\n"
            "['/Orientation_init','Enum_Orientation:" + dic_folder["/Orientation_init"] + "'],\n"
            "['/Configuration_init','S:" +
                            self.material_data[dic_folder["/StructureMaterial"]]["Configuration"] + "'],\n"  
            "])\n \n")
            # Creación de líneas correspondientes a initiation_lug.
            file.writelines("MS.CreateStandaloneAnalysis('initiation_lug',None,[\n"
            "   '/CsmMbr_Name S:" + keys + "',\n"
            "   '/Geometry *AirbusEO_DLugGeometry:',\n"
            "   '/Geometry/ReferencedObject AirbusEO_DLugGeometry:Geom" + str(cont) + "',\n"
            "   '/Loading *AirbusEO_DLugLoading:',\n"
            "   '/Loading/ReferencedObject AirbusEO_DLugLoading:Loading" + str(cont) + "',\n"
            "   '/FatigueLaw *AirbusEO_DFatigueLawGeoDependent:',\n"
            "   '/FatigueLaw/ReferencedObject AirbusEO_DFatigueLawGeoDependent:Law" + str(cont) + "',\n"
            "],\n"
            "'" + keys + "')\n \n")
            cont = cont + 1 # Actualización del contador en caso de múltiples casos de estudio.

        file.writelines(" \n")
        file.writelines("MS.RunAllAnalysis()\n")
        file.writelines("MS.Save('" + output_filename +".czm')\n") # Asigna el nombre del archivo CZM de salida.
        file.close()

    def write_bach(self, output_path, output_filename):
        """
        Escribe el archivo para poder invocar ISAMI en modo batch.

        output_path: Ruta del archivo de salida.
        output_filename: Nombre del archivo de salida.

        """
        self.output_file = output_path + '/' + output_filename
        if os.path.isfile(self.output_file + '_bach.sh'):  # Creación del archivo de salida.
            os.remove(self.output_file + '_bach.sh')
        file = open(self.output_file + '_bach.sh', "x")
        file.writelines("#!/bin/bash\n")
        file.writelines("/CAE/ISAMI/v11.1.0/bin/launchIA.ksh ksh -application isami_derivatives -python " + output_filename + ".py")
        file.close()