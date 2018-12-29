import Tkinter
from Tkinter import *

window = Tk()

window.title('Hello')

window.minsize(100, 100)
window.maxsize(300, 300)

window.geometry('300x300+500+500')

my_label = Label(window)

my_label['text'] = '0'

my_label['bg'] = 'red'

button = Button()

button['text'] = 'click!'

#my_label.pack(side = 'left')
#button.place({'x':0, 'y':0, 'width':50, 'height': 30})

button.pack()

def click():
	current_number = int(my_label['text'])
	my_label['text'] = str(current_number + 1)

button['command'] = click

tf = Entry()

#tf.get()

tf.pack()

def click2():
	s = tf.get()
	my_label['text'] = s

button['command'] = click2
#my_label.place({'x': 125, 'y': 125, 'width': 50, 'height': 50})

my_label.pack()

window.mainloop()

