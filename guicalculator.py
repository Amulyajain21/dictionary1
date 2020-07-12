'''from tkinter import *
expression=""

def raise_frame(frame):
    frame.tkraise()
def press(num): 
    # point out the global expression variable 
    global expression 
  
    # concatenation of string 
    expression = expression + str(num) 
  
    # update the expression by using set method 
    equation.set(expression) 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
  
    # Put that code inside the try block 
    # which may generate the error 
    try: 
  
        global expression 
  
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
  
        equation.set(total) 
  
        # initialze the expression variable 
        # by empty string 
        expression = "" 
     
    except: 
  
        equation.set(" error ") 
        expression = "" 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
  
  
root = Tk()
root.geometry("1000x1000")
root.configure(background="grey")

f1 = Frame(root, width=1000, height=1000)
f2 = Frame(root, width=1000, height=1000)
f3 = Frame(root, width=1000, height=1000)
#f4 = Frame(root)

for frame in (f1, f2,f3):
    frame.grid(row=0, column=0, sticky='news')

Label(f1, text='Calculator').pack()
Button(f1, text='General Calculator', command=lambda:raise_frame(f2)).pack()
Button(f1, text='Scientific Calculator', command=lambda:raise_frame(f3)).pack()

Label(f2, text='General Calculator').pack()
Button(f2, text='1', command=done).pack(side='left')
Button(f2, text='2', command=done).pack(side='left')
Button(f2, text='3', command=done).pack(side='left')
Button(f2, text='4', command=done).pack(side='left')
Button(f2, text='5', command=done).pack(side='bottom')
Button(f2, text='6', command=done).pack(side='bottom')
Button(f2, text='7', command=done).pack(side='bottom')
Button(f2, text='8', command=done).pack(side='bottom')
Button(f2, text='9', command=done).pack(side='bottom')
Button(f2, text='0', command=done).pack(side='bottom')
button1 = Button(root, text=' 1 ', fg='black', bg='red', 
                     command=lambda: press(1):raise_frame(f2), height=1, width=7)
button1.grid(row=2, column=0) 

button2 = Button(root, text=' 2 ', fg='black', bg='red', 
                     command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1) 
  
button3 = Button(root, text=' 3 ', fg='black', bg='red', 
                     command=lambda: press(3), height=1, width=7) 
button3.grid(row=2, column=2) 
  
button4 = Button(root, text=' 4 ', fg='black', bg='red', 
                     command=lambda: press(4), height=1, width=7) 
button4.grid(row=3, column=0) 
  
button5 = Button(root, text=' 5 ', fg='black', bg='red', 
                     command=lambda: press(5), height=1, width=7) 
button5.grid(row=3, column=1) 
  
button6 = Button(root, text=' 6 ', fg='black', bg='red', 
                     command=lambda: press(6), height=1, width=7) 
button6.grid(row=3, column=2) 
  
button7 = Button(root, text=' 7 ', fg='black', bg='red', 
                     command=lambda: press(7), height=1, width=7) 
button7.grid(row=4, column=0) 
  
button8 = Button(root, text=' 8 ', fg='black', bg='red', 
                     command=lambda: press(8), height=1, width=7) 
button8.grid(row=4, column=1) 
  
button9 = Button(root, text=' 9 ', fg='black', bg='red', 
                     command=lambda: press(9), height=1, width=7) 
button9.grid(row=4, column=2) 
  
button0 = Button(root, text=' 0 ', fg='black', bg='red', 
                     command=lambda: press(0), height=1, width=7) 
button0.grid(row=5, column=0) 
  
plus = Button(root, text=' + ', fg='black', bg='red', 
                  command=lambda: press("+"), height=1, width=7) 
plus.grid(row=2, column=3) 
  
minus = Button(root, text=' - ', fg='black', bg='red', 
                   command=lambda: press("-"), height=1, width=7) 
minus.grid(row=3, column=3) 
  
multiply = Button(root, text=' * ', fg='black', bg='red', 
                      command=lambda: press("*"), height=1, width=7) 
multiply.grid(row=4, column=3) 
  
divide = Button(root, text=' / ', fg='black', bg='red', 
                    command=lambda: press("/"), height=1, width=7) 
divide.grid(row=5, column=3) 
  
equal = Button(root, text=' = ', fg='black', bg='red', 
                   command=equalpress, height=1, width=7) 
equal.grid(row=5, column=2) 
  
clear = Button(root, text='Clear', fg='black', bg='red', 
                   command=clear, height=1, width=7) 
clear.grid(row=5, column='1') 
  
Button(f2, text='Calculator', command=lambda:raise_frame(f1)).pack()


Label(f3, text='Scientific Calculator').pack(side='left')
Button(f3, text='Calculator', command=lambda:raise_frame(f1)).pack(side='left')

Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()'''

import tkinter as tk               
from tkinter import font as tkfont

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Calculator")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Calculator", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="General Calculator",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Scientific Calculator",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="General calculator", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        root = tk.Tk()
    expression = "" 
  
  
# Function to update expressiom 
# in the text entry box 
    def press(num):
        global expression 
  
    # concatenation of string 
        expression = expression + str(num) 
  
    # update the expression by using set method 
        equation.set(expression) 
  
  
# Function to evaluate the final expression 
    def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
  
    # Put that code inside the try block 
    # which may generate the error 
        try:
            global expression 
  
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
            total = str(eval(expression)) 
  
            equation.set(total) 
  
        # initialze the expression variable 
        # by empty string 
            expression = "" 
    
    # if error is generate then handle 
    # by the except block 
        except:
            equation.set(" error ") 
            expression = "" 
  
  
# Function to clear the contents 
# of text entry box 
    def clear():
        global expression 
        expression = "" 
        equation.set("") 
  
  
    # set the background colour of GUI window 
        root.configure(background="light green") 
  
    # set the title of GUI window 
        root.title("Simple Calculator") 
  
    # set the configuration of GUI window 
        root.geometry("265x125") 
  
    # StringVar() is the variable class 
    # we create an instance of this class 
        equation = StringVar() 
  
    # create the text entry box for 
    # showing the expression . 
        expression_field = Entry(gui, textvariable=equation) 
  
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
        expression_field.grid(columnspan=4, ipadx=70) 
  
        equation.set('enter your expression') 
  
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
        button1 = Button(root, text=' 1 ', fg='black', bg='red', 
                     command=lambda: press(1), height=1, width=7) 
        button1.grid(row=2, column=0) 
  
        button2 = Button(root, text=' 2 ', fg='black', bg='red', 
                     command=lambda: press(2), height=1, width=7) 
        button2.grid(row=2, column=1) 
  
        button3 = Button(root, text=' 3 ', fg='black', bg='red', 
                     command=lambda: press(3), height=1, width=7) 
        button3.grid(row=2, column=2) 
  
        button4 = Button(root, text=' 4 ', fg='black', bg='red', 
                     command=lambda: press(4), height=1, width=7) 
        button4.grid(row=3, column=0) 
  
        button5 = Button(root, text=' 5 ', fg='black', bg='red', 
                     command=lambda: press(5), height=1, width=7) 
        button5.grid(row=3, column=1) 
  
        button6 = Button(root, text=' 6 ', fg='black', bg='red', 
                     command=lambda: press(6), height=1, width=7) 
        button6.grid(row=3, column=2) 
  
        button7 = Button(root, text=' 7 ', fg='black', bg='red', 
                     command=lambda: press(7), height=1, width=7) 
        button7.grid(row=4, column=0) 
  
        button8 = Button(root, text=' 8 ', fg='black', bg='red', 
                     command=lambda: press(8), height=1, width=7) 
        button8.grid(row=4, column=1) 
  
        button9 = Button(gui, text=' 9 ', fg='black', bg='red', 
                     command=lambda: press(9), height=1, width=7) 
        button9.grid(row=4, column=2) 
  
        button0 = Button(root, text=' 0 ', fg='black', bg='red', 
                     command=lambda: press(0), height=1, width=7) 
        button0.grid(row=5, column=0) 
  
        plus = Button(root, text=' + ', fg='black', bg='red', 
                  command=lambda: press("+"), height=1, width=7) 
        plus.grid(row=2, column=3) 
  
        minus = Button(root, text=' - ', fg='black', bg='red', 
                   command=lambda: press("-"), height=1, width=7) 
        minus.grid(row=3, column=3) 
  
        multiply = Button(root, text=' * ', fg='black', bg='red', 
                      command=lambda: press("*"), height=1, width=7) 
        multiply.grid(row=4, column=3) 
  
        divide = Button(root, text=' / ', fg='black', bg='red', 
                    command=lambda: press("/"), height=1, width=7) 
        divide.grid(row=5, column=3) 
  
        equal = Button(root, text=' = ', fg='black', bg='red', 
                   command=equalpress, height=1, width=7) 
        equal.grid(row=5, column=2) 
  
        clear = Button(root, text='Clear', fg='black', bg='red', 
                   command=clear, height=1, width=7) 
        clear.grid(row=5, column='1') 
  
    # start the GUI 
       
        button = tk.Button(self, text="Calculator",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Scientific Calculator", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Calculator",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
