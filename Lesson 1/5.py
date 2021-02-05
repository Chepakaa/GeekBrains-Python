finance = int(input("Введите сумму выручки: "))
expenses = int(input("Введите сумму расходов"))
if finance > expenses:
    print("Прибыль — выручка больше расходов")
    revenue = str(finance / expenses * 100)
    print(revenue + "%")
else:
    print("Убыток — расходы больше выручки")
people = int(input("Введите кол-во сотрудников: "))
profit = (finance - expenses) / people
print("Прибыль фирмы в расчете на одного сотрудника: " + str(profit))
