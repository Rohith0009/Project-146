from tkinter import *

import ctypes

# Compatibility Settings
ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()

root.title("Fibonacci Sum")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

required_digits_input = Entry(root)
Fibonacci_Series = Label(root, text="Fibonacci Series:")
Fibonacci_Sum = Label(root, text="Fibonacci Sum:")


def fibonacci():
    global num_1,num_2,sum,total_sum, generated_num, new_both
    num_1,num_2,sum,total_sum, generated_num, new_both = 0,1,0,0,2,0
    Fibonacci_Series['text'] += f" {num_1} {num_2}"
    required_digits = required_digits_input.get()
    while generated_num <= int(required_digits):
        new_both = num_1 + num_2
        num_1,num_2 = num_2,new_both
        Fibonacci_Series["text"] += f" {str(new_both)}"
        generated_num += 1
        total_sum += new_both
    Fibonacci_Sum['text'] += f" {str(total_sum+1)}"

show_btn = Button(root, text="Show Fibonacci digits", command=fibonacci)
required_digits_input.pack()
show_btn.pack()
Fibonacci_Series.pack()
Fibonacci_Sum.pack()


root.mainloop()