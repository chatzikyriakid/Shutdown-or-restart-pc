from tkinter import *
import os
import time
from playsound import playsound


def shutdown():
    timer = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    if timer > 0:
        time.sleep(timer)
        playsound(r'C:\Users\Beast\Documents\Python Scripts\Shutdown or restart pc with timer\beep.wav')
        os.system("shutdown /s /t 1")


def restart():
    timer = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    if timer > 0:
        time.sleep(timer)
        playsound(r'C:\Users\Beast\Documents\Python Scripts\Shutdown or restart pc with timer\beep.wav')
        os.system("shutdown /r /t 1")


def convert_to_secs(hours, mins, secs):
    return int(hours) * 3600 + int(mins) * 60 + int(secs)


# initialize window
window = Tk()
window.title('Shutdown or restart with timer')
window.geometry('470x200')
window.resizable(0, 0)

# shutdown button
lbl = Label(window, text='    ')
lbl.grid(column=0, row=0)
lbl1 = Label(window, text='    ')
lbl1.grid(column=0, row=1)
shut_btn = Button(window, text='Shutdown now', font=("Arial Bold", 12), bg='#2CA9E0',
                  command=shutdown)
shut_btn.grid(column=1, row=1)
# restart button
lbl = Label(window, text='    ')
lbl.grid(column=0, row=2)
lbl2 = Label(window, text='    ')
lbl2.grid(column=0, row=3)
rest_btn = Button(window, text='Restart now', font=("Arial Bold", 12), bg='#155470', fg='#C1C5C5',
                  command=restart)
rest_btn.grid(column=1, row=3)

# timer function
lbl3 = Label(window, text='    ')
lbl3.grid(column=5, row=2)
or_label = Label(window, text='OR', font=("Arial Bold", 12))
or_label.grid(column=6, row=2)
lbl4 = Label(window, text='    ')
lbl4.grid(column=7, row=2)
timer_lbl = Label(window, text='Set timer', font=("Arial Bold", 12), bg='#8BDF95')
timer_lbl.grid(column=9, row=1)

# spinboxes
hours_lbl = Label(window, text='Hours', font=("Arial Bold", 10), bg='#8BDF95')
hours_lbl.grid(column=8, row=2)
minutes_lbl = Label(window, text='Minutes', font=("Arial Bold", 10), bg='#8BDF95')
minutes_lbl.grid(column=9, row=2)
seconds_lbl = Label(window, text='Seconds', font=("Arial Bold", 10), bg='#8BDF95')
seconds_lbl.grid(column=10, row=2)
hours = Spinbox(window, from_=0, to=24, width=5)
hours.grid(column=8, row=3)
minutes = Spinbox(window, from_=0, to=60, width=5)
minutes.grid(column=9, row=3)
seconds = Spinbox(window, from_=0, to=60, width=5)
seconds.grid(column=10, row=3)

# set button
shutdown_btn = Button(window, text='Shutdown', font=("Arial Bold", 12), bg='black', fg='white',
                      command=shutdown)
shutdown_btn.grid(column=8, row=5)
restart_btn = Button(window, text='Restart', font=("Arial Bold", 12), bg='black', fg='white',
                     command=restart)
restart_btn.grid(column=10, row=5)

window.mainloop()
