class Wallet:
    money = 0
    def __init__(self, name):
        self.oner = name

    def oner_name(self):
         print("my name is ", self.oner)

    def now_money(self):
        print("현재 잔액은: ",self.money)

    def income(self, m):
        self.money += m
        self.now_money()

    def spend(self, m):
        if self.money < m:
            print("잔액이 부족합니다.")
            self.now_money()
        else:
            self.money -= m
            print("{}를 지출했습니다.".format(m))
            self.now_money()



my_w = Wallet('macanic')
my_w.oner_name()
my_w.income(75000)
my_w.spend(10000)
my_w.now_money
