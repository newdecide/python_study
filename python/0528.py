# 클래스 생성
class Wallet:
    money = 0

     # 처음 객체가 생성될때
    def __init__(self, name):
        self.owner = name
    def print_owner_name(self):
        print('owner name is ',self.owner)

    def print_now_money(self):
        print("현재 잔액은 : ", self.money)

    def spend(self, m):
        if self.money < m:
            print("돈이 부족 합니다.")
            self.print_now_money()
        else:
            self.money -= m
            print("{}를 지출했습니다".format(m))
            self.print_now_money()

    def income(self, m):
        self.money += m
        self.print_now_money()

han_w = Wallet('han') # 변수에 클래스 객체 생성

han_w.print_owner_name()
han_w.income(200000)
han_w.spend(18000)

print()

bit_w = Wallet('bit')

bit_w.print_owner_name()
bit_w.income(250000)
bit_w.spend(45000)

