''' how many sundays fell on the first of the month in the twentieth century? '''

''' note: 1 jan 1901 is a sunday '''

months = ['JAN', 'FEB', 'MAR',
          'APR' ,'MAY', 'JUN',
          'JUL', 'AUG', 'SEP', 
          'OCT', 'NOV', 'DEC']
                    
thirtyDays = {'APR','JUN', 'SEP', 'NOV'}

def isLeap(year):
    if year % 4 == 0 and year != 2000:
        return True
    else:
        return False
        
def getMonthLength(month):
    if month in thirtyDays:
        return 30
    elif month == 'FEB' and isLeap(year):
        return 29
    elif month == 'FEB':
        return 28
    else:
        return 31

year = 1900
day = 0
sundays = []
while year < 2001:
    for month in months:
        if day % 7 == 0 and year > 1900:
            sundays.append('{0}, {1}'.format(month, year))
        day += getMonthLength(month)
        print(day)
    year += 1
print(sundays)
print(len(sundays))