
import random
import string

def add_subparser(subparsers):
    parser = subparsers.add_parser('text_utils', help='Работа с текстом')
    parser.add_argument('--random', help='Генерация случайного текста', type=int, metavar='N')
    parser.add_argument('--count', help='Подсчет количества слов и символов', metavar='TEXT')
    parser.add_argument('--upper', help='Конвертация текста в верхний регистр', metavar='TEXT')
    parser.add_argument('--lower', help='Конвертация текста в нижний регистр', metavar='TEXT')
    parser.set_defaults(func=handle_text_utils)

def handle_text_utils(args):
    if args.random:
        generate_random_text(args.random)
    elif args.count:
        count_words_and_chars(args.count)
    elif args.upper:
        convert_to_upper(args.upper)
    elif args.lower:
        convert_to_lower(args.lower)

def generate_random_text(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    random_text = ''.join(random.choice(letters) for _ in range(length))
    print(f"Случайный текст ({length} символов): {random_text}")

def count_words_and_chars(text):
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    print(f"Количество слов: {num_words}, количество символов: {num_chars}")

def convert_to_upper(text):
    upper_text = text.upper()
    print(f"Текст в верхнем регистре: {upper_text}")

def convert_to_lower(text):
    lower_text = text.lower()
    print(f"Текст в нижнем регистре: {lower_text}")