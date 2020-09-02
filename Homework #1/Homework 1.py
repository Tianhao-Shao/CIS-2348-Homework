# Tianhao Shao
# 1781421

print('Birthday Calculator')
print('Current day')

current_month = int(input('Enter the current month(by number): '))
current_day = int(input('Enter the current day: '))
current_year = int(input('Enter the current year: '))

print('Month: ' + str(current_month))
print('Day: ' + str(current_day))
print('Year: ' + str(current_year))

print('Birthday')

user_birthmonth = int(input('Enter your birth month (by number):'))
user_birthday = int(input('Enter your birth day: '))
user_birthyear = int(input('Enter your birth year: '))

print('Month: ' + str(user_birthmonth))
print('Day: ' + str(user_birthday))
print('Year: ' + str(user_birthyear))

if(
        current_day == user_birthday and current_month == user_birthmonth
):
    print('Happy Birthday!')
else:
    print('You are ' + str(current_year - user_birthyear) + ' years old.')
