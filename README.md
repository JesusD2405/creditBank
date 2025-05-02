# Credit Bank

_Proyecto en Django Rest Framework, que contiene el desarrollo de una App Web para gestión de los procesos bancarios._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.

### Pre-requisitos 📋

1. [Docker](https://docs.docker.com/)

_Es importante tener instaladas las herramientas anteriormente mencionadas para iniciar los siguientes pasos._

## Instalación 🔧

_*** Preparando nuestras variables de entorno ***_

_Nos situamos en la raíz y hacemos una copia del archivo docker-compose.yml.dist (En caso de adaptar aun más la configuración se podría adaptar los cambios requeridos)_

```
 cp docker-compose.yml.dist docker-compose.yml
```

_También realizamos una copia del archivo docker-env.dist reemplazando la extensión del archivo por el nombre del ambiente (local)_

```
 cp docker-env.dist docker-env.local
```

_En nuestro nuevo archivo docker-env.local modificamos y adaptamos las variables de entorno del Docker_

_Finalmente, en la raíz del proyecto ejecutamos_

```
 docker compose --env-file=./docker-env.local up --build
```

_De esta manera tendríamos todos nuestros conenedores levantados._

_Si deseamos cargar y ejecutar la migraciones del proyecto, para tener una BD limpia, ejecutamos dentro del CONTENEDOR de la API:_

```
./manage.py makemigrations
./manage.py migrate
```

_Para crear el Super Usuario para Django Admin (Con este usuario puede acceder a las vistas administrativas):_

```
./manage.py createsuperuser
```

## Documentación de Api (Swagger) 📚

_Para ingresar a ver la documentación de la Api ingresamos la siguiente url en el navegador:_

```
/api/docs
```

## Acceso a vistas administrativas 🧪

_Para ingresar al login y poder gestionar las vistas (Clientes, Créditos y Bancos) debemos ya haber creado el usuario Admin (Especificado en la etapa de instalación), luego podemos acceder a nuestra URL principal (Por defecto http://localhost:8000 en caso de no haber modificado el puerto):_


## Despliegue 📦

_*** Preparando nuestras variables de entorno ***_

_Nos situamos en la raíz y hacemos una copia del archivo docker-compose.yml.dist (En caso de adaptar aun más la configuración se podría adaptar los cambios requeridos)_

```
 cp docker-compose.yml.dist docker-compose.yml
```

_Luego hacemos una copia del archivo docker-env.dist reemplazando la extensión del archivo por el nombre del ambiente a desplegar:_

1. dev (Desarrollo).
2. pre (Pre-Producción).
3. pro (Producción).

```
 cp docker-env.dist docker-env.ambiente
```

_En nuestro nuevo archivo docker-env.ambiente modificamos y adaptamos las variables de entorno del Docker_

_Finalmente, en la raíz del proyecto ejecutamos_

```
 docker compose --env-file=./docker-env.ambiente up --build
```

## Construido con 🛠️

_Herramientas utilizadas en el proyecto:_

- [Python V3.12](https://docs.python.org/es/3.12/) - Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código, se utiliza para desarrollar aplicaciones de todo tipo.
- [Pip V21.0.1](https://pypi.org/project/pip/) - Pip es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python.
- [Docker](https://docs.docker.com/compose/install/) - Es una tecnología de contenedorización de código abierto para crear y contener sus aplicaciones.
- [Django Rest Framework](https://www.django-rest-framework.org/) - El marco Django REST es un conjunto de herramientas potente y flexible para crear API web.
- [Django-safedelete](https://django-safedelete.readthedocs.io/en/latest/index.html) - Proporciona un modelo abstracto, que le permite recuperar o eliminar de forma transparente sus objetos, sin tener que eliminarlos de su base de datos..
- [JQuery](https://jquery.com/) - jQuery es una biblioteca multiplataforma de JavaScript, creada inicialmente por John Resig, que permite simplificar la manera de interactuar con los documentos HTML, manipular el árbol DOM, manejar eventos, desarrollar animaciones y agregar interacción con la técnica AJAX a páginas web.
- [JQuery Validation](https://jqueryvalidation.org/) - Plugin de jQuery facilita la validación de formularios del lado del cliente, a la vez que ofrece numerosas opciones de personalización.
- [Bootstrap v5.3](https://getbootstrap.com/) - Potente kit de herramientas frontend extensible y repleto de funciones. Crea y personaliza con Sass, utiliza componentes y sistemas de cuadrícula prediseñados, y dale vida a tus proyectos con potentes plugins de JavaScript.
- [Sweetalert2](https://getbootstrap.com/) - Un reemplazo hermoso, responsivo, personalizable y accesible (WAI-ARIA) para los cuadros emergentes de JavaScript.

---

Desarrollado por [Jesús David Pérez](https://github.com/JesusD2405) ❤️🚀
