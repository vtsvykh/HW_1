from datetime import datetime
from datetime import timedelta

import ru_local as ru
print(ru.NUMBER)
n = int(input())

date = datetime(2009, 9, 25)
data_future = datetime(2009, 9, 25) + timedelta(n)

SPEED = 38_241                                       # Speed of miles per hour.
speed_1 = SPEED * 24                                 # Speed of miles per hour.
DISTANCE = 16_637_000_000
distance_miles = DISTANCE + (n*speed_1)              # Distance in miles.
distance_km = distance_miles * 1.6934                # Distance in kilometres.
distance_au = distance_miles/92_955_781.16           # Distance in au.

DELAY = 299_792_458
delay_1 = DELAY * 3.6                                # Delay in km per hour.
delay_wireless = distance_km/delay_1

print(n, ru.DISTANCE, distance_miles, ru.MILES)
print(n, ru.DISTANCE, distance_km, ru.KM)
print(n, ru.DISTANCE, distance_au, ru.AU)
print(n, ru.DELAY, round(delay_wireless, 1), ru.HOURS)
