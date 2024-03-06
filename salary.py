import tkinter as tk
from tkinter import ttk
from tkinter import *
import ttkbootstrap as ttk
from customtkinter import *
from tkinter import *
from datetime import date
from datetime import datetime
from PIL import Image, ImageTk


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

    elif(month_val=="February") and (year % 4 == 0) and (year % 100 != 0):
        day_amt_3 = month_amtt//29
        rounded_day_amt_3 = round(day_amt_3,2)
        absent_amt = absent_days*rounded_day_amt_3
        given_amount = month_amtt - absent_amt
        my_amount.set(value=given_amount)
    elif(month_val == "February") and (year%400 == 0) and (year%100 == 0):
        day_amt_3 = month_amtt//29
        rounded_day_amt_3 = round(day_amt_3,2)
        absent_amt = absent_days*rounded_day_amt_3
        given_amount = month_amtt - absent_amt
        my_amount.set(value=given_amount)
    elif(month_val == "February"):
        day_amt_3 = month_amtt//28
        rounded_day_amt_3 = round(day_amt_3,2)
        absent_amt = absent_days*rounded_day_amt_3
        given_amount = month_amtt - absent_amt
        my_amount.set(value=given_amount)
def emplo_name():
    a = em_name.get()
    emplo_name_1.set(a)

#window

window = ttk.Window(themename="flatly")
window.geometry("1366x768")
window.title("Salary Calculator")


#image

header_frame = Frame(window, width=1366, height=110)
header_frame.pack()
img_1 = ImageTk.PhotoImage(Image.open("image_1.png"))
img_1_l = ttk.Label(header_frame,image=img_1,)
img_1_l.pack()

#Date Frame

#date and time

now = date.today()
dt_string = now.strftime("%d/%m/%Y")
date_frame = Frame(window, width=722, height=100)
date_frame.pack()
date = ttk.Label(date_frame, text= "Today's Date is :", font="Roboto 13 bold")
date.pack(pady=20, side="left")
time = ttk.StringVar(value=dt_string)
time_entity = ttk.Label(date_frame, textvariable=time, font="Roboto 13 bold")
time_entity.pack(side="left")
year = datetime.today().year
print(year)

#tabs

notebook = ttk.Notebook(window)

#Employee Information

employ_info = Frame(notebook, width= 722, height=700)
employ_info.pack(pady=20, side="left")
employ_name = Frame(employ_info, width=722, height=300)
employ_name.pack(pady=40)
employee_name = ttk.Label(employ_name, text="Enter the name of the Employee : ", font="Roboto 14 bold")
employee_name.pack(side="left")
em_name = ttk.StringVar()
employee_name_1 = ttk.Entry(employ_name,width=25, textvariable=em_name)
employee_name_1.pack(padx=10,side="right")
next_but_1 = ttk.Button(employ_info, text="Save", command=emplo_name).pack(pady=25)


#Salary Frame

salary_frame = Frame(notebook, width=800, height=700)
salary_frame.pack()

#Month Name
month_frame = Frame(salary_frame, width=722, height=100)
month_frame.pack(pady=20, padx=20)
entry_1_label = ttk.Label(month_frame, text="Enter the name of the Month : ", font="Roboto 15 bold")
entry_1_label.pack(side="left")
month_name = ttk.StringVar()
month_name.set("January")
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
Month_Combo = ttk.Combobox(master=month_frame, values=months, font="Roboto 15 bold", textvariable=month_name)
Month_Combo.pack()

#Monthly Amount to be given

month_amt = Frame(salary_frame, width=722,height=100)
month_amt.pack()
entry_2_label = ttk.Label(month_amt, text="Enter the Monthly Amount : ", font="Roboto 15 bold")
entry_2_label.pack(side="left")
month_amt_1 = ttk.IntVar()
entry_2 = ttk.Entry(month_amt, width=30, textvariable=month_amt_1)
entry_2.pack(side="left",pady= 20, padx=40)


#Absent days

month_abt = Frame(salary_frame, width=722,height=100)
month_abt.pack()
entry_3_label = ttk.Label(month_abt, text="Enter the No of Absent Days : ", font="Roboto 15 bold")
entry_3_label.pack(side="left")
month_abt_1 = ttk.IntVar()
entry_3 = ttk.Entry(month_abt, width=30, textvariable=month_abt_1)
entry_3.pack(side="left",pady= 20, padx=40)

#Calculate Button

button_frame = Frame(salary_frame, width=722, height=87)
button_frame.pack(pady=20)
button_1 = ttk.Button(button_frame, text="Calculate Salary", command=month_value)
button_1.pack()

#Output Frame

output_frame = Frame(salary_frame,width=722, height=200)
output_frame.pack(pady=50)
x = "The final salary of "
z = "is : "
entry_3_label = ttk.Label(output_frame, text=x, font="Roboto 15 bold")
entry_3_label.pack(side="left")
emplo_name_1 = ttk.StringVar()
entry_4_label = ttk.Label(output_frame, textvariable=emplo_name_1, font="Roboto 15 bold")
entry_4_label.pack(side="left")
entry_5_label = ttk.Label(output_frame, text=z, font="Roboto 15 bold")
entry_5_label.pack(side="left")
my_amount = ttk.StringVar()
entry_3_label = ttk.Label(output_frame, textvariable=my_amount ,font="Roboto 15 bold")
entry_3_label.pack(side="left")


#Author Credit

author_frame = Frame(notebook,width=722,height=100)
author_frame.pack()
label_2 = ttk.Label(author_frame, text="Made by Samdarshi", font="Algerian 13 bold italic underline")
label_2.pack(pady=50)
label_3 = ttk.Label(author_frame, text="Contact no : 9508168502", font="Bahnscript 13 bold italic underline")
label_3.pack(pady=50)


#notebook

notebook.add(employ_info, text="Employee Info")
notebook.add(salary_frame, text="Salary Info")
notebook.add(author_frame,text="Author Info")
notebook.pack()


#run
window.mainloop()
