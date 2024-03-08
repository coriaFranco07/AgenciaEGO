# Franco Coria Zaragoza

# Proyecto Django de Agencia de Autos

Este repositorio contiene el código fuente de un proyecto Django para una agencia de autos.

## Requisitos previos

- Python 3.x instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- Git instalado en tu sistema. Puedes descargarlo desde [git-scm.com](https://git-scm.com/downloads/).

## Pasos para levantar el proyecto localmente

1. Clona este repositorio en tu máquina local utilizando Git:

    ```bash
    git clone https://github.com/coriaFRanco07/AgenciaEGO.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd agencia-autos
    ```

3. Crea un entorno virtual para el proyecto (opcional pero recomendado):

    ```bash
    python -m venv venv
    ```

4. Activa el entorno virtual (si creaste uno):

    - En Windows:

    ```bash
    venv\Scripts\activate
    ```

    - En macOS y Linux:

    ```bash
    source venv/bin/activate
    ```

5. Instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

6. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

7. Crea un superusuario para acceder al panel de administración (opcional):

    ```bash
    python manage.py createsuperuser
    ```

8. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

9. Abre tu navegador web y visita [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver el proyecto en funcionamiento.



