# Actualizar Imagen

Un script en Python que genera un wallpaper con el número de días que has vivido.

## Configuración

1. Clona el repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`
3. Agrega tus recursos a la carpeta `assets/`:
   - `base.jpg`: Tu imagen base (preferiblemente 1920x1080 o similar).
   - `Montserrat.ttf`: Tu archivo de fuente.
4. Personaliza el script en `src/actualizar_imagen.py`:
   - Cambia `fecha_nacimiento` a tu fecha de nacimiento.
   - Ajusta `ruta_salida` a la ruta de salida deseada.
5. Ejecuta el script: `python src/actualizar_imagen.py`

## Personalización

- Para cambiar la fecha de nacimiento, edita `fecha_nacimiento = date(YYYY, MM, DD)`
- Para cambiar el texto o la posición, modifica las variables `texto` y `x, y`.
- Para fuente o imagen diferente, reemplaza los archivos en `assets/`.