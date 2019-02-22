# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

"""

def my_round(number, ndigits):
    number = str(number)
    ndigits = int(ndigits)
    
    # Находим место где целая часть отделяется от дробной
    p = number.find('.')
    
    # Создаем число на которое нужно увеличить
    # в случае округления в большую сторону
    okrup = str(0.)
    i = 0
    while i < ndigits-2:
        okrup = okrup + str(0)
        i += 1
    okrup = okrup + str(1)
    
    # Находим цифру, которая определяет куда округлять
    lastdigit = number[ndigits+p+1]
    
    if int(lastdigit) > 5:
        # Округление в большую сторону
        number = float(number) + float(okrup)
        number = str(number)
        number = number[0:ndigits+p+1]
    else:
        # Округление в меньшую сторону
        number = str(number)
        number = number[0:ndigits+p+1]
    return number

# Это все округляется в большую сторону
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
# Добавим пример с округлением в меньшую
print(my_round(235232.987654321, 7))

"""

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

"""

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    
    sum_begin = 0
    sum_end = 0
    
    if len(ticket_number) == 6:
        i = 0
        while i < 6:
            if i < 3:
                sum_begin = sum_begin + int(ticket_number[i])
            else:
                sum_end = sum_end + int(ticket_number[i])
            i += 1
        if sum_begin == sum_end:
            lucky_ticket = 'Ваш билет счастливый. Поздравляем!'
        else:
            lucky_ticket = 'К сожалению, билет не счастливый.'
    else:
        lucky_ticket = 'Неправильный билет. Номер должен состоять из 6 цифр.'
    return lucky_ticket


# Это примеры счастливого и неправильного билетов
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
# Добавим пример не счастливого билета
print(lucky_ticket(478682))

"""
