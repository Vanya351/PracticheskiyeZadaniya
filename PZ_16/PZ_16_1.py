# Создайте класс Банк, который имеет аттрибуты суммы денег и процентной ставки.
# Добавьте методы для вычисления процентных начислений и снятия денег

class Bank:
    def __init__(self, percent: float, money: float):
        self.percent = percent
        self.money = money

    def payment(self):
        newmoney = round(self.money * (1 + self.percent/100), 2) - self.money
        print("начисления: ", round(newmoney, 2))
        self.money += newmoney
        print("процент зачислен, на счету:", self.money)

    def take_money(self, amount: float):
        if self.money >= amount:
            self.money -= amount
            print("деньги сняты, на счету осталось:", self.money)
            return amount
        else:
            print("недостаточно средств на счету")
            return 0


if __name__ == "__main__":
    score = Bank(14.5, 300)
    score.payment()
    score.take_money(220)
    score.payment()
    score.payment()
