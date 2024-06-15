# Для класса из 1 задания создать функции save и load, позовляющие сохранять информацию из экземпляров класса в файл и
# загружать обратно. Использовать pickle для сериализации и десериализации объектов Python в бинарном формате

import pickle
import PZ_16_1


class SaveBank(PZ_16_1.Bank):
    def save(self, name):
        with open(f"{name}.bin", "wb") as fl:
            pickle.dump(self.money, fl)
            pickle.dump(self.percent, fl)

    def load(self, name):
        with open(f"{name}.bin", "rb") as fl:
            self.money = pickle.load(fl)
            self.percent = pickle.load(fl)


score1 = SaveBank(14.5, 300)
score1.save('score1.bin')

score1backup = SaveBank(0, 0)
score1backup.load('score1.bin')
print(score1backup.money, score1backup.percent)
