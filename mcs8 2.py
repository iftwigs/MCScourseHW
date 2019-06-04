
import telepot
import requests

def temperature(city_name):
	response = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&apikey=831de9f7679d4609a9c3feda3c7bd6e5'.format(city_name))
	data = response.json()
	print(data)
	if 'main' in data:
		return round(data['main']['temp']) - 273
	else:
		return None

token = 'your token here'
print('Start')

bot = telepot.Bot(token)

def reply(text, chat_id):
	if '/weather ' in text:
		city_name = text[9:]
		t = temperature(city_name)
		bot.sendMessage(chat_id, 'Temperature in the city {} is {} degrees'.format(city_name, t))
	else:
		bot.sendMessage(chat_id, text)

print('Bot is ready')

update_id = 0

while True:
	updates = bot.getUpdates(offset = update_id + 1)
	for update in updates:
		if update['update_id'] > update_id:
			update_id = update['update_id']
			reply(update['message']['text'], update['message']['chat']['id'])
