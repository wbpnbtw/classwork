month = ["Февраль", "Январь", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь",
         "Декабрь", "февраль", "январь", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь",
         "ноябрь", "декабрь"]
count = input("Введите количество сотрудников")
output = []
payall = 0
date_dir = input("Введите месяц подсчета ")
if date_dir in month:
    date_dir = date_dir
else:
    print("Ошибка ввода")
if count.isalpha():
    print("Ошибка")
for i in range(0, int(count)):
    name = input("Введите имя - ")
    date = input("Введите дату рождения(в текстовом виде) - ")
    if date in month:
        date = date
    else:
        print("ошибка ввода, требуется перезапуск программы(Секретарша не может данные ввести, позор)")
        break
    pay = input("Введите зп - ")
    if pay.isalpha():
        print("Ошибка ввода")
    else:
        if date == date_dir:
            pay = int(pay) + (int(pay) * 0.25)
        payall += int(pay)
    output.append(name)
    output.append(date)
    output.append(pay)
if len(output) == 0:
    print("ОШИБКА")
else:
    print(output, "ФОТ = ", payall, )
