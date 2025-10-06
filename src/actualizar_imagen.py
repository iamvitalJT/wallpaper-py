import os
from PIL import Image, ImageDraw, ImageFont
from datetime import date

# 📂 Rutas de trabajo
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
ruta_imagen = os.path.join(project_root, "assets", "base.jpg")
ruta_fuente = os.path.join(project_root, "assets", "Montserrat.ttf")  # 🔤 tu fuente personalizada
ruta_salida = r"C:\Users\iamvi\OneDrive\Imágenes\Wallpapers\dias.jpg"
# 🧮 Calcular días vividos
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
    fuente = ImageFont.truetype(ruta_fuente, 150)

img = Image.open(ruta_imagen).convert("RGB")

img = img.resize((1920, 1080))

draw = ImageDraw.Draw(img)

# 📝 Texto a mostrar
texto = f"Ya llevas {diasvividos} días"

# 📍 Posición del texto (ajustable)
x, y = 250, 250

# 🎨 Sombra más notoria + borde negro + texto blanco
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

# 💾 Guardar como 'dias.jpg' (sin tocar base.jpg)
img.save(ruta_salida, format="JPEG", quality=95)
