# Из предложенного текстового файла (text18-5.txt) вывести на экран его содержимое, количество символов. в тексте
# Сформировать новый файл, в который поместить текст в стихотворной форме предварительно заменив символы нижнего
# регистра на верхний

with open('text18-5.txt', 'r', encoding='utf-16') as f:
    t = f.read()

print(t)
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(t.upper())
