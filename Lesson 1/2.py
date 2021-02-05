#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
total = int(input("Введите секунды: "))
seconds = total % 60
total = total - seconds
hours = total // 3600
total = total - (hours * 3600)
mins = total // 60
print(f"{hours}:{mins}:{seconds}")
