# BlueWallet Backend

BlueWallet Backend es el componente de backend de la aplicación BlueWallet, una plataforma de billetera virtual desarrollada en Django Rest Framework. Proporciona una API-REST para la gestión de billeteras virtuales y operaciones financieras en fondos Money-Market.

## Características

- API-REST robusta y escalable.
- Integración con PostgreSQL para almacenamiento de datos.
- Integración con Redis para gestión de caché y rendimiento óptimo.
- Implementación de seguridad mediante autenticación y autorización de usuarios.
- Pruebas unitarias y de integración para garantizar la calidad del código.

## Requisitos del sistema

- Python 3.x
- Django 3.x
- Django Rest Framework 3.x
- PostgreSQL
- Redis

## Configuración y ejecución (Not Available Yet)

1. Clona este repositorio: `git clone https://github.com/CtrlCri/BlueWallet.git`
2. Ve al directorio del proyecto: `cd bluewallet-backend`
3. Crea y activa un entorno virtual: `python3 -m venv venv && source venv/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Configura las variables de entorno en el archivo `.env` según tus preferencias.
6. Realiza las migraciones de la base de datos: `python manage.py migrate`
7. Inicia el servidor de desarrollo: `python manage.py runserver`

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, por favor crea un pull request explicando los cambios propuestos.

## Licencia

Este proyecto se encuentra bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
