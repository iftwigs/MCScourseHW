import telepot

token = 'AAEdnoGFrialvnrRGC0U6Q46ONj83IJuHv4'

bot = telepot.Bot(token)

#bot.message(123423124, "hello")

last_update = 0

while True:
	updates = bot.getUpdates(offset = last_update + 1)
	for update in updates:
		print(update['message']['text'])
		if update['update_id'] > last_update:
			last_update = update['update_id']



