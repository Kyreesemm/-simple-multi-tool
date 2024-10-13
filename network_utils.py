
import os
import platform
import socket
import requests

def add_subparser(subparsers):
    parser = subparsers.add_parser('network_utils', help='Сетевые утилиты')
    parser.add_argument('--ping', help='Пинг до указанного адреса', metavar='ADDRESS')
    parser.add_argument('--ip', help='Получение текущего IP-адреса', action='store_true')
    parser.add_argument('--check', help='Проверка доступности сайта', metavar='URL')
    parser.set_defaults(func=handle_network_utils)

def handle_network_utils(args):
    if args.ping:
        ping_address(args.ping)
    elif args.ip:
        get_current_ip()
    elif args.check:
        check_website(args.check)

def ping_address(address):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = f"ping {param} 4 {address}"
    os.system(command)

def get_current_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Текущий IP-адрес: {ip_address}")

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Сайт {url} доступен.")
        else:
            print(f"Сайт {url} недоступен. Код состояния: {response.status_code}")
    except requests.ConnectionError:
        print(f"Сайт {url} недоступен.")
