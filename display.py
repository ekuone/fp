# fp
Turn off PC!

from tkinter import *
import time
from my_display import Turn_off
from datetime import date

def history(today, real_time):
    txt_file = open('history.txt', 'a')
    txt_file.write('(date: ' + today)
    txt_file.write(' ' + str(real_time) + ') ')
    txt_file.write("\n")

def clock():

    time_local = Label(my_crean, width = 6, font = 11)
    time_local.pack()
    time_local.place(relx = 0.05, rely = 0.02)
    real_time = time.strftime('%I:%M:%S', time.localtime())
    if real_time!='':
        time_local.config(text = real_time, font = 18)
    my_crean.after(100,clock)

def tick(user_minutes):
    clock = Label(my_crean, width = 6, font = 11)
    clock.pack()
    clock.place(relx = 0.4, rely = 0.02)

    time_1 = int(time.time())
    user_minutes = int(user_minutes) * 60 + 1

    while (user_minutes >= 0):
        if user_minutes == 0:
            Turn_off(3)
            his_time = time.strftime('%I:%M:%S', time.localtime())
            today = str(date.today())
            history(today ,his_time)
            break
        else:
            user_minutes -= 1
            minutes = int(user_minutes/60)
            dis_min = str(minutes)
            if minutes < 10:
                dis_min = '0'  + str(minutes)
            se = user_minutes - (minutes*60)
            dis_sec = str(se)
            if se < 10:
                dis_sec = '0' +str(se)
            clock.config(text = str(dis_min) + ':' + str(dis_sec))
            my_crean.update()
            time_2 = int(time.time())
            while time_2 == time_1:
                time_2 = int(time.time())
            time_1 = time_2

        clock.config(text = " TIME IS UP ", width = 14, font=14)
        clock.update_idletasks()

my_crean = Tk()
my_crean.geometry('220x150')
my_crean.title("SYH")
clock()
global seconds, time_1, time_2
time_1 = ''
time_2 = ''

advise = Label(text = 'when you want to turn off the computer')
advise.place(relx = 0, rely = 0.25)

current_time = Label(text = 'local time')
current_time.pack()
current_time.place(relx = 0.05, rely = 0.15)

half_hour_click = Button(my_crean, text = "30 min", width = 6, command = lambda:tick(30))
one_hour_click = Button(my_crean, text = "1 hour", width = 6, command = lambda:tick(60))
two_hour_click = Button(my_crean, text = "2 hour", width = 6, command = lambda:tick(120))
check_ruslan_teacher = Button(my_crean, text = "♡Ruslan♡", width = 8, command = lambda:tick(0))

half_hour_click.place(relx = 0.1, rely = 0.4)
one_hour_click.place(relx = 0.36, rely = 0.4)
two_hour_click.place(relx = 0.62, rely = 0.4)
check_ruslan_teacher.place(relx = 0.36, rely = 0.6)

my_crean.mainloop()
