# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# * до часа: <m> мин <s> сек;
# * до суток: <h> час <m> мин <s> сек;
# * *до месяца, до года, больше года: по аналогии.
duration = 46812151702452

time_minutes = duration % 60
print('До минуты', time_minutes, 'сек')
time_hour = duration % 3600 // 60
print('До часа', time_hour, 'минут', time_minutes, 'секунд')
time_day = duration % 86400 // 3600
print('До суток', time_day, 'часов', time_hour, 'минут', time_minutes, 'секунд')
time_mounth = duration % 2629743 // 604800
print('До месяца', time_mounth, 'суток ', time_day, 'часов', time_hour, 'минут', time_minutes, 'секунд')
time_year = duration % 31556926 // 2629743
print('До года', time_year, ' месяца', time_mounth, 'суток ', time_day, 'часов', time_hour, 'минут', time_minutes,
      'секунд')
# Human-readable time 	Seconds
# 1 hour	                3600 seconds
# 1 day	                86400 seconds
# 1 week	                604800 seconds
# 1 month (30.44 days) 	2629743 seconds
# 1 year (365.24 days) 	31556926 seconds

# Второй вариант
print('Второй вариант')

duration = int(input('Введем любое число в секундах: '))
second = 60
hour = 3600
day = 86400
week = 604800
mounth = 2629743
year = 31556926

time_minutes = duration % second
print('До минуты', time_minutes, 'сек')
time_hour = duration % hour // second
print('До часа', time_hour, 'минут', time_minutes, 'секунд')
time_day = duration % day // hour
print('До суток', time_day, 'часов', time_hour, 'минут', time_minutes, 'секунд')
time_mounth = duration % mounth // week
print('До месяца', time_mounth, 'суток ', time_day, 'часов', time_hour, 'минут', time_minutes, 'секунд')
time_year = duration % year // mounth
print('До года', time_year, ' месяцев', time_mounth, 'суток ', time_day, 'часов', time_hour, 'минут', time_minutes,
      'секунд')
