# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма 
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
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
