digit = int(input('Type seconds: '))
days, digit = divmod(digit, 60 * 60 * 24)
hours, digit = divmod(digit, 60 * 60)
minutes, sec = divmod(digit, 60)
if 5 < days <21:
    day_str = 'дней'
elif str(days)[-1] == '1':
    day_str = 'день'
elif str(days)[-1] in '234':
    day_str = 'дня'
else:
    day_str = 'дней'
res = f'{days} {day_str}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(sec).zfill(2)}'
print(res)