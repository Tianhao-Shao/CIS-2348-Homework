print('Birthday Calculator\n')
print('\tCurrent day')
current_day = int(input('Enter the current day: '))
current_month = int(input('Enter the current month(by number): '))
current_year = int(input('Enter the current year: '))
print('\tBirthday')
user_birthday = int(input('Enter your birth day: '))
user_birthmonth = int(input('Enter your birth month (by number):'))
user_birthyear = int(input('Enter your birth year: '))

if(current_day == user_birthday and current_month == user_birthmonth ):
    print('\nHappy Birthday!')
else:
    print('\nYou are', current_year - user_birthyear, 'years old.')
