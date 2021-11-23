from tkinter import *

def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def clear(event):
    global equation_text

    equation_text = ""

    equation_label.set(equation_text)

def equals(event):
    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_text = ""

        equation_label.set("Syntax Error")

    except ZeroDivisionError:

        equation_text = ""

        equation_label.set("0 Error")

window = Tk()
window.title("Calculator")
window.geometry("380x520")

window.iconbitmap("C:\\Users\\Teepe\\Downloads\\Calculator image.ico")

equation_text = ""
equation_label = StringVar()

display = Label(window, textvariable=equation_label, font=("Consolas",35))
display.pack()

frame = Frame(window)
frame.pack()

button7 = Button(frame, text=7, width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press(7))
button7.grid(row=0,column=0)
button8 = Button(frame, text=8, width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press(8))
button8.grid(row=0,column=1)
button9 = Button(frame, text=9, width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press(9))
button9.grid(row=0,column=2)
buttonDel = Button(frame, text="Del", width=9, height=4, bg="black", fg="white", font=("Consolas"),command=clear)
buttonDel.grid(row=3,column=2)
button4 = Button(frame, text=4, width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press(4))
button4.grid(row=1,column=0)
button5 = Button(frame, text=5, width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press(5))
button5.grid(row=1,column=1)
button6 = Button(frame, text=6, width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press(6))
button6.grid(row=1,column=2)
buttonDiv = Button(frame, text="/", width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press("/"))
buttonDiv.grid(row=1,column=3)
button1 = Button(frame, text=1, width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press(1))
button1.grid(row=2,column=0)
button2 = Button(frame, text=2, width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press(2))
button2.grid(row=2,column=1)
button3 = Button(frame, text=3, width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press(3))
button3.grid(row=2,column=2)
buttonMul = Button(frame, text="*", width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press("*"))
buttonMul.grid(row=2,column=3)
buttonDec = Button(frame, text=".", width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press("."))
buttonDec.grid(row=3,column=0)
button0 = Button(frame, text=0, width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press(0))
button0.grid(row=3,column=1)
buttonMin = Button(frame, text="-", width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press("-"))
buttonMin.grid(row=3,column=3)
buttonPlus = Button(frame, text="+", width=9, height=4, bg="black", fg="white", font=("Consolas"),command=lambda: button_press("+"))
buttonPlus.grid(row=0,column=3)
buttonEquals = Button(window, text="=", width=15, height=4, bg="black", fg="white", font=("Consolas"),command=equals)
buttonEquals.pack()
window.bind("<Return>",equals)
window.bind("<Delete>",clear)
window.bind("<BackSpace>",clear)

window.resizable(False, False)
window.mainloop()