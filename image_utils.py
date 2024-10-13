
from PIL import Image, ImageDraw, ImageFont
import os

def add_subparser(subparsers):
    parser = subparsers.add_parser('image_tools', help='Работа с изображениями')
    parser.add_argument('--resize', nargs=3, help='Изменение размера изображения', metavar=('INPUT', 'OUTPUT', 'SIZE'))
    parser.add_argument('--convert', nargs=3, help='Конвертация изображения в другой формат', metavar=('INPUT', 'OUTPUT', 'FORMAT'))
    parser.add_argument('--text', nargs=4, help='Наложение текста на изображение', metavar=('INPUT', 'OUTPUT', 'TEXT', 'POSITION'))
    parser.set_defaults(func=handle_image_tools)

def handle_image_tools(args):
    if args.resize:
        resize_image(args.resize[0], args.resize[1], args.resize[2])
    elif args.convert:
        convert_image(args.convert[0], args.convert[1], args.convert[2])
    elif args.text:
        add_text_to_image(args.text[0], args.text[1], args.text[2], args.text[3])

def resize_image(input_path, output_path, size):
    try:
        with Image.open(input_path) as img:
            width, height = map(int, size.split('x'))
            img = img.resize((width, height))
            img.save(output_path)
            print(f"Изображение сохранено: {output_path}")
    except Exception as e:
        print(f"Ошибка при изменении размера изображения: {e}")

def convert_image(input_path, output_path, format):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format=format.upper())
            print(f"Изображение сконвертировано и сохранено: {output_path}")
    except Exception as e:
        print(f"Ошибка при конвертации изображения: {e}")

def add_text_to_image(input_path, output_path, text, position):
    try:
        with Image.open(input_path) as img:
            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()
            x, y = map(int, position.split(','))
            draw.text((x, y), text, font=font, fill=(255, 255, 255))
            img.save(output_path)
            print(f"Текст добавлен и изображение сохранено: {output_path}")
    except Exception as e:
        print(f"Ошибка при наложении текста на изображение: {e}")
