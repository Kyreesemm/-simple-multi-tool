
import secrets
import string
import hashlib

def add_subparser(subparsers):
    parser = subparsers.add_parser('security_utils', help='Утилиты для безопасности и приватности')
    parser.add_argument('--generate-password', type=int, help='Генерация безопасного пароля заданной длины', metavar='LENGTH')
    parser.add_argument('--hash-text', choices=['md5', 'sha256'], help='Хеширование текста', metavar='ALGORITHM')
    parser.add_argument('--text', type=str, help='Текст для хеширования', metavar='TEXT')
    parser.set_defaults(func=handle_security_utils)

def handle_security_utils(args):
    if args.generate_password:
        password = generate_secure_password(args.generate_password)
        print(f"Сгенерированный пароль: {password}")
    elif args.hash_text and args.text:
        hashed_text = hash_text(args.text, args.hash_text)
        print(f"Хешированный текст ({args.hash_text}): {hashed_text}")

def generate_secure_password(length=12):
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов.")
    
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def hash_text(text, algorithm='sha256'):
    if algorithm == 'md5':
        hash_object = hashlib.md5(text.encode())
    elif algorithm == 'sha256':
        hash_object = hashlib.sha256(text.encode())
    else:
        raise ValueError("Неподдерживаемый алгоритм хеширования.")
    
    return hash_object.hexdigest()
