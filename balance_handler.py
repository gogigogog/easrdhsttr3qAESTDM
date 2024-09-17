import requests

# В этом файле будет логика для взаимодействия с Telegram API

TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_CHAT_ID'


def get_stars(user_id):
    """
    Функция для получения количества звезд от пользователя через Telegram API.
    Эта функция будет обращаться к Telegram API и возвращать количество звезд.
    """
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getStars?chat_id={TELEGRAM_CHAT_ID}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        stars = data.get('result', {}).get('stars', 0)
        return stars
    else:
        return 0


def pop_stars(user_id):
    """
    Эта функция списывает звезды и возвращает количество списанных звезд.
    """
    stars = get_stars(user_id)

    if stars > 0:
        # Логика для списания звезд
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/useStars?chat_id={TELEGRAM_CHAT_ID}&amount={stars}"
        requests.get(url)
        return stars
    else:
        return 0
