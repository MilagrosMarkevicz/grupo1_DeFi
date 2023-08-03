# DeFi (Finanzas Descentralizadas)

_Blog desarrollado como parte del proyecto final de la Etapa 2 del INFORMATORIO, el cual es un programa del Gobierno del Chaco orientado al aprendizaje del sector de Software y Servicios Informáticos._

_El objetivo del sitio es informar las últimas noticias sobre el sector de Finanzas Descentralizadas._

## Comenzando 🚀

_Para obtener una copia del proyecto funcionando en tu PC de manera local para propósitos de desarrollo y pruebas, seguí las instrucciones_


### Pre-requisitos 📋

_Antes de iniciar, es recomendable generar un entorno virtual de trabajo donde instalaremos las dependencias necesarias para que el proyecto funcione. Para ello, abrimos el CMD y nos dirigimos a la carpeta donde queremos guardar el entorno virtual y ejecutamos el siguiente comando:_


```
virtualenv nombre-entorno

```
_Una vez creado es necesario activarlo para ello ejecutamos la siguiente linea (en Windows):_


```
nombre_del_entorno\Scripts\activate.bat

```

_Ya contamos con un entorno virtual activado en el cual podemos instalar todas las dependencias para correr nuestro proyecto._


_Luego, con el entorno activado, no dirigimos a la carpeta donde se encuentra el archivo requirements.txt y ejecuta el siguiente comando en la consola._

```
pip install -r requirements.txt

```
_Este comando instalará en nuestro entorno, todo lo necesario para que el proyecto funcione funciona correctamente._

### SETTINGS 🔧

Luego tenes que crear un archivo de configuraciones en la carpeta proyecto/settings/ y llamala "local.py", donde debes indicar las credenciales de tu base de datos como se muestra a continuacion.

```
from .base import *

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'databaseName',
        'USER': 'databaseUser',
        'PASSWORD': 'databasePassword',
        'HOST': 'localhost',
        'PORT': 'portNumber',
    }
}

```


## Construido con 🛠️

_Las herramientas utilizadas para el desarrollo fueron:_

* [Django](https://www.djangoproject.com/) Framework web
* [Python](https://www.python.org/) Del lado del servidor (backend)
* [Bootstrap](https://getbootstrap.com/) Framework web para el desarrollo frontend (HTML, CSS, JavaScript)
* [MySql](https://www.mysql.com/) - Sistema de gestión de bases de datos.


## Autor ✒️

_Proyecto desarrollado por:_ 


**Cerdan, David**


**Cardozo, Edgardo Javier**


**Feck, Gimena Lara**


**Lopez, Juan Pablo**


**Markevicz Vallejos, Milagros Vanina Edith**


**Marino, Luciano**


**Romero, Veronica Patricia**
 




[Contribuyentes](https://github.com/MilagrosMarkevicz/grupo1_DeFi/graphs/contributors)


