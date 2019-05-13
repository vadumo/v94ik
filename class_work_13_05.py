import pyowm

owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
a = input()
observation = owm.weather_at_place(a)
w = observation.get_weather()
print(w.get_temperature('celsius'), w.get_humidity(), w.get_wind())                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)

# вгадай число

import random
rand_num = random.randint(1, 100)
you_choice = int(input("Вгадай число = "))
while you_choice != rand_num:
    if you_choice == rand_num:
        print('Ти вгадав, вітаю!')
    elif you_choice > rand_num:
        print('Твоє число завалике.')
        you_choice = int(input('Попробуй ще раз = '))
    elif you_choice < rand_num:
        print('Твоє число замале')
        you_choice = int(input('Попробуй ще раз = '))
print('Ти вгадав, вітаю!')

import math

# площа прямокутника
a = int(input('Перша сторона прямокутника = '))
b = int(input('Друга сторона прямокутника = '))
print('Площа прямокутника = ', a * b)

# площа трикутника 0.5 *a *h
a = int(input('Сторона трикутника = '))
h = int(input('Висота трикутника = '))
plosha_truk = a * h
plosha_truk = math.pow(plosha_truk, 0.5)
print('Площа трикутника = ', plosha_truk)

# площа кола pi*r**2
r = int(input('Пів периметр = '))
pi = math.pi
r = r**2
print('Площа кола = ', pi*r)
