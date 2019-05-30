class Wallet:
    money = 0

     # 처음 객체가 생성될때
    def __init__(self, name):
        print("{}님 환영합니다.".format(name))
        self.owner = name

    def __str__(self):
        # return super().__str__() # 객체명 호출
        return '{}의 지갑입니다'.format(self.owner)
    
    def __repr__(self):
        return '{}의 지갑입니다'.format(self.owner)

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

class ChildWallet(Wallet):
    pass


sol_w = ChildWallet('sol')
sol_w.print_owner_name()
sol_w.income(250000)

# 상속 확인하는 메서드 issubclass
print("ChildWallet class는 Wallet class 상속받았다: ",issubclass(ChildWallet, Wallet))

class Account(Wallet):
    def __init__(self, name, account_number):
        self.owner = name
        self.account_number = account_number # 계좌 기능 추가
        super().__init__(name) # 부모클래스 호출

    def __str__(self):
        return '{}의 계좌입니다. 계좌번호 : {}'.format(self.owner, self.account_number)


    def __repr__(self):
        return '{}의 계좌입니다. 계좌번호 : {}'.format(self.owner, self.account_number)

    def __add__(self, another):
        return self.money + another.money

    def send_money(self, money, to):
        if self.money > money:
            to.money += money # 받는 사람은 돈증가
            self.money -= money # 보내는 사람은 돈 감소
            print("{}원을 {}에게 보냈습니다.".format(money, to.owner))
            self.print_now_money()

sola_a = Account('sola', '123-123456')

sola_a.account_number

print(sola_a)
print("__str__: ",sola_a.__str__())
print("__repr__:",sola_a.__repr__())
print(sola_a.account_number)

sola_a.income(150000)
sola_a.send_money

sola_b = Account('sola_b', '123-234-678')
print(sola_b)
sola_b.income(100000)
sola_b.print_now_money

sola_c = sola_a + sola_b # 계좌의 합
print("a와b 계좌의 합은",sola_c)
print("sola_a 잔액: ",sola_a.money)
print("sola_b 잔액: ",sola_b.money)

# special method
# __str__()
# __call__()
# __add()__(y)