import csv

data = open('cv19.csv').readlines()
# print('read {0} lines'.format(len(data)))

d8 = []
usdead = []
wwdead = []
prev_usdatum = 0
prev_wwdatum = 0
first = True
header = 'header'

for line in data:

    if first:
        first = False
        header = line[:-1]
        continue

    s = line[:-1].split()
    d8.append(s[0])
    try:
        usdead.append(int(s[1][:-1]))
    except:
        usdead.append(prev_usdatum)
    try:
        wwdead.append(int(s[2]))
    except:
        wwdead.append(prev_wwdatum)

    # print(d8[-1], usdead[-1], wwdead[-1])
    prev_usdatum = usdead[-1]
    prev_wwdatum = wwdead[-1]

print(header)
for i in range(len(d8)):
    print(d8[i], str(usdead[i])+',', wwdead[i])

