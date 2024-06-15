import random as rnd
import pickle


class Mine:
    def __init__(self):
        res = ['уголь', 'медь', 'железо', 'золото']
        tp = rnd.randint(1, 4)
        self.resource = res[tp]
        self.deep = 0

    def dig(self):
        self.deep += 1
        return self.resource, rnd.randint(1, 4)


mine1 = Mine()
print('шахта добывает', mine1.resource)

a = mine1.dig()
print('шахта добыла', a[1], a[0])

mine1.dig()
mine1.dig()
print('глубина шахты', mine1.deep)

with open("aaa.bin", "wb") as fl:
    pickle.dump("что тут происходит?", fl)
