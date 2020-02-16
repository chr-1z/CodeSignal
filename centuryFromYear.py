def centuryFromYear(year):
    if year <= 100:
        return 1
    
    elif year % 100 == 0:
        return year/100
    
    else:
        return int(year/100)+1

print(centuryFromYear(1905))
