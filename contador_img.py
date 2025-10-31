import os
from PIL import Image, ImageDraw, ImageFont
from datetime import date

# EDITABLE: Cambia esta ruta a tu directorio base donde están los archivos
ruta_base = r"."
# EDITABLE: Cambia el nombre de tu imagen base si es diferente
ruta_imagen = os.path.join(ruta_base, "base.jpg")
# EDITABLE: Cambia el nombre de tu fuente personalizada si es diferente
ruta_fuente = os.path.join(ruta_base, "Montserrat.ttf")
# EDITABLE: Cambia la ruta de salida donde se guardará la imagen generada
ruta_salida = r"C:\Users\iamvi\Desktop\dias.jpg"
# EDITABLE: Cambia tu fecha de nacimiento (año, mes, día)
fecha_nacimiento = date(2007, 4, 2)
hoy = date.today()
diasvividos = (hoy - fecha_nacimiento).days

if not os.path.exists(ruta_imagen):
    print("No se encontró el archivo 'base.jpg'.")
    exit()
if not os.path.exists(ruta_fuente):
    print("⚠️ No se encontró 'mi_fuente.ttf'. Se usará la fuente por defecto.")
    fuente = ImageFont.load_default()
else:
    # EDITABLE: Cambia el tamaño de la fuente
    fuente = ImageFont.truetype(ruta_fuente, 150)

img = Image.open(ruta_imagen).convert("RGB")

# EDITABLE: Cambia el tamaño de la imagen de salida (ancho, alto)
img = img.resize((1920, 1080))

draw = ImageDraw.Draw(img)

# EDITABLE: Cambia el mensaje que se mostrará en la imagen
texto = f"Ya llevas {diasvividos} días"

# EDITABLE: Cambia la posición del texto en la imagen (x, y)
x, y = 250, 250

# EDITABLE: Cambia los efectos del texto (sombra, borde, colores)
sombra_offset = 10
border_offset = 4
border_color = (0, 0, 0)

# Sombra
draw.text((x + sombra_offset, y + sombra_offset), texto, font=fuente, fill=(0, 0, 0))

# Borde
for dx in range(-border_offset, border_offset + 1):
    for dy in range(-border_offset, border_offset + 1):
        if dx == 0 and dy == 0:
            continue
        draw.text((x + dx, y + dy), texto, font=fuente, fill=border_color)

# Texto principal
draw.text((x, y), texto, font=fuente, fill=(255, 255, 255))

# EDITABLE: Cambia la calidad de la imagen de salida (0-100)
img.save(ruta_salida, format="JPEG", quality=95)

print(f"✅ Imagen generada correctamente en: {ruta_salida}")