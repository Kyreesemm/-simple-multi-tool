
import random

def add_subparser(subparsers):
    parser = subparsers.add_parser('entertainment', help='Утилиты для развлечений')
    parser.add_argument('--random-number', type=int, nargs=2, help='Генерация случайного числа в заданном диапазоне', metavar=('MIN', 'MAX'))
    parser.add_argument('--guess-number', action='store_true', help='Игра "угадай число"')
    parser.add_argument('--rock-paper-scissors', action='store_true', help='Игра "камень, ножницы, бумага"')
    parser.add_argument('--random-joke', action='store_true', help='Генерация случайной шутки')
    parser.set_defaults(func=handle_entertainment_utils)

def handle_entertainment_utils(args):
    if args.random_number:
        number = generate_random_number(args.random_number[0], args.random_number[1])
        print(f"Случайное число: {number}")
    elif args.guess_number:
        play_guess_number()
    elif args.rock_paper_scissors:
        play_rock_paper_scissors()
    elif args.random_joke:
        tell_random_joke()

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def play_guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Угадайте число от 1 до 100.")
    
    while True:
        try:
            guess = int(input("Введите ваше предположение: "))
            attempts += 1
            if guess < number_to_guess:
                print("Больше!")
            elif guess > number_to_guess:
                print("Меньше!")
            else:
                print(f"Поздравляем! Вы угадали число {number_to_guess} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

def play_rock_paper_scissors():
    choices = ['камень', 'ножницы', 'бумага']
    computer_choice = random.choice(choices)
    user_choice = input("Выберите: камень, ножницы или бумага: ").lower()
    
    if user_choice not in choices:
        print("Некорректный выбор. Попробуйте снова.")
        return
    
    print(f"Компьютер выбрал: {computer_choice}")
    
    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")

def tell_random_joke():
    jokes = [
        "Почему программисты не любят природу? Слишком много багов.",
        "Какой язык программирования самый грустный? Питон, потому что он всегда в депрессии.",
        "Почему программисты путают Рождество с Хэллоуином? Потому что Oct 31 == Dec 25.",
        "Какой самый любимый напиток у программистов? Java.",
        "Почему программисты не могут быть хорошими садовниками? Потому что они не могут найти корень проблемы."
    ]
    print(random.choice(jokes))
