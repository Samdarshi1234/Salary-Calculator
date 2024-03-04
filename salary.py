import tkinter as tk
from tkinter import ttk
from tkinter import *
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from customtkinter import *
import win32com.client
VirtualUI = win32com.client.Dispatch("Thinfinity.VirtualUI")

#functions

def month_value():
    month_val = month_name.get()
    month_amtt = month_amt_1.get()
    absent_days = month_abt_1.get()

    if(month_val=='January' or month_val=='March' or month_val=='May' or month_val=='July' or month_val=='August' or month_val=='October' or month_val=='December'):
        day_amt_1= month_amtt//31
        rounded_day_amt_1 = round(day_amt_1,2)
        absent_amt = absent_days*rounded_day_amt_1
        given_amount = month_amtt - absent_amt
        my_amount.set(value=given_amount)


    elif(month_val=="April" or month_val=="June" or month_val=="September" or month_val=="November"):
        day_amt_2 = month_amtt//30
        rounded_day_amt_2 = round(day_amt_2,2)
        absent_amt = absent_days*rounded_day_amt_2
        given_amount = month_amtt - absent_amt
        my_amount.set(value=given_amount)

    elif(month_val=="February"):
        day_amt_3 = month_amtt//29
        rounded_day_amt_3 = round(day_amt_3,2)
        absent_amt = absent_days*rounded_day_amt_3
        given_amount = month_amtt - absent_amt
        my_amount.set(value=given_amount)

#window

window = ttk.Window(themename="flatly")
window.geometry("722x600")
window.title("Salary Calculator")

#image

header_frame = Frame(window, width=722, height=87)
header_frame.pack()
img_1 = ImageTk.PhotoImage(Image.open("image_1.png"))
img_1_l = ttk.Label(header_frame,image=img_1)
img_1_l.pack()

#Month Name
month_frame = Frame(window, width=722, height=100)
month_frame.pack(pady=20)
entry_1_label = ttk.Label(month_frame, text="Enter the name of the Month : ", font="Roboto 15 bold")
entry_1_label.pack(side="left")
month_name = ttk.StringVar()
month_name.set("January")
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
Month_Combo = ttk.Combobox(master=month_frame, values=months, font="Roboto 15 bold", textvariable=month_name)
Month_Combo.pack()


#Monthly Amount to be given

month_amt = Frame(window, width=722,height=100)
month_amt.pack()
entry_2_label = ttk.Label(month_amt, text="Enter the Monthly Amount : ", font="Roboto 15 bold")
entry_2_label.pack(side="left")
month_amt_1 = ttk.IntVar()
entry_2 = ttk.Entry(month_amt, width=30, textvariable=month_amt_1)
entry_2.pack(side="left",pady= 20, padx=40)


#Absent days

month_abt = Frame(window, width=722,height=100)
month_abt.pack()
entry_3_label = ttk.Label(month_abt, text="Enter the No of Absent Days : ", font="Roboto 15 bold")
entry_3_label.pack(side="left")
month_abt_1 = ttk.IntVar()
entry_3 = ttk.Entry(month_abt, width=30, textvariable=month_abt_1)
entry_3.pack(side="left",pady= 20, padx=40)

#Calculate Button

button_frame = Frame(window, width=722, height=87)
button_frame.pack(pady=20)
button_1 = ttk.Button(button_frame, text="Calculate Salary", command=month_value)
button_1.pack()

#Output Frame

output_frame = Frame(window,width=722, height=200)
output_frame.pack()
entry_3_label = ttk.Label(output_frame, text="The Final Salary is : ", font="Roboto 15 bold")
entry_3_label.pack(side="left")
my_amount = ttk.StringVar()
entry_3_label = ttk.Label(output_frame, textvariable=my_amount ,font="Roboto 15 bold")
entry_3_label.pack(side="left")


#Author Credit

author_frame = Frame(window,width=722,height=100)
author_frame.pack()
label_2 = ttk.Label(author_frame, text="Made by Samdarshi", font="Algerian 13 bold italic underline")
label_2.pack(pady=50)

#run
VirtualUI.start(60)
window.mainloop()