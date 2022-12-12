import datetime 

HR_graduation = datetime.date(2022,11, 14)  

ninetydays_after_grad = HR_graduation + datetime.timedelta(days=90)

last_day_2022 = datetime.date(2022, 12, 31)
today = datetime.date.today()

days_before_90 = (ninetydays_after_grad-today).days

print('HR graduation: ',HR_graduation)
print('90 days from grad: ', ninetydays_after_grad)

before_end_year = (last_day_2022-today).days

print(f'Days until end of year {before_end_year} days')
print(f'90 days after graduation is {ninetydays_after_grad}, which is \
({days_before_90}) days from today')

# LC problems per day
rate_LC = 3

# how many unique LC problems have you solved?
# as of Dec 10
solved_LC = 28

goal = 150
print('---------rate check------------')

rate_required = (goal - solved_LC)//(days_before_90)
print('rate required to meet my goal:', rate_required)

print(f'LC completed by end of the year: {solved_LC + rate_LC*(before_end_year - before_end_year//7)}, \
at a rate of {rate_LC} LC problems per day')

print(f'LC completed within 90 days of graduation: {solved_LC + rate_LC*(days_before_90 - days_before_90//7)}, \
at a rate of {rate_LC} LC problems per day')

