import requests

def temp(city_name):
	response = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&APPID=00c9243d5b8cac9388e64ef2de7770f8".format(city_name))
	d = response.json()
	return int(d['main']['temp']) - 273
	print(d)


q = input()
t = temp(q)
print('The weather in city of {} is')
