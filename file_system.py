
import os

def add_subparser(subparsers):
    parser = subparsers.add_parser('file_system', help='Работа с файловой системой')
    parser.add_argument('--list', help='Просмотр файлов и папок', action='store_true')
    parser.add_argument('--search', help='Поиск файлов по имени')
    parser.add_argument('--size', help='Подсчет размера папки')
    parser.set_defaults(func=handle_file_system)

def handle_file_system(args):
    if args.list:
        list_files()
    elif args.search:
        search_files(args.search)
    elif args.size:
        folder_size(args.size)

def list_files():
    print("Список файлов и папок в текущей директории:")
    for item in os.listdir('.'):
        print(item)

def search_files(name):
    print(f"Поиск файлов с именем '{name}' в текущей директории и поддиректориях:")
    for root, dirs, files in os.walk('.'):
        for file in files:
            if name in file:
                print(os.path.join(root, file))

def folder_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fp = os.path.join(dirpath, file)
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    print(f"Общий размер папки '{path}': {total_size} байт")