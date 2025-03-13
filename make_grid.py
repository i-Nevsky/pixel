from PIL import Image, ImageDraw, ImageFont

def create_grid_image(input_path, output_path, step=50):
    """
    Рисует сетку с заданным шагом (step) на изображении
    и проставляет числовые координаты вдоль линий.
    """
    # Открываем исходное изображение
    img = Image.open(input_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    
    width, height = img.size

    # Если есть шрифт (например, roboto.ttf) – укажи путь к нему
    # Если нет, Pillow возьмет шрифт по умолчанию
    try:
        font = ImageFont.truetype("roboto.ttf", 20)
    except:
        font = None  # тогда будет использоваться шрифт по умолчанию

    # Рисуем вертикальные линии и подписываем координаты
    for x in range(0, width+1, step):
        # Линия
        draw.line([(x, 0), (x, height)], fill=(255, 0, 0, 128), width=1)
        # Подпись координаты x (если не выходим за пределы)
        if x < width:
            draw.text((x+2, 0), f"x={x}", fill=(255, 0, 0, 255), font=font)

    # Рисуем горизонтальные линии и подписываем координаты
    for y in range(0, height+1, step):
        # Линия
        draw.line([(0, y), (width, y)], fill=(255, 0, 0, 128), width=1)
        # Подпись координаты y
        if y < height:
            draw.text((0, y+2), f"y={y}", fill=(255, 0, 0, 255), font=font)

    # Сохраняем результат
    img.save(output_path)

if __name__ == "__main__":
    # Путь к твоему изображению без сетки
    input_image = "base_image.png"
    # Путь, куда сохранить результат с сеткой
    output_image = "base_image_grid.png"

    create_grid_image(input_image, output_image, step=50)
    print("Сетка с координатами сохранена в", output_image)
