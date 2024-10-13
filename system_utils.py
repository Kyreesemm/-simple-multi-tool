
import platform
import psutil
import os
import subprocess

def add_subparser(subparsers):
    parser = subparsers.add_parser('system_utils', help='Утилиты для управления системой')
    parser.add_argument('--system-info', action='store_true', help='Получение информации о системе')
    parser.add_argument('--monitor', action='store_true', help='Мониторинг использования ЦП и памяти')
    parser.add_argument('--shutdown', action='store_true', help='Выключение компьютера')
    parser.add_argument('--reboot', action='store_true', help='Перезагрузка компьютера')
    parser.set_defaults(func=handle_system_utils)

def handle_system_utils(args):
    if args.system_info:
        get_system_info()
    elif args.monitor:
        monitor_resources()
    elif args.shutdown:
        shutdown_system()
    elif args.reboot:
        reboot_system()

def get_system_info():
    print("Информация о системе:")
    print(f"Система: {platform.system()}")
    print(f"Имя узла: {platform.node()}")
    print(f"Релиз: {platform.release()}")
    print(f"Версия: {platform.version()}")
    print(f"Архитектура: {platform.machine()}")
    print(f"Процессор: {platform.processor()}")

def monitor_resources():
    print("Мониторинг использования ресурсов:")
    print(f"Использование ЦП: {psutil.cpu_percent(interval=1)}%")
    memory = psutil.virtual_memory()
    print(f"Использование памяти: {memory.percent}%")

def shutdown_system():
    print("Выключение системы...")
    if platform.system() == "Windows":
        os.system("shutdown /s /t 1")
    else:
        os.system("shutdown now")

def reboot_system():
    print("Перезагрузка системы...")
    if platform.system() == "Windows":
        os.system("shutdown /r /t 1")
    else:
        os.system("reboot")
