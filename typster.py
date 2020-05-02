from tkinter import *
import time
import random

file = open('c_words.txt', 'r')
word_list = file.read().split('\n')

start = time.time()
char_count = 0
mistakes = 0
prev_len = 0

def reset():
	global start, char_count, mistakes, prev_len, passage, l
	start = time.time()
	char_count = 0
	mistakes = 0
	prev_len = 0
	passage, l = new_passage()
	e.configure(state=NORMAL)
	ps_var.set(' '.join(passage[0:3]))
	e.delete(0, 'end')

def my_tracer(a, b, c): # trace send 3 arguments to my_tracer

	global start, char_count, mistakes, prev_len

	new_text = inp.get()

	current_len = len(new_text)
	if current_len < prev_len:
		mistakes += 1

	prev_len = len(new_text)


	time_var.set('Time Passed: ' + str(round(time.time() - start)) + 's')

	if new_text == passage[0] + ' ':
		# calculating WPM
		char_count += len(passage[0]) + 1
		tm = time.time() - start
		wpm = round((char_count/5)/(tm/60))
		wpm_var.set('WPM: ' + str(wpm))

		# calculating accuracy
		acc = round(100 - ((mistakes/char_count)*100), 2)
		acc_var.set('Accuracy: ' + str(acc) + '%')

		passage.pop(0)
		ps_var.set(' '.join(passage[0:3]))
		e.delete(0, 'end')
		mistakes -= 1

		if len(passage) == 0:
			game_over()


def game_over():
	ps_var.set('GAME OVER!')
	e.configure(state=DISABLED)


root = Tk()
root.configure(background='black')
root.title('Typster')
root.geometry("600x240+700+100")


def new_passage():
	p = []
	for i in range(30):
		p.append(random.choice(word_list))
	l = len(' '.join(p))
	return p, l

passage, l = new_passage()
ps_var = StringVar()
ps_var.set(' '.join(passage[0:3]))

ps = Label(root, background = 'black', fg = 'gold', wraplength = 900, font = 'Helvetica, 34', textvariable = ps_var).pack()

inp = StringVar()
inp.trace('w', my_tracer)
e = Entry(root, font = 'Helvetica, 28', background = 'gold', highlightbackground = 'gold', fg = 'black', textvariable = inp)
e.pack()

wpm = 0
wpm_var = StringVar()
wpm_var.set('WPM: ' + str(wpm))
wpm_e = Label(root, textvariable = wpm_var, background = 'black', fg = 'gold', font = 'Helvetica, 18').pack()

time_a = 0
time_var = StringVar()
time_var.set('Time Passed: ' + str(time_a) + 's')
time_e = Label(root, textvariable = time_var, background = 'black', fg = 'gold', font = 'Helvetica, 18').pack()

acc = 0
acc_var = StringVar()
acc_var.set('Accuracy: ' + str(acc) + '%')
acc_e = Label(root, textvariable = acc_var, background = 'black', fg = 'gold', font = 'Helvetica, 18').pack()


reset_btn = Button(root, text = "RESET", highlightbackground = 'gold', command = reset, font = 'Helvetica, 18').pack()


root.mainloop()
