import json

def getPinyin(character):
    fin = open('characters/pinyin.txt', 'r', encoding='utf-8')
    myDict = json.loads(fin.read())
    fin.close()
    return myDict[character]
