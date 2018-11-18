# Reconocimiento-Facial
Detección de rostro y reconocimiento facial frontal (Entorno Controlado, local).

El principal objetivo de este Proyecto es el diseño de un sistema para identificar
personas (mediante el reconocimiento de caras frontales) y su aplicación a un
sistema de recoleccion de datos de un individuo tales como RENAP, SAT, MAICON. 

___
# Documentación 
¿cómo funciona la tecnología de reconocimiento de rostros y cuáles son los problemas que hay que tener en cuenta?
Este tipo de tecnologías no es precisamente un fenómeno reciente. Los primeros experimentos con esta tecnología se remontan a la década de 1960.
El proceso de detección y reconocimiento consta de cuatro módulos principales y varios pasos intermedios:

- Detección del rostro: detecta que hay una cara en la imagen, sin identificarla. Si se trata de un vídeo, también es posible hacer un seguimiento del rostro. Proporciona la localización y la escala a la que encontramos la cara.

- Acondicionamiento y normalización: localiza las componentes del rostro y, mediante transformaciones geométricas, lo normaliza respecto propiedades geométricas, como el tamaño y la pose, y fotométricas, como la iluminación. Para normalizar las imágenes de rostros, se pueden seguir diferentes reglas, como la distancia entre las pupilas, la posición de la nariz, o la distancia entre las comisuras de los labios.

- Extracción de características: proporciona información para distinguir entre los rostros de diferentes personas según variaciones geométricas o fotométricas.

- Reconocimiento: el patrón facial de características extraído se compara con los vectores de características extraídos de las caras de la base de datos. Si encuentra con un porcentaje elevado de similitud, devuelve la identidad del rostro; si no, indica que es una cara desconocida.

El siguiente esquema resume el proceso  que se utiliza para detectar y reconocer un rostro.

<p align="center">
	<img src="http://drive.google.com/uc?export=view&id=1PlziuDb9X1hQrhdl0m7mZ6_lFJ9jDx0o">
</p>

El software de detección y reconocimiento de rostros tiene mucho camino por recorrer.
___

# Un poco de funcionamiento interno:
El proyecto cuenta con 4 (faceRecog, ml, records, static y templates) carpetas principales un favicon, el archivo manage.py para iniciar el servidor y el archivo readme.
En la carpeta templates se encuentral los archivos html que basicamente son archivo estaticos que tienen los elementos (div, etiquetas, botnoes, modales entre otros) que se van a desplegar en la pagina web. Cuenta con 5 paginas details, error. Index. Layout y records. 

Para mejorar la presentación de las paginas se utiliza bootstrap, las cuales tienen sus css, fuentes y jquerys para las animaciones esto se encuentra el carpeta static la cual también tiene una carpeta llamada img donde están almacenadas las imágenes que se usan para la pagina web y en esta carpeta también se guardan las imágenes de cada persona que se agrega esta imagen se muestra en la pagina de details
para iniciar el servidor web se necesita de migraciones las cuales realiza django esto se refiere a imporat los models, las urls  y las vistas esto se encuentra en la carpeta records. 

Dentro de la carpeta ml se encuentra se encuentran 2 carpetas importantes una se llama dataset es donde se almacenan las imágenes de todos los rostos de las personas que se agregan estas imágenes son las que utilizan el entrenamiento. También se encuentra la carpeta regnizer que es donde se crea el archivo resultante del entrenamiento (trainingData.yml) en este archivo se encuentra los datos de los rostos de la careta dataset.

Dentro del la carpeta faceRecog se encuentra los archivos de python encargados de realizar la conexión con mysql y crear las tablas (settings). También el archivo de views.py que son las vistas es donde se realiza los import y las llamadas a opencv para agregar, entrenar y identificar el modelo.

___

# ********************* Requerimientos *************************
Instalar :
- Python version: 2.7.15
- Django version: 1.11.9
- OpenCV version: 3.2
- Sklearn version: 0.19.1
- Mysql Database

# Configuración de mysql
	- Crear un usuario con contraseña (superusuario).
	- crear una base de datos (cualquier nombre).
	- Modificar el archivo settings.py en la carpeta faceRecog.
	- Modificar la configuración del objeto BATABASES con los de su maquina.
	- modificar las lineas:
		'NAME': 'nombre de tu base de datos ',
		'USER': 'su_usuario',
		'PASSWORD': 'clave_de_tu_usuario',
		'HOST': '127.0.0.1',
		'PORT': '8889'(verificar el puerto de mysql por defaul es 3306)

# Ejecutar el entorno Django (en el directorio del proyecto)
	- Crear las migraciones con el comando:
		python manage.py migrate
	- Crear un usuario en django:
		python manage.py createsuperuser
	- Ejecutar el servidor:
		python manage.py runserver --nothreading --noreload
	

# Iniciar el servidor de desarrollo en tu navegador.
   http://127.0.0.1:8000/


___

# Guía de Uso

<p align="center">
	<img src="http://drive.google.com/uc?export=view&id=1Zg_VZLEf5PRFL3aHRE90uGY_83yTNaKB">
</p>

Al iniciar se vera una pantalla con tres botones los cuales se identifican con :
Agregar persona: se utiliza para agregar a una persona al modelo, el cual despliega un modal el el cual
se debe ingresar un id único para cada persona luego dar clic en el botón iniciar y seguir las
indicaciones dadas en el modal.


<p align="center">
	<img src="http://drive.google.com/uc?export=view&id=1zcTSiRKQ-ivfvrsI__-gc6_YR7tFbxOF">
</p>


Al iniciar la captura de rostros se vera un recuadro de color verde el el cual se mostrara el numero de
fotografiá tomada espera hasta que el contador llene a 36 capturas.

<p align="center">
	<img src="http://drive.google.com/uc?export=view&id=18IHw66zIvZ3hC_gzXYX3kQndvf9u81-m">
</p>


Luego de realizar las capturas se debe llenar un formulario utilizando el id asignado a las fotografiás.


<p align="center">
	<img src="http://drive.google.com/uc?export=view&id=1YT1-nX4SZ8DrJauBIDVR_KV0AAwBFJlE">
</p>

Entrenamiento: El cual crea el modelo utilizando las fotografiás capturadas en el inciso Agregar
personas basta con dar un clic sobre el botón.

<p align="center">
	<img src="http://drive.google.com/uc?export=view&id=1JgjxXG6IoByzTeDE3Ab1dtPVMCcXhIQy">
</p>

Camara: Es inciso abre la cámara y enviá los frame capturados a comparar con el modelo para realizar
la identificación.

<p align="center">
	<img src="http://drive.google.com/uc?export=view&id=1oIfyeL3V4d5gHNG6EDieYuHnInGH1xks">
</p>

Cuando el rostro no tienen coincidencia con uno de los capturados se muestra el texto “Desconocido”
de color rojo.

<p align="center">
	<img src="http://drive.google.com/uc?export=view&id=1Ob_FG5eQkSLpsLqWuD0mG2K20hZgu6N7">
</p>

Cuando el rostro tienen coincidencia con uno de los capturados se muestra el texto “Detectado” de
color Verde. Y se muestra un pagina con los detalles de la persona ingresados en el formulario del
inciso agregar persona.

<p align="center">
	<img src="http://drive.google.com/uc?export=view&id=1uroNNAEERMq_qEsID4fvus6BMNvPUXfT">
</p>
___


# Otros Archivos

	# DATASET
  http://drive.google.com/uc?export=view&id=1b30BoA82X7JFV_xzQDW6fuRa8lbOCXPK	

	# Modelo:
  http://drive.google.com/uc?export=view&id=1U9DUsElwBME-PfPFvojZNZ-1azE8TmlV

___





