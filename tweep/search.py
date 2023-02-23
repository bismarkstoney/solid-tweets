import tweepy
import configparser
import pandas as pd

# read configs
consumer_key="QCrju6WNwJBXHhe2P3MYOLHlU"
consumer_secret_key="wlPbD9RqWlFvgcsfUirXhp1Gem62e5aTfs09CIuyzMivHXAtWm"
access_token="900767746992078848-DMrc98KDLPjQcrlOwWsZQvpueskRtNM"
access_secret_token="jnjGgOV0lJnuaJ7ULomulhH5OwOcjcpzSG2P8HyRpauth"

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

