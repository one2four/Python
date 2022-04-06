# coding:utf-8

year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))
sum = 0
# months = (0,31,59,90,120,151,181,212,243,273,304,334)
# if 0 < month <= 12:
#     sum = months[month - 1]
# else:
#     print ('data error')
# sum += day
# leap = 0
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and (month > 2):
#     sum += 1
# print ('it is the %dth day.' % sum)
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print(months[1])
if month == 1:
    if 0 < day < months[month-1]:
        sum = day
        print(sum)
    else:
        print("day errot")
elif 1 < month <= 12:
    if 0 < day < months[month-1]:
        for i in range(0, month-1):
            sum = sum + months[i]
        # print(sum)
            th = sum + day
            if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))) and month > 2:
                th = th + 1
                print('today is %dth day' % th)
    else:
        print("day errot")
else:
    print("mouth error")
