import requests

def temperature(city_name):
	response = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&apikey=831de9f7679d4609a9c3feda3c7bd6e5'.format(city_name))
	data = response.json()
	prind(data)
	if 'main' in data:
		return round(d['main']['temp']) - 273
	else:
		return None