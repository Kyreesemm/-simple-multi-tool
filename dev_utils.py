
import json
import uuid
import base64

def add_subparser(subparsers):
    parser = subparsers.add_parser('dev_utils', help='Утилиты для разработчиков')
    parser.add_argument('--validate-json', help='Проверка валидности JSON', metavar='JSON_STRING')
    parser.add_argument('--generate-uuid', action='store_true', help='Генерация UUID')
    parser.add_argument('--encode-base64', help='Кодирование строки в Base64', metavar='STRING')
    parser.add_argument('--decode-base64', help='Декодирование строки из Base64', metavar='BASE64_STRING')
    parser.set_defaults(func=handle_dev_utils)

def handle_dev_utils(args):
    if args.validate_json:
        validate_json(args.validate_json)
    elif args.generate_uuid:
        generate_uuid()
    elif args.encode_base64:
        encode_base64(args.encode_base64)
    elif args.decode_base64:
        decode_base64(args.decode_base64)

def validate_json(json_string):
    try:
        json_object = json.loads(json_string)
        print("JSON валиден.")
    except json.JSONDecodeError as e:
        print(f"Ошибка: Невалидный JSON. {e}")

def generate_uuid():
    new_uuid = uuid.uuid4()
    print(f"Сгенерированный UUID: {new_uuid}")

def encode_base64(input_string):
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    print(f"Base64 кодированная строка: {encoded_string}")

def decode_base64(base64_string):
    try:
        decoded_bytes = base64.b64decode(base64_string)
        decoded_string = decoded_bytes.decode('utf-8')
        print(f"Декодированная строка: {decoded_string}")
    except Exception as e:
        print(f"Ошибка при декодировании Base64: {e}")
