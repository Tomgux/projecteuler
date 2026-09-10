one = 3 # one, two
three = 5 # three, seven, eight
four = 4 # four, five, nine
six = 3 # six

ten = 3 # ten
eleven = 6 # eleven, twelve
thirteen = 8 # thirteen, fourteen, eighteen, nineteen
fifteen = 7 # fifteen, sixteen
seventeen = 9 # seventeen

twenty = 6 # twenty, thirty, eighty, ninety
fifty = 5 # fifty, sixty, forty
seventy = 7 # seventy

hundredand = 10 # ___ hundred and ___
hundred = 7 # hundred

answer = 0
for i in range(1, 1000):
    number = i

    if number > 99:
        hundreds = number // 100
        if (number%100==0):
            answer = answer + hundred
        else:
            answer = answer + hundredand
        if hundreds == 6:
            answer = answer + six
        elif hundreds == 1 or hundreds == 2:
            answer = answer + one
        elif hundreds == 3 or hundreds == 7 or hundreds == 8:
            answer = answer + three
        else:
            answer = answer + four
        number = number % 100

    if number > 9 and number < 20:
        if number == 11 or number == 12:
            answer = answer + eleven
            continue
        elif number == 13 or number == 14 or number == 18 or number == 19:
            answer = answer + thirteen
            continue
        elif number == 17:
            answer = answer + seventeen
            continue
        elif number == 10:
            answer = answer + ten
            continue
        else:
            answer = answer + fifteen
            continue

    if number >= 20:
        if number > 39 and number < 70:
            answer = answer + fifty
            number = number % 10
        elif number > 69 and number < 80:
            answer = answer + seventy
            number = number % 10
        else:
            answer = answer + twenty
            number = number % 10

    if number != 0:
        if number == 6:
            answer = answer + six
        elif number == 1 or number == 2:
            answer = answer + one
        elif number == 3 or number == 7 or number == 8:
            answer = answer + three
        else:
            answer = answer + four

answer = answer + 11 # one thousand
print(answer)

