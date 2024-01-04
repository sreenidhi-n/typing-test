import tkinter as tk
from tkinter import CENTER, GROOVE, Entry, StringVar, ttk, filedialog, PhotoImage
from tkinter import HORIZONTAL
import random 
import time
from turtle import width 
import difflib 

def start():
    limit = 100
    start = 0
    load_speed = 1
    while(start<limit):
        time.sleep(0.05)
        bar['value']+=(load_speed/limit)*100
        start+=load_speed
        percent.set(str(int((start/limit)*100))+"%")
        window.update_idletasks() 
    window.destroy()

window = tk.Tk()
window.title('Loading...')
icon = PhotoImage(file = r'C:\Users\hp\Desktop\project\attribute edt.im.png')
window.iconphoto(False,icon)
window.config(bg = 'ghost white')
percent = StringVar()
text = StringVar()
bar = ttk.Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)
percentLabel = tk.Label(window,textvariable=percent).pack()
button = tk.Button(window,text="Start",command=start).pack()
window.mainloop() 

def main(): 
    global text1
    root = tk.Tk()
    root.geometry('950x600')
    bgimg = PhotoImage(file=r'C:\Users\hp\Desktop\project\download_edited(1).png')
    photo_label = tk.Label(root, image=bgimg)
    photo_label.place(x=0,y=0)
    icon = PhotoImage(file = r'C:\Users\hp\Desktop\project\attribute edt.im.png')
    root.iconphoto(False,icon)
    logo = PhotoImage(file = r'C:\Users\hp\Desktop\project\text (2).png')
    logo_label = tk.Label(root, image=logo)
    logo_label.place(x=305,y=25)
    root.title('Typing Test')

    heading = tk.Label(text = 'Typing Test',bg = 'gray97', font = ('Candara',35), justify = CENTER).place(x = 350,y = 10)
    textvar = open('C:/Users/hp/Desktop/project/test.txt').read().split('\n')
    text1 = tk.Label(text = random.choice(textvar),bg = 'gray97',font=('Candara',19))
    text1.place(x=175,y=200)
    accuracy = '0%'
    entry_field = tk.Entry(root,width=35, font=('Candara',20))
    entry_field.place(x=175,y=300)
    entry_field.focus()

    def add_file(): 
        global filename, text1
        filename = filedialog.askopenfilename()
        print('Selected:', filename)
        text2 = random.choice(open(filename).read().split('.'))
        text1.config(text = text2, bg = 'gray97',font=('Candara',17))
        text1.place(x=175,y=200) 
    if entry_field.get() != '': 
        if len(entry_field.get()) == len(text1.cget('text')):
            text1 = tk.Label(text = random.choice(open('C:/Users/hp/Desktop/project/test.txt').read().split('\n')),bg = 'gray97',font=('Candara',17))
            text1.place(x=175,y=200) 
    add_button = tk.Button(root, text='Open', height=2, width=6,relief=GROOVE, font = ('Candara',12), command=add_file).place(x=175,y=500)

    def clearfunc():
        global t0, accuracy_lbl, w_count, text1, t1
        global filename
        global mylabel
        global mylabel1
        entry_field.delete(0,'end') 
        entry_field.config(fg='black')
        text1.config(text = random.choice(open('C:/Users/hp/Desktop/project/test.txt').read().split('\n')),bg = 'gray97',font=('Candara',19))
        text1.place(x=175,y=200)
        w_count = 0 
        t0 = time.time()
        t1 = time.time()
    reset_button = tk.Button(root, text='Reset', height=2, width=6,relief=GROOVE, font = ('Candara',12), command=clearfunc).place(x=375,y=500)

    t0 = time.time()
    def calculate(*args,**kwargs):
        global entry
        global t1 
        global accuracy_lbl
        global w_count, accuracy_lbl, type_speed, mylabel1, mylabel
        global speed

        t1 = time.time()
        entry = entry_field.get()
        w_count = len(entry.split())

        if t1 != t0: 
            my_label = tk.Label(root, text="SPEED: " ,bg = 'gray97', font = ('Candara',13))
            mylabel = tk.Label(root, text="TOTAL WORDS: " + str(w_count),bg = 'gray97', font = ('Candara',13))
            mylabel.place(x=375, y=400)
            mylabel1 = tk.Label(root, text="TIME TAKEN(sec): " + str(round(t1-t0)),bg = 'gray97', font = ('Candara',13))
            mylabel1.place(x=575, y=400)

            if not text1.cget('text').startswith(entry_field.get()):
                entry_field.config(fg = 'red')
            else:
                entry_field.config(fg = 'green')
            if entry == text1.cget('text'):
                entry_field.config(fg = 'green')
            speed = round(((60*w_count)/((t1-t0)*5)),2)
            type_speed =  tk.Label(text = 'SPEED: '+str(speed)+ ' WPM ', bg = 'gray97', font = ('Candara',13))
            type_speed.place(x = 175,y = 450)
            accuracy = round(difflib.SequenceMatcher(None,text1.cget("text"),entry_field.get()).ratio()*100,2)
            accuracy_lbl = tk.Label(root, text= "ACCURACY: "+  str(accuracy) + '%' ,bg = 'gray97', font = ('Candara',13)) 
            accuracy_lbl.place(x=575, y=450)
            if speed >= 25:
                my_label.configure(text="SPEED: EXCELLENT")
                my_label.place(x=175, y=400)
            elif speed >= 10 and speed <= 25 :
                my_label.configure(text="SPEED: AVERAGE ")
                my_label.place(x=175, y=400)
            else:
                my_label.configure(text="SPEED: POOR")
                my_label.place(x=175, y=400)
    calculate()
    result_btn = tk.Button(root, text="Result", font=('Candara',12),height=2, width=6,relief=GROOVE, command=calculate).place(x=575,y=500)
    root.mainloop()  
main() 
