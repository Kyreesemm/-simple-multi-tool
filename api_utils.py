
import requests
import wikipediaapi

WEATHER_API_KEY = 'YOUR_API_KEY'
EXCHANGE_API_KEY = 'YOUR_API_KEY'

def add_subparser(subparsers):
    parser = subparsers.add_parser('api_tools', help='Работа с API')
    parser.add_argument('--weather', help='Получение текущей погоды для города', metavar='CITY')
    parser.add_argument('--convert', nargs=2, help='Конвертация валют из одной в другую', metavar=('FROM', 'TO'))
    parser.add_argument('--wiki', help='Поиск информации в Wikipedia', metavar='QUERY')
    parser.set_defaults(func=handle_api_tools)

def handle_api_tools(args):
    if args.weather:
        get_weather(args.weather)
    elif args.convert:
        convert_currency(args.convert[0], args.convert[1])
    elif args.wiki:
        search_wikipedia(args.wiki)

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric',
        'lang': 'ru'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"Погода в {city}: {weather_description}, температура: {temperature}°C")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе погоды: {e}")
    except KeyError:
        print("Не удалось получить данные о погоде. Проверьте правильность названия города.")

def convert_currency(from_currency, to_currency):
    base_url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/pair/{from_currency}/{to_currency}"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()
        rate = data['conversion_rate']
        print(f"Курс {from_currency} к {to_currency}: {rate}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе курса валют: {e}")
    except KeyError:
        print("Не удалось получить данные о курсе валют.")

def search_wikipedia(query):
    wiki_wiki = wikipediaapi.Wikipedia('ru')
    page = wiki_wiki.page(query)
    
    if page.exists():
        print(f"Страница Wikipedia: {page.title}\n")
        print(page.summary[:500])
    else:
        print("Страница не найдена в Wikipedia.")
