import requests
from time import time

# URL для отправки POST-запроса с количеством тапов
url = "https://api.hamsterkombat.io/clicker/tap"

# Заголовки запроса
headers = {
    "Connection":	"keep-alive",
    "sec-ch-ua":	'"Chromium";v="122", "Not(A:Brand";v="24", "Android WebView";v="122"',
    "sec-ch-ua-mobile":	'?1',
    "User-Agent":	"Mozilla/5.0 (Linux; Android 11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.64 Mobile Safari/537.36",
    "sec-ch-ua-platform":	'"Android"',
    "Accept":	"*/*",
    "Origin":	"https://hamsterkombat.io",
    "X-Requested-With":	"org.telegram.messenger",
    "Sec-Fetch-Site":	"same-site",
    "Sec-Fetch-Mode":	"cors",
    "Sec-Fetch-Dest":	"empty",
    "Referer":	"https://hamsterkombat.io/",
    "Accept-Encoding":	"gzip, deflate, br",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN ",  # Замените YOUR_ACCESS_TOKEN на ваш токен авторизации
}

#Получаем timestamp для запроса
def timestamp():
    return int(time())

# Данные для POST-запроса
data = {
    "count": 1000, #  количество кликов
    "availableTaps": 0, #  количество доступных кликов
    "timestamp": timestamp()
}

def send_post_request():
    """
    Функция для отправки POST-запроса
    """
    with requests.Session() as session:
        response = session.post(url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            print("POST-запрос успешно отправлен:", result)
        else:
            print("Ошибка при отправке POST-запроса:", response.status_code, response.text)


        balance = result['clickerUser']['balanceCoins']
        availableTaps = result['clickerUser']['availableTaps']
        print(f'''
                Balance: {balance}
                Available Taps: {availableTaps}

            ''')



if __name__ == "__main__":
    send_post_request()
