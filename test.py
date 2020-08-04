import tweepy

cfile = open('characters/characters.txt', 'r', encoding='utf-8')
credentials = open('credentials.txt', 'r')

interval = 10

consumer_key = credentials.readline().strip()
consumer_secret = credentials.readline().strip()
access_key = credentials.readline().strip()
access_secret = credentials.readline().strip()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

statuses = api.user_timeline('every_zi')

print(statuses[0].text)

cfile.close()
credentials.close()
