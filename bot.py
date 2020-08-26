import tweepy
import time
import characters.pinyin as pinyin
import json
from os import environ

cfile = open('characters/characters.txt', 'r', encoding='utf-8')
clist = json.loads(cfile.read())
# curr = open('current.txt', 'r+')
# credentials = open('credentials.txt', 'r')

interval = 60 * 60 * 2
# interval = 10

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_key = environ['access_key']
access_secret = environ['access_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

while True:
    i = clist.index(api.user_timeline('every_zi')[0].text.split()[0]) + 1
    if i >= len(clist):
        break
    print('getting character {}'.format(i + 1))
    c = clist[i]
    message = c + " " + pinyin.getPinyin(c)
    api.update_status(message)
    time.sleep(interval)
api.update_status("Job done!")
cfile.close()
# curr.close()
# credentials.close()
