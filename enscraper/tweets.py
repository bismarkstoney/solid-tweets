import pandas as pd
import snscrape.modules.twitter as sntwitter

query = "(from:ASAMOAH_GYAN3) until:2022-12-31 since:2014-12-20"
tweets = []
limit = 10 # can be up to a million 

columns = ["username", "text", "createdAt"]
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
   
    if len(tweets) == limit:
        break
    else:
        tweets.append(
            [
              
                tweet.user.username,
                tweet.rawContent,
                tweet.date,
            ]
        )
   

df = pd.DataFrame(tweets, columns=columns)
df.to_json('test.json', orient='records')

