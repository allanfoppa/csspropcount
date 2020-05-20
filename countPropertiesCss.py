# import sys
# print(sys.version)
import re

counts = dict()
qtdProps = 0
qtdPropsRep = 0

for line in open('files/css/bulma.css', 'r'):
    matchObj = re.search("(.+;$|.+}$)", line)
    if matchObj:
        line = line.strip()
        words = line.split('; ')
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

lst = list()

for key, val in list(counts.items()):
    lst.append((val, key))
    lst.sort(reverse=True)
for key, val in lst[:]:
    qtdProps = qtdProps + 1
    if key > 1:
        x = 'vezes'
        qtdPropsRep = qtdPropsRep + 1
    else:
        x = 'vez'
    print('A propriedade', val.upper(), 'aparece', key, x)

print('Há', qtdProps, 'propriedades no seu projeto. Sendo', qtdPropsRep, 'repetidas')
