NAME = input()
SALARY = float(input())
VENDAS = float(input())

BONUS = VENDAS * 0.15
TOTAL = BONUS + SALARY

print('TOTAL = R$ {:.2f}'.format(TOTAL))
