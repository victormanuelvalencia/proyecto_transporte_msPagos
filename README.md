# proyecto_transporte_MsPagos


Este es un microservicio de pagos desarrollado en Python utilizando **Flask** para la creación de la API y **ePayco** para procesar los pagos. El microservicio está diseñado para ser parte de una arquitectura basada en microservicios que maneja pagos electrónicos y envíos de notificaciones relacionadas.

## Tecnologías Utilizadas

- **Lenguaje**: Python 3.11.9
- **Framework**: Flask
- **Pasarela de Pagos**: ePayco SDK
- **Notificaciones**: Flask para envío de notificaciones por correo electrónico (opcional)

## Características

- **Integración con ePayco**: Maneja pagos de forma segura y eficiente utilizando la pasarela de pagos de ePayco.
- **Envío de Notificaciones**: El microservicio incluye una funcionalidad para enviar notificaciones después de realizar un pago.
- **API REST**: Diseño ligero de la API utilizando Flask, que permite integrar fácilmente este microservicio con otros sistemas.
- **Modularidad**: Código modular y fácil de mantener, ideal para una arquitectura de microservicios.

## Requisitos

- Python 3.11.9
- Flask
- ePayco SDK
- Flask-Mail (opcional, si se desea implementar el envío de correos)
  
## Instalación

1. Clona este repositorio en tu máquina local:
   
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
