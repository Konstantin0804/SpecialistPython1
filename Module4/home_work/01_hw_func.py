# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    ticket_number = list(map(int,ticket_number))
    first_number = ticket_number[0]+ticket_number[1]
    last_number = ticket_number[-1]+ticket_number[-2]
    return first_number == last_number


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
