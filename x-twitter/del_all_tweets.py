import tweepy

# Ваши ключи доступа к Twitter API
API_KEY = "YOUR_API_KEY"
API_SECRET_KEY = "YOUR_API_SECRET_KEY"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

# Авторизация в Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def delete_all_tweets():
    # Получаем все твиты пользователя
    tweets = api.user_timeline(count=200, tweet_mode="extended")
    
    # Удаляем каждый твит поочередно
    for tweet in tweets:
        api.destroy_status(tweet.id)
        print(f"Deleted tweet with ID: {tweet.id}")

    print("All tweets have been deleted.")

if __name__ == "__main__":
    delete_all_tweets()
