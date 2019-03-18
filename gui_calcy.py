from tkinter import *
gui = Tk()
gui.title("Simple Calculator")
gui.geometry("240x125")
expression = ""

# ******************************** Backend *************************************

# ****** For press function ******
def press(num):
    global expression
    expression+=str(num)
    equation.set(expression)

#****** For equalpress function ******

def equalpress():
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression=""

#****** For clearpress function ******

def clearpress():
    global expression
    expression=""
    equation.set("")
    
# ******************************** Display *************************************

equation = StringVar()
expression_field = Entry(gui, textvariable = equation, width=39)
expression_field.configure(background="silver")
expression_field.grid(columnspan = 7)
expression_field.focus()
equation.set("Enter the value")
button1 = Button(gui, text="1", height=1, width=7, command=lambda:press(1), activebackground="silver", activeforeground='red', activefont='bold')
button1.grid(row = 2, column=0)
button2 = Button(gui, text="2", height=1, width=7, command=lambda:press(2), activebackground="silver")
button2.grid(row = 2, column=1)
button3 = Button(gui, text="3", height=1, width=7, command=lambda:press(3), activebackground="silver")
button3.grid(row = 2, column=2)
plus = Button(gui, text="+", height=1, width=7, command=lambda:press("+"), activebackground="silver")
plus.grid(row = 2, column=3)
button4 = Button(gui, text="4", height=1, width=7, command=lambda:press(4), activebackground="silver")
button4.grid(row = 3, column=0)
button5 = Button(gui, text="5", height=1, width=7, command=lambda:press(5), activebackground="silver")
button5.grid(row = 3, column=1)
button6 = Button(gui, text="6", height=1, width=7, command=lambda:press(6), activebackground="silver")
button6.grid(row = 3, column=2)
minus = Button(gui, text="-", height=1, width=7, command=lambda:press("-"), activebackground="silver")
minus.grid(row = 3, column=3)
button7 = Button(gui, text="7", height=1, width=7, command=lambda:press(7), activebackground="silver")
button7.grid(row = 4, column=0)
button8 = Button(gui, text="8", height=1, width=7, command=lambda:press(8), activebackground="silver")
button8.grid(row = 4, column=1)
button9 = Button(gui, text="9", height=1, width=7, command=lambda:press(9), activebackground="silver")
button9.grid(row = 4, column=2)
multiply = Button(gui, text="*", height=1, width=7, command=lambda:press("*"), activebackground="silver")
multiply.grid(row = 4, column=3)
button0 = Button(gui, text="0", height=1, width=7, command=lambda:press(0), activebackground="silver")
button0.grid(row = 5, column=0)
clear = Button(gui, text="clear", height=1, width=7, command=clearpress, activebackground="silver")
clear.grid(row = 5, column=1)
equal = Button(gui, text="=", height=1, width=7, command=equalpress, activebackground="silver")
equal.grid(row = 5, column=2)
divide = Button(gui, text="/", height=1, width=7, command=lambda:press("/"), activebackground="silver")
divide.grid(row = 5, column=3)

gui.mainloop()
