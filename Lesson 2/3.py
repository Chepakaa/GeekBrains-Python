# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Через dict
user_dict = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
user = int(input("Введите месяц цифрой: "))
val_list = list(user_dict.values())
key_list = list(user_dict.keys())
for i in val_list:
    for a in i:
        if a == user:
            print(f"{user} месяц, относится к времени года: {key_list[val_list.index(i)]}")

# Через list
season_of_the_year = ["Зима", "Весна", "Лето", "Осень"]
months = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
user = int(input("Введите месяц цифрой: "))
for i in months:
    for a in i:
        if a == user:
            print(f"{user} месяц, относится к времени года: {season_of_the_year[months.index(i)]}")