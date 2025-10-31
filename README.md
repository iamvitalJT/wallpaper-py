# Contador de Días Vividos

Este proyecto es un script en Python que genera una imagen con el conteo de días vividos desde una fecha de nacimiento especificada. Puedes cambiar la imagen base, añade texto con efectos visuales como sombra y borde.

## Funcionamiento

El script `contador_img.py` realiza los siguientes pasos:

1. Carga una imagen base desde el directorio especificado.
2. Calcula los días transcurridos desde la fecha de nacimiento hasta la fecha actual.
3. Dibuja el texto con el conteo de días sobre la imagen, aplicando efectos de sombra y borde para mayor legibilidad.
4. Guarda la imagen resultante en la ruta de salida especificada.

## Requisitos

- Python 3.x
- Biblioteca PIL (Pillow): `pip install pillow`
- Una imagen base en formato JPG (por defecto `base.jpg`)
- Una fuente TrueType (por defecto `Montserrat.ttf`)

## Configuración Editable

El código incluye comentarios marcados como "EDITABLE" que indican las partes que puedes modificar para personalizar el script:

- **Rutas de archivos**: Cambia las rutas base, imagen, fuente y salida según tu estructura de directorios.
- **Fecha de nacimiento**: Modifica la fecha en `date(año, mes, día)` para calcular los días desde tu nacimiento.
- **Tamaño de imagen**: Ajusta las dimensiones de la imagen de salida.
- **Mensaje de texto**: Personaliza el texto que se mostrará en la imagen.
- **Posición del texto**: Cambia las coordenadas x, y para reposicionar el texto.
- **Efectos visuales**: Modifica los valores de sombra, borde y colores para cambiar la apariencia del texto.
- **Tamaño de fuente**: Ajusta el tamaño de la fuente utilizada.
- **Calidad de imagen**: Cambia la calidad de compresión JPEG de la imagen de salida.

## Ejecución Automática

Para ejecutar el script automáticamente al iniciar Windows:

1. Copiar el acceso directo `Ejecutable.bat`.
2. Usar Windows + R, escribir `shell:startup`.
3. Pegar el acceso directo en la carpeta de inicio.

Esto hará que el script se ejecute cada vez que enciendas tu dispositivo, generando una nueva imagen con el conteo actualizado de días vividos.