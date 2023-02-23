import tweepy
import configparser
import pandas as pd

# read configs
consumer_key=""
consumer_secret_key=""
access_token=""
access_secret_token=""

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_secret_token)

api = tweepy.API(auth)

keywords = '@veritasium'
limit=300

tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended').items(limit)


columns = ['avatar', 'username', 'text', 'createdAt']
data = []

for tweet in tweets:
    data.append([tweet.user.profile_image_url_https, tweet.user.screen_name, tweet.full_text, tweet.created_at])

df = pd.DataFrame(data, columns=columns)
df.to_json('test.json', orient='records')

