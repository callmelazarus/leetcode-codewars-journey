import datetime 

HR_graduation = datetime.date(2022,11, 14)  

ninetydays_after_grad = HR_graduation + datetime.timedelta(days=90)

last_day_2022 = datetime.date(2022, 12, 31)
today = datetime.date.today()

days_before_90 = (ninetydays_after_grad-today).days

print(HR_graduation)
print(ninetydays_after_grad)

before_end_year = (last_day_2022-today).days

print(f'Days until end of year {before_end_year} days')
print(f'90 days after graduation is {ninetydays_after_grad}, which is \
{days_before_90} days from today')

# LC problems per day
rate_LC = 5

print(f'LC completed by end of the year: {rate_LC*(before_end_year - before_end_year//7)}, \
at a rate of {rate_LC} LC problems per day')

print(f'LC completed within 90 days of graduation: {14 + rate_LC*(days_before_90 - days_before_90//7)}, \
at a rate of {rate_LC} LC problems per day')