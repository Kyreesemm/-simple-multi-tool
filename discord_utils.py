
import requests

DISCORD_API_URL = "https://discord.com/api/v10"

def add_subparser(subparsers):
    parser = subparsers.add_parser('discord_utils', help='Утилиты для работы с Discord')
    parser.add_argument('--validate-token', help='Проверка валидности Discord токена', metavar='TOKEN')
    parser.add_argument('--get-user-info', help='Получение информации о пользователе по токену', metavar='TOKEN')
    parser.set_defaults(func=handle_discord_utils)

def handle_discord_utils(args):
    if args.validate_token:
        validate_discord_token(args.validate_token)
    elif args.get_user_info:
        get_user_info(args.get_user_info)

def validate_discord_token(token):
    headers = {
        "Authorization": f"Bot {token}"
    }
    response = requests.get(f"{DISCORD_API_URL}/users/@me", headers=headers)
    if response.status_code == 200:
        print("Токен валиден.")
    else:
        print("Токен невалиден или имеет недостаточные права.")

def get_user_info(token):
    headers = {
        "Authorization": f"Bot {token}"
    }
    response = requests.get(f"{DISCORD_API_URL}/users/@me", headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        print("Информация о пользователе:")
        print(f"ID: {user_info['id']}")
        print(f"Имя пользователя: {user_info['username']}#{user_info['discriminator']}")
        print(f"Электронная почта: {user_info.get('email', 'Не доступно')}")
    else:
        print("Не удалось получить информацию о пользователе. Токен может быть невалиден или иметь недостаточные права.")
