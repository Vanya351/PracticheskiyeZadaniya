# Из исходного текстового файла (ip_address.txt) из раздела "Частоупотребимые маски" перенести строки с нулевым
# четвёртым октетом, а во второй - все остальные. Посчитать количество полученных строк в каждом файле

import re

with open("ip_address.txt", "r", encoding="utf-8") as fl:
    exp = re.compile(r"Частоупотребимые маски[0-9\s.]+")
    st = fl.read()
    st = exp.findall(st)
    st = st[0]

exp = re.compile(r"[\d.]+\.0")
w1 = exp.findall(st)
w1 = '\n'.join(w1)

exp = re.compile(r"[\d.]{12}[1-9]\d+")
w2 = exp.findall(st)
w2 = '\n'.join(w2)

with open("null_oct.txt", "w") as fl:
    fl.write(w1)
    print('строк в файле с нулевым октетом', len([0 for i in w1 if i == '\n'])+1)

with open("not_null_oct.txt", "w") as fl:
    fl.write(w2)
    print('строк во втором файле', len([0 for i in w2 if i == '\n'])+1)
