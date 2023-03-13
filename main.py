from datetime import datetime
from datetime import timedelta

import ru_local as ru
print(ru.NUMBER)
n = int(input())

date = datetime(2009, 9, 25)
data_future = datetime(2009, 9, 25) + timedelta(n)   # Дата спустя n дней.

SPEED = 38_241                                       # Скорость миль в час.
speed_1 = SPEED * 24                                 # Скорость миль в день.
DISTANCE = 16_637_000_000                            # Расстояние зонда от солнца 25 сентября 2009 года.
distance_miles = DISTANCE + (n*speed_1)              # Расстоние от солнца спустя n дней в милях.
distance_km = distance_miles * 1.6934                # Расстоние от солнца спустя n дней в километрах.
distance_au = distance_miles/92_955_781.16             # Расстоние от солнца астрономических единицах.

DELAY = 299_792_458                                  # Задержка в м/с.
delay_1 = DELAY * 3.6                                # Задержка км/ч.
delay_wireless = distance_km/delay_1                 # Задержка беспроводной связи спустя n дней.

print(n, ru.DISTANCE, distance_miles, ru.MILES)
print(n, ru.DISTANCE, distance_km, ru.KM)
print(n, ru.DISTANCE, distance_au, ru.AU)
print(n, ru.DELAY, round(delay_wireless, 1), ru.HOURS)
