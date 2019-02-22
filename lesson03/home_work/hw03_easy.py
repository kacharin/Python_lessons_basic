# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


"""


def my_round(number, ndigits):
    number = str(number)
    ndigits = int(ndigits)
    
    # Находим где начинается дробная часть
    p = number.find('.', 0,)
    
    # Удаляем лишние знаки после запятой
    number = number[0:ndigits+p+1]
    
    # Достаем последнюю цифру, чтобы понять в какую сторону округлять
    e = number[len(number)-1:]

    if int(e) < 5:
        # Округляем в меньшую сторону, 
        # т.е. просто выводим число с нужным кол-вом знаков после запятой
        number = number[0:p+ndigits+1]
    else:
        # Создаем число z, на которое нужно увеличить, 
        # в случае, округления в большую сторону
        z = str(0.)
        i = 0
        while i < ndigits-2:
            z = z + str(0)
            i += 1
        z = z + str(1)
        z = float(z)
        
        number = float(number)
        number = number + z
        number = str(number)
        number = number[0:ndigits+p+1]
    return number

# Все примеры окруляются в большую сторону
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
# Добавим примеры, который окруляются в меньшую сторону, 
# и с другим кол-вом знаков после запятой
print(my_round(2.123454321, 5))
print(my_round(2.123454321, 6))
print(my_round(2.123454321, 4))

"""

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

"""

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    # Проверим правильный ли билет
    if len(ticket_number) == 6:
        # Считаем суммы начала и конца
        begin_sum = 0
        end_sum = 0
        i = 0
        while i < 6:
            if i < 3:
                begin_sum = begin_sum + int(ticket_number[i])
            else:
                end_sum = end_sum + int(ticket_number[i])
            i += 1
        # Сравниваем концы
        if begin_sum == end_sum:
            lucky_ticket = 'Это счастливый билет. Поздравляем!'
        else:
            lucky_ticket = 'Билет не счастливый...'
    else:
        lucky_ticket = 'Неправильный билет. Номер должен состоять из 6 чисел.'
    return lucky_ticket


# Тут варианты счастливых и неправильного билетов
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
# Добавим вариант не счастливого билета
print(lucky_ticket(483953))

"""