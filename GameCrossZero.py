import Tkinter as tk


ZeroOrOne = 0
liftOfNormalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
def changeText(buttonVariable):
	global ZeroOrOne, button1, button2, button3, button4, button5, button6, button7, button8, button9
	localDeleteIndex = 0
	if (ZeroOrOne == 0):
		buttonVariable.set("X")
		ZeroOrOne = 1
		disableButtonsAfterSelection()
		decideWin(buttonVariable)
	else:
		buttonVariable.set("O")
		ZeroOrOne = 0
		disableButtonsAfterSelection()
		decideWin(buttonVariable)

def disableButtonsAfterSelection():
	for i in range(len(liftOfNormalState)):
			indexOfButton = liftOfNormalState[i]
			if (liftOfButtons[indexOfButton]['text'] != ""):
				liftOfButtons[indexOfButton].config(state=tk.DISABLED)
				localDeleteIndex = i
	del liftOfNormalState[localDeleteIndex]

def decideWin(buttonVariable): 
	if ( ((button_text1.get() != "") and (button_text1.get() == button_text2.get() == button_text3.get())) or 
			((button_text4.get() != "") and (button_text4.get() == button_text5.get() == button_text6.get())) or 
			((button_text7.get() != "") and (button_text7.get() == button_text8.get() == button_text9.get())) or
			((button_text1.get() != "") and (button_text1.get() == button_text4.get() == button_text7.get())) or
			((button_text2.get() != "") and (button_text2.get() == button_text5.get() == button_text8.get())) or
			((button_text3.get() != "") and (button_text3.get() == button_text6.get() == button_text9.get())) or
			((button_text1.get() != "") and (button_text1.get() == button_text5.get() == button_text9.get())) or
			((button_text3.get() != "") and (button_text3.get() == button_text5.get() == button_text7.get()))):
		r1 = tk.Tk()
		r1.title("Zero Cross Game")
		w = tk.Label(r1, text='Game winner is  ' + buttonVariable.get() +'', height=20, width=20) 
		w.pack() 
		r1.mainloop()


r = tk.Tk()
r.title("Zero Cross Game")


button_text1 = tk.StringVar()
button1 = tk.Button(r, textvariable=button_text1, command= lambda: changeText(button_text1), height=5, width=10)
button1.grid(row=0, column=0)

button_text2 = tk.StringVar()
button2 = tk.Button(r, textvariable=button_text2, command= lambda: changeText(button_text2), height=5, width=10)
button2.grid(row=0, column=1)

button_text3 = tk.StringVar()
button3 = tk.Button(r, textvariable=button_text3, command= lambda: changeText(button_text3), height=5, width=10)
button3.grid(row=0, column=2)

button_text4 = tk.StringVar()
button4 = tk.Button(r, textvariable=button_text4, command= lambda: changeText(button_text4), height=5, width=10)
button4.grid(row=1, column=0)

button_text5 = tk.StringVar()
button5 = tk.Button(r, textvariable=button_text5, command= lambda: changeText(button_text5), height=5, width=10)
button5.grid(row=1, column=1)

button_text6 = tk.StringVar()
button6 = tk.Button(r, textvariable=button_text6, command= lambda: changeText(button_text6), height=5, width=10)
button6.grid(row=1, column=2)

button_text7 = tk.StringVar()
button7 = tk.Button(r, textvariable=button_text7, command= lambda: changeText(button_text7), height=5, width=10)
button7.grid(row=2, column=0)

button_text8 = tk.StringVar()
button8 = tk.Button(r, textvariable=button_text8, command= lambda: changeText(button_text8), height=5, width=10)
button8.grid(row=2, column=1)


button_text9 = tk.StringVar()
button9 = tk.Button(r, textvariable=button_text9, command= lambda: changeText(button_text9), height=5, width=10)
button9.grid(row=2, column=2)

liftOfButtons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

r.mainloop()



