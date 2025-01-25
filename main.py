from tkinter import *
import math
import random
import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20
reps = 0
timer_new = None
rows = 5
ROW_COLOR = "#B0C5A4"
ROW_COLOR2 = "#EBC49F"
list_items = []
count = 0
test =0
start_c = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer_new)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    check.config(text="")
    global reps 
    reps = 0


     


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global start_c

    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%8==0:
        count_down(long_break_sec)
        timer.config(text="LONG BREAK",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        timer.config(text="SHORT BREAK",fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="WORK",fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global count_sec
    global count_min
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
     
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer_new
        timer_new = window.after(1000, count_down, count-1)
    else:
        showwindow()
        play()
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text=marks)

def change():
    global rows
    list_items[rows-6].config(bg=ROW_COLOR)


def items():
    global rows
    global list_items
    item = task_input.get()
    if item=="":
        return 0
    new_label = Label(text=item)
    new_label.grid(column=1,row=rows)
    new_button = Button(text='✔',command=change)
    new_button.grid(column=2,row=rows)

    rows+=1
    list_items.append(new_label)

    new_label.config(bg=ROW_COLOR2)

def showwindow():
    window.deiconify()

def pause():
    global test
    check = False
    if test%2==0:
        window.after_cancel(timer_new)
        pause_b.config(text='Unpause')
    else:
        count_down((count_min*60)+(count_sec))
        pause_b.config(text='Pause')
    test+=1
    
def play():
    playsound.playsound('/Users/mrinaalnahata/Downloads/mixkit-achievement-bell-600.wav')



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)







canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/Users/mrinaalnahata/CODE/Python 100 days/pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)



timer = Label(text="TIMER",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
timer.grid(column=1,row=0)

start = Button(text="Start",highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)

reset = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(column=2,row=2)

add = Button(text="Add",highlightthickness=0,command=items)
add.grid(column=1,row=4)

pause_b = Button(text="Pause",highlightthickness=0,bg=YELLOW,relief='flat',padx=0,pady=0,command=pause)
pause_b.grid(column=0,row=3)


task_input = Entry()
task_input.grid(column=1,row=3)

check = Label(fg=GREEN,bg=YELLOW)
check.grid(column=1,row=2)






window.mainloop()







