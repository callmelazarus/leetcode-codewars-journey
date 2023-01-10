import datetime 
print('-------PROGRESS---------')
HR_graduation = datetime.date(2022,11, 14)  
sixMonths = datetime.date(2023,5,14)

ninetydays_after_grad = HR_graduation + datetime.timedelta(days=90)
onetwentydays_later = HR_graduation + datetime.timedelta(days=120)

# last_day_2022 = datetime.date(2022, 12, 31)
today = datetime.date.today()

days_before_90 = (ninetydays_after_grad-today).days

print('HR graduation: ',HR_graduation, 'which is (',(today-HR_graduation).days, ') days ago')


# print(f'Days until end of year {before_end_year} days')
print(f'90 days after graduation is {ninetydays_after_grad}, which is \
({days_before_90}) days from today')

print(f'120 days after graduation: ', onetwentydays_later)
print(f'6 months from graduation is May 14 which is (', (sixMonths-today).days, ') from today')

# LC problems per day
rate_LC = 1

# how many unique LC problems have you solved?
# as of Dec 30 - 50
solved_LC = 56

# ranking as of 12/26/2022 - 1004934
# ranking as of 12/30/2022 - 932310
rank_prev = 932310

# ranking as of 12/30/2022
rank = 862373

goal = 150
print('---------rate check------------')

rate_required = (goal - solved_LC)//(days_before_90)
print('rate required to meet my goal:', rate_required)


print(f'LC completed within 90 days of graduation: {solved_LC + rate_LC*(days_before_90 - days_before_90//7)}, \
at a rate of {rate_LC} LC problems per day')

print(f'Current rank is {rank}, roughly top {rank/5000000*100}%')
