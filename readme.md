# Lug ISAMI

Librería que asiste en la escritura de archivos de entrada ISAMI para el análisis de orejetas. 

## Instalación


```bash
pip install ...
```

## Uso

#### Creación de un archivo input para ISAMI:

```python
from lugWriter import lugInput
from path import Path

testcases_dir = Path(__file__).dirname()
filename = 'Lug_template.xlsm'  # Nombre del archivo Excel con los datos de entrada.
Lug = Lug_generator(filename, testcases_dir)  # Inicializa la librería con el archivo input y la ruta.
# Escribe y almacena el archivo input de ISAMI.
Lug.write_output(output_filename='ISAMI_input_file')
```

