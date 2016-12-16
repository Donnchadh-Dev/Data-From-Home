import pyowm
import pprint

# OWM API Key
owm = pyowm.OWM('API-KEY')

# OWM Pro Subscription
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in Carlow (Ireland)
observation = owm.weather_at_place('Carlow,Ire')
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>
# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}#

print (w.get_temperature('celsius'))

print

forecast = owm.daily_forecast("Carlow,Ire")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)

print (forecast.will_be_sunny_at(tomorrow))
print (forecast.will_be_rainy_at(tomorrow))
print (forecast.will_be_cloudy_at(tomorrow))

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
#observation_list = owm.weather_around_coords(-22.57, -43.12)
