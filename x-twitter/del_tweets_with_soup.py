import requests
from bs4 import BeautifulSoup

# Замените данными свои учетные данные от аккаунта Twitter
username = 'your_username'
password = 'your_password'

# Войти в аккаунт Twitter, чтобы получить cookies
session = requests.session()
login_url = 'https://twitter.com/login'
response = session.get(login_url)
soup = BeautifulSoup(response.content, 'html.parser')
auth_token = soup.find('input', attrs={'name': 'authenticity_token'})['value']
login_data = {
    'session[username_or_email]': username,
    'session[password]': password,
    'authenticity_token': auth_token
}
session.post('https://twitter.com/sessions', data=login_data)

# Получить список всех твитов и удалить каждый твит
profile_url = f'https://twitter.com/{username}'
response = session.get(profile_url)
soup = BeautifulSoup(response.content, 'html.parser')
tweets = soup.find_all('div', class_='js-tweet-text-container')

for tweet in tweets:
    tweet_id = tweet['data-item-id']
    delete_url = f'https://twitter.com/i/api/1.1/statuses/destroy/{tweet_id}.json'
    session.post(delete_url)

print("Все твиты были удалены.")
