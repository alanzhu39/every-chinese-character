import random
import json

fin = open('TGSCC-Unicode.txt', 'r', encoding='utf-8')
fout = open('characters.txt', 'w', encoding='utf-8')

fin.readline()
fin.readline()

clist = []

line = fin.readline()
while line != '':
    clist.append(chr(int(line.split()[1][2:], 16)))
    line = fin.readline()

random.shuffle(clist)
fout.write(json.dumps(clist))

fin.close()
fout.close()
