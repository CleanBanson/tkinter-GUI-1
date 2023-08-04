



#Author: Matt Harris
#Date: Aug 3, 2023
#Project Name: MyFirstGUItkinter


#import tkinter which comes automaticlly with python
import tkinter as tk



#This creates a basic window. The variable does not need to be named window. That is just what I chose.
window = tk.Tk()



#This specifies the dimensions of the window.
window.geometry("500x500")
#This sets the title
window.title("My First GUI")



#This will add some text/label to your window.
#The padx and pady elements create space between the edged of the window and the label.
#label.pack() is us calling the variable into existance
label = tk.Label(window, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)




#This is how you add a text box.
#Usually a textbox is so a user can enter text.
#textbox.pack() is us calling the variable into existance
textbox = tk.Text(window, height=3, font=('Arial', 16))
textbox.pack(padx=10, pady=10)


#Entry will give you a one line entry field.
myentry = tk.Entry(window)
myentry.pack()



#This creates a button but it has not functionality yet.
button = tk.Button(window, text="Click Me!", font=('Arial', 18))
button.pack(padx=10, pady=10)


#This is a way to create a grid of buttons
buttonframe = tk.Frame(window)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky="W, E")

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky="W, E")

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky="W, E")

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky="W, E")

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky="W, E")

btn6 = tk.Button(buttonframe, text="6", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky="W, E")

buttonframe.pack(fill='x')




#Another button you place manually/specifically
anotherbtn = tk.Button(window, text="TEST")
anotherbtn.place(x=200, y=375, height=100, width=100)











#I think this goes at the bottom of your code
window.mainloop()


















