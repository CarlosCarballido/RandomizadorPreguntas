# Randomizador de Preguntas
## Spanish Version

Este programa en Python te permite cargar un conjunto de preguntas y respuestas desde un archivo JSON y luego mostrarlas de forma aleatoria. Es útil para realizar juegos de preguntas y respuestas de forma interactiva.

## Requisitos

- Python 3.x

## Instalación

1. Clona este repositorio en tu máquina local o descarga el archivo ZIP.
2. Asegúrate de tener Python 3.x instalado en tu sistema.
3. Ejecuta el archivo `randomizador_preguntas.py`.

## Uso

1. Coloca tus preguntas y respuestas en un archivo JSON con el siguiente formato:

    ```json
    {
        "preguntas": [
            {
                "id": 1,
                "pregunta": "Define el teorema de Deducción",
                "respuesta": ""
            },
            {
                "id": 2,
                "pregunta": "Define el teorema de Condicionalización",
                "respuesta": ""
            },
            ...
        ]
    }
    ```

2. Ejecuta el archivo `randomizador_preguntas.py [Ruta/archivo/JSON]`.
3. Sigue las instrucciones en pantalla para mostrar preguntas y sus respuestas de forma aleatoria.

## Contribución

Las contribuciones son bienvenidas. Si tienes alguna sugerencia, corrección de errores o función que te gustaría añadir, siéntete libre de abrir un issue o enviar un pull request.
