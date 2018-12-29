import json
import Tkinter
from Tkinter import *

window = Tk()

window.title('Register')

window.minsize(100, 100)
window.maxsize(300, 300)
window.geometry('300x300+500+500')

my_label = Label()
my_label['text'] = 'hi'
my_label['bg'] = 'pink'
my_label.pack()

my_label_2 = Label()
my_label_2['text'] = 'enter your name'
my_label_2.pack()

tf = Entry()
tf.pack()

my_label_3 = Label()
my_label_3['text'] = 'enter your password'
my_label_3.pack()

tf_2 = Entry()
tf_2.pack()


def savedata(login, password):
	file = open('/Users/macbookpro/Downloads/register.json', 'r')
	try:
		data = json.load(file)
	except ValueError:
		data = []
	file.close()
	data.append({'login': login, 'password': password})
	file = open('register.json', 'w')
	json.dump(data, file)
	file.close()

def click():
	print(tf)
	savedata(tf.get(), tf_2.get())

button = Button()
button['text'] = 'Complete'
button['command'] = click

button.pack()

window.mainloop()

savedata('log', 'pass')

