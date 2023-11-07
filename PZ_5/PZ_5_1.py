# С помощью функций получить вертикальную и горизонтальную линии. Линия проводиться многократной печатью символа
# Заключить слово в рамку из полученных линий

def line(slovo, sim):
    sm = sim + ' ' * (len(slovo) + 2) + sim
    slovo = sim + ' ' + slovo + ' ' + sim
    sim *= len(slovo)
    slovo = sim + '\n' + sm + '\n' + slovo + '\n' + sm + '\n' + sim
    return slovo


s = input("введите слово >> ")

c = ''
while len(c) != 1:
    c = input('введите 1 символ, который будет использоваться для рамки >> ')

b = line(s, c)
print('\n\n'+b)
