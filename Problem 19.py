#You are given the following information, but you may prefer to do some research for yourself.

    #1 Jan 1900 was a Monday.

    #Thirty days has September,
    #April, June and November.
    #All the rest have thirty-one,
    #Saving February alone,
    #Which has twenty-eight, rain or shine.
    #And on leap years, twenty-nine.

    #A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
import time
start_time = time.clock()
days=[]
days_in_1900=[]
days_in_the_20th_century={}
for x in range(1):
    for y in range(1, 32):  # Januar
        days_in_1900.append(y)
    for y in range(1, 29):  # Februar
        days_in_1900.append(y)
    for y in range(1, 32):  # März
        days_in_1900.append(y)
    for y in range(1, 31):  # April
        days_in_1900.append(y)
    for y in range(1, 32):  # Mai
        days_in_1900.append(y)
    for y in range(1, 31):  # Juni
        days_in_1900.append(y)
    for y in range(1, 32):  # Juli
        days_in_1900.append(y)
    for y in range(1, 32):  # August
        days_in_1900.append(y)
    for y in range(1, 31):  # September
        days_in_1900.append(y)
    for y in range(1, 32):  # Oktober
        days_in_1900.append(y)
    for y in range(1, 31):  # November
        days_in_1900.append(y)
    for y in range(1, 32):  # Dezember
        days_in_1900.append(y)

z=1899
for x in range(1,102):
    z=z+1
    if x%4==0 and z%400==0:
        for y in range(1,32):#Januar
            days.append(y)
        for y in range(1,30):#Februar
            days.append(y)
        for y in range(1,32):#März
            days.append(y)
        for y in range(1,31):#April
            days.append(y)
        for y in range(1,32):#Mai
            days.append(y)
        for y in range(1,31):#Juni
            days.append(y)
        for y in range(1,32):#Juli
            days.append(y)
        for y in range(1,32):#August
            days.append(y)
        for y in range(1,31):#September
            days.append(y)
        for y in range(1,32):#Oktober
            days.append(y)
        for y in range(1,31):#November
            days.append(y)
        for y in range(1,32):#Dezember
            days.append(y)
    else:
        for y in range(1,32):#Januar
            days.append(y)
        for y in range(1,29):#Februar
            days.append(y)
        for y in range(1,32):#März
            days.append(y)
        for y in range(1,31):#April
            days.append(y)
        for y in range(1,32):#Mai
            days.append(y)
        for y in range(1,31):#Juni
            days.append(y)
        for y in range(1,32):#Juli
            days.append(y)
        for y in range(1,32):#August
            days.append(y)
        for y in range(1,31):#September
            days.append(y)
        for y in range(1,32):#Oktober
            days.append(y)
        for y in range(1,31):#November
            days.append(y)
        for y in range(1,32):#Dezember
            days.append(y)
for x in range(1,(len(days)+1)):
    days_in_the_20th_century[x]=0
n="Monday"
for x in days_in_the_20th_century:
    if n=="Monday":
        days_in_the_20th_century[x]="Monday"
        n="Tuesday"
    elif n=="Tuesday":
        days_in_the_20th_century[x]="Tuesday"
        n="Wednesday"
    elif n=="Wednesday":
        days_in_the_20th_century[x]="Wednesday"
        n="Thursday"
    elif n=="Thursday":
        days_in_the_20th_century[x]="Thursday"
        n="Friday"
    elif n=="Friday":
        days_in_the_20th_century[x]="Friday"
        n="Saturday"
    elif n=="Saturday":
        days_in_the_20th_century[x]="Saturday"
        n="Sunday"
    elif n=="Sunday":
        days_in_the_20th_century[x]="Sunday"
        n="Monday"

'Sundays that fell on the first of the month in 1900'
sundays_in_1900=0
for x,y in zip(days_in_the_20th_century,days_in_1900):
    if days_in_the_20th_century[x] == "Sunday" and y == 1:
        sundays_in_1900 = sundays_in_1900 + 1

'Sundays that fell on the first of the month between 1900 and 2000'
sundays=0
for x,y in zip(days_in_the_20th_century,days):
        if days_in_the_20th_century[x]=="Sunday" and y==1:
            sundays=sundays+1

print(sundays-sundays_in_1900)
print(time.clock() - start_time, "seconds")