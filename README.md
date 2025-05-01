# Credit Bank

_Proyecto en Django Rest Framework, que contiene el desarrollo de una App Web Rest Full para gestión de los procesos de ....._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.

### Pre-requisitos 📋

1. [Docker](https://docs.docker.com/)
2. [PostgreSql](https://www.postgresql.org/download/)

_Es importante tener instaladas las herramientas anteriormente mencionadas para iniciar los siguientes pasos._

## Instalación 🔧

_*** Preparando nuestras variables de entorno ***_

_Nos situamos en la raíz y hacemos una copia del archivo docker-env.dist reemplazando la extensión del archivo por el nombre del ambiente (local)_

```
 cp docker-env.dist docker-env.local
```

_En nuestro nuevo archivo docker-env.local modificamos y adaptamos las variables de entorno del Docker_

_Finalmente, en la raíz del proyecto ejecutamos_

```
 docker compose --env-file=./docker-env.local up --build
```

_De esta manera tendríamos todos nuestros conenedores levantados._

_Si deseamos cargar una BD existente hacía nuestro contenedor de BD, ejecutamos:_

```
cat .\backup-app.sql | docker exec -i container-db psql -U USER -d NAME_DB
```

_Si deseamos cargar y ejecutar la migraciones del proyecto, para tener una BD limpia, ejecutamos dentro del CONTENEDOR de la API:_

```
./manage.py makemigrations
./manage.py migrate
```

_Para crear el Super Usuario para Django Admin:_

```
./manage.py createsuperuser
```

## Despliegue 📦

_*** Preparando nuestras variables de entorno ***_

_Nos situamos en el directorio "./docker" y hacemos una copia del archivo docker-env.dist reemplazando la extensión del archivo por el nombre del ambiente a desplegar:_

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

---

Desarrollado por [Jesús David Pérez](https://github.com/JesusD2405) ❤️🚀
