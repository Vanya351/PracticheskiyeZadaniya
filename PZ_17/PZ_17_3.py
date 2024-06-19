"""
с использованием модуля ОС
перейти в каталог PZ_11. вывести список файлов (каталоги не надо).
перейти в корень проекта и создать папку test, в ней test1. в test перместить два файла из ПЗ6, в test1 1 из ПЗ7. файл
из ПЗ7 переименовать в test.txt, вывести информацию о размере файлов в папке test.
перейти в папку ПЗ11. найти файл с самым коротким именем и вывести его в консоль. использовать функцию os.basename()
перейти в папку, где есть отчёт .pdf и запустить его в программе os.startfile()
удалить файл test.txt
"""

import os

# создадим новые файлы, чтобы не задеть практички
open("../PZ_6/pz6fl1.txt", "w").close()
open("../PZ_6/pz6fl2.txt", "w").close()
open("../PZ_7/pz7fl1.txt", "w").close()
open("../PZ_11/sh.txt", "w").close()

os.chdir("../PZ_11")
print('файлы в PZ_11:', end=' ')
fls = [i for _, __, i in os.walk(".")]
for i in fls[0]:
    print(i, end=' ')

os.chdir("..")
if not os.path.isdir("test"):
    os.mkdir("test")
os.chdir("test")
if not os.path.isdir("test1"):
    os.mkdir("test1")

os.rename("../PZ_6/pz6fl1.txt", "pz6fl1.txt")
os.rename("../PZ_6/pz6fl2.txt", "pz6fl2.txt")
os.rename("../PZ_7/pz7fl1.txt", "test1/pz7fl1.txt")
os.rename("test1/pz7fl1.txt", "test.txt")

os.chdir("../PZ_11")
min_file = sorted(os.listdir(), key=lambda i: len(i))[0]
print("\nфайл с коротчайшим именем PZ_11:", os.path.basename(min_file))

os.chdir("../reports")
os.startfile("PZ_3.pdf")
print("запущен файл PZ_3.pdf")
