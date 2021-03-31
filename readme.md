# Lug ISAMI

Librería que asiste en la escritura/lectura de archivos en ISAMI para el análisis de orejetas. 

## Instalación


```bash
pip install ...
```

## Uso

#### Creación de un archivo input de ISAMI:

```python
from lugWriter import lugInput

filepath = 'filepath' # Ruta del archivo de entrada. 
filename = 'filename.xlsm'  # Nombre del archivo Excel con los datos de entrada.
Lug = lugInput(filepath, filename)  # Inicializa la librería con el archivo input y la ruta.
Lug.write_output('ISAMI_input_file') # Escribe y almacena el archivo input de ISAMI.
```

#### Lectura de un archivo html output de ISAMI:

```python
from lugReader import lugHTML

filepath = 'filepath' # Ruta del archivo de entrada. 
filename = 'filename.html' # o 'filename.czm' 
html_data = lugHTML(filepath, filename) # Almacena los datos del html de lectura.
```