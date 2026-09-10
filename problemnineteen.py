dayofweek = 1
dayofmonth = 1
month = 1
year = 1900

# We can simply iterate through years. We record anytime dayofweek = 7 while dayofmonth = 1
# To note, sep, apr, june, nov (month == 4, 6, 9) have 30 days
# Feb (month == 2) has 28 or 29
# Rest (else) have 31

count = 0
while year < 2001:

    if dayofweek == 7 and dayofmonth == 1:
        count = count+1

    dayofweek = dayofweek + 1
    dayofmonth = dayofmonth + 1

    if dayofweek == 8:
        dayofweek = 1

    if month == 4 or month == 6 or month == 9:
        if dayofmonth == 31:
            dayofmonth = 1
            month = month + 1
    elif month == 2:
        if year == 1900 or year == 2000:
            if year%400==0:
                # leap year
                if dayofmonth == 30:
                    dayofmonth = 1
                    month = month+1
            else:
                # not a leap year
                if dayofmonth == 29:
                    dayofmonth = 1
                    month = month+1
        elif year%4 == 0:
            # leap year
            if dayofmonth == 30:
                dayofmonth = 1
                month = month+1
        else:
            # not a leap year
            if dayofmonth == 29:
                dayofmonth = 1
                month = month+1
    else:
        if dayofmonth == 32:
            dayofmonth = 1
            month = month + 1

    if month == 13:
        month = 1
        year = year + 1

print(count)