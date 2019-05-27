
print('현재는 0원입니다. 일을 해야 돈을 벌 수 있습니다.')
MY_MONEY =[0]

def spend(m):
    if MY_MONEY[0] > m:
        MY_MONEY[0] -= m
        print("{}를 사용했습니다. 남은 잔액:{}".format(m, MY_MONEY[0]))
    else:
        print("가지고 있는 돈이 부족합니다.")

def income(m):
    MY_MONEY[0] += m
    print("{}를 벌었습니다. 남은 잔액:{}".format(m, MY_MONEY[0]))

wallet = {
    'money' : MY_MONEY,
    'spend' : spend,
    'income' : income
}

print("잔고:" , wallet['money'])
wallet['income'](100000)
wallet['spend'](18000)
print(wallet['money'])