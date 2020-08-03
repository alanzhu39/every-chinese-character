import json

fin = open('Unihan_Readings.txt', 'r', encoding='utf-8')
fout = open('pinyin.txt', 'w', encoding='utf-8')

myDict = {}

line = fin.readline()
while line != '':
    if line[0] == 'U':
        words = line.split()
        if words[1] == 'kMandarin':
            key = chr(int(words[0][2:], 16))
            myDict[key] = words[2]
    line = fin.readline()

fout.write(json.dumps(myDict))

fin.close()
fout.close()
