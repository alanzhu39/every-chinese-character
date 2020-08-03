import tweepy
import time
import characters.pinyin as pinyin
import json

cfile = open('characters/characters.txt', 'r', encoding='utf-8')
clist = json.loads(cfile.read())
credentials = open('credentials.txt', 'r')

interval = 60 * 60 * 6
interval = 10

consumer_key = credentials.readline().strip('\n')
consumer_secret = credentials.readline().strip('\n')
access_key = credentials.readline().strip('\n')
access_secret = credentials.readline().strip('\n')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

api.update_status(clist[0])

"""
for i in range(len(clist)):
    print('getting character {}'.format(i + 1))
    c = clist[i]
    message = c + " " + pinyin.getPinyin(c)
    api.update_status(message)
    time.sleep(interval)
"""

cfile.close()
credentials.close()
