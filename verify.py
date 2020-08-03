import json

pfile = open('characters/pinyin.txt', 'r', encoding='utf-8')
cfile = open('characters/characters.txt', 'r', encoding='utf-8')

myDict = json.loads(pfile.read())
cSet = set(myDict.keys())

clist = json.loads(cfile.read())

for i in range(len(clist)):
    if clist[i] not in cSet:
        print(i)

pfile.close()
cfile.close()
