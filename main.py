
import argparse
import file_system
import text_utils
import network_utils
import api_utils
import image_utils
import dev_utils
import discord_utils
import system_utils
import security_utils
import entertainment

def main():
    parser = argparse.ArgumentParser(description="Мульти-инструмент CLI")
    subparsers = parser.add_subparsers(dest='command')

    file_system.add_subparser(subparsers)
    text_utils.add_subparser(subparsers)
    network_utils.add_subparser(subparsers)
    api_utils.add_subparser(subparsers)
    image_utils.add_subparser(subparsers)
    dev_utils.add_subparser(subparsers)
    discord_utils.add_subparser(subparsers)
    system_utils.add_subparser(subparsers)
    security_utils.add_subparser(subparsers)
    entertainment.add_subparser(subparsers)

    args = parser.parse_args()
    if args.command:
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()