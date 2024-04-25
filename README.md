# Instalación de CLIPS en Windows y prueba de código

CLIPS es un entorno de desarrollo para la construcción de sistemas expertos. 

## Requisitos

- Sistema operativo Windows 7, 8, o 10.
- Privilegios de administrador para la instalación.

## Paso 1: Descargar CLIPS

1. Visita la página oficial de CLIPS en SourceForge: [CLIPS en SourceForge](https://sourceforge.net/projects/clipsrules/files/CLIPS/6.4.1/).
2. Descarga el archivo ejecutable (.msi) apropiado para tu versión de Windows.

## Paso 2: Instalar CLIPS

1. Ubica el archivo `.msi` descargado y haz doble clic para iniciar la instalación.
2. Sigue las instrucciones del asistente de instalación:
   - Acepta el acuerdo de licencia.
   - Elige la carpeta de destino para la instalación.
   - Confirma la instalación y espera a que finalice el proceso.

## Paso 3: Verificar la Instalación

1. Abre la línea de comandos (cmd) en tu sistema.
2. Navega al directorio donde instalaste CLIPS.
3. Puedes hacerlo utilizando el comando cd, por ejemplo: ```cd C:\Program Files\SSS\CLIPS 6.4.1\```.
4. Ejecuta CLIPS escribiendo ```CLIPSDOS.exe``` en la línea de comandos.
5. Si todo está correcto, deberías ver el entorno de CLIPS iniciando en la línea de comandos.

## Paso 4: Probar código

1. En el repositorio de este README, descarga el archivo llamado ```cholesterol_clips_code.clp``` en el directorio de preferencia.
2. En la linea de comando de CLIPS, navega al directorio donde se descargó el archivo. Deberías ver la siguiente salida:
```
CLIPS> (load C:\Users\Duncan ZM\Downloads\cholesterol_clips_code.clp)
%*********
TRUE
```
3. Corre los siguientes comando para empezar el programa:
```
CLIPS> (reset)
CLIPS> (run)
```
4. Te saldrán 4 prompts y los irás llenando. Al final debería mostrar el riesgo de enfermedad de corazón. Aquí un ejemplo:
```
What is your name? Fred
Fred, what is your gender? male
Fred, what is your total cholesterol? 180
Fred, what is your HDL? 50
Fred, you have a moderate risk of heart disease.
```

# Instalación de Python en Windows y prueba de código

Python es un lenguaje de programación de alto nivel, interpretado y de propósito general.

## Requisitos

- Sistema operativo Windows 7, 8, 10.
- Privilegios de administrador para la instalación.

## Paso 1: Descargar Python

1. Visita la página oficial de Python: [Python.org](https://www.python.org/downloads/windows/).
2. En la sección de descargas, selecciona la versión de Python que deseas instalar. Se recomienda descargar la versión más reciente.
3. Haz clic en el enlace "Download" para la versión de Windows que corresponda a tu sistema.

## Paso 2: Instalar Python

1. Ubica el archivo descargado y haz doble clic para iniciar la instalación.
2. En la primera pantalla del instalador, asegúrate de marcar la opción "Add Python X.X to PATH" antes de hacer clic en "Install Now". Esto agregará Python al PATH de tu sistema, facilitando su ejecución desde la línea de comandos.
3. Sigue las instrucciones en pantalla para completar la instalación.

## Paso 3: Verificar la Instalación

1. Una vez finalizada la instalación, abre la línea de comandos (cmd).
2. Ejecuta el siguiente comando para verificar que Python se ha instalado correctamente y está correctamente añadido al PATH:
```
python --version
```

## Paso 4: Probar código

1. En el repositorio de este README, descarga el archivo llamado ```cholesterol_python_code.py`` en el directorio de preferencia.
2. Abre la linea de comando de Windows (cmd), navega al directorio donde se descargó el archivo.
```
cd C:\Downloads\
```
3. Corre el siguiente comando para empezar el programa:
```
python3 cholesterol_python_code.py
```
4. Te saldrán 4 prompts y los irás llenando. Al final debería mostrar el riesgo de enfermedad de corazón. Aquí un ejemplo:
```
What is your name? Fred
Fred, what is your gender? male
Fred, what is your total cholesterol? 180
Fred, what is your HDL? 50
Fred, you have a moderate risk of heart disease.
```
