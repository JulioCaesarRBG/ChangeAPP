from tkinter import *
from tkinter import ttk
import pyautogui
import time
import serial
import os

apk = Tk()
apk.title("Aplikasi Keamanan")
apk.iconbitmap("bochicon.ico")
apk.geometry("696x464")
    
ser = serial.Serial ('COM5', 9600) #port yang digunakan COM5 atau COM6 ketika menggunakan bluetooth
door = ser.readline(1000)
print (door)
 
running = False
running2 = False
running3 = False

def change_app():
    global door
    global ser
    if running:
        data = ser.readline(1000)
        if door != data:
            door = data
            print(door) 
            pyautogui.keyDown('alt')
            time.sleep(.1)
            pyautogui.press('tab')
            time.sleep(.1)
            pyautogui.keyUp('alt')
    apk.after(40, change_app)

def on_start():
   global running
   running = True

def on_stop():
   global running
   running = False

def close_app():
    global door
    global ser

    if running2:
        data = ser.readline(1000)
        if door != data:
            door = data
            print(door)
            pyautogui.keyDown('alt')
            time.sleep(.1)
            pyautogui.press('F4')
            time.sleep(.1)
            pyautogui.keyUp('alt')
            apk.destroy()
    apk.after(40, close_app)

def on_start2():
   global running2
   running2 = True

def on_stop2():
   global running2
   running2 = False

def shut():
    global door
    global ser

    if running3:
        data = ser.readline(1000)
        if door != data:
            door = data
            print(door)
            os.system("shutdown /s /t 1")
    apk.after(40, shut)

def on_start3():
   global running3
   running3 = True

def on_stop3():
   global running3
   running3 = False

c=Canvas(apk,bg="gray16",height=200,width=100)
filename=PhotoImage(file="G:\i\hmm.png")
background_label=Label(apk,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

c.pack()

canvas = Canvas(apk, bg="Turquoise1", width=200, height=30)
canvas.create_text(100, 15, text="Mengganti tab aplikasi", font=('Comic Sans MS', 12))
canvas.pack()

start = ttk.Button(apk, text="Start", command=on_start)
start.pack(padx=10)

stop = ttk.Button(apk, text="Stop", command=on_stop)
stop.pack(padx=10)


canvas2 = Canvas(apk, bg="Turquoise2", width=200, height=30)
canvas2.create_text(100, 15, text="Menutup tab aplikasi", font=('Comic Sans MS', 12))
canvas2.pack()

start2 = ttk.Button(apk, text="Start", command=on_start2)
start2.pack(padx=10)

stop2 = ttk.Button(apk, text="Stop", command=on_stop2)
stop2.pack(padx=10)


canvas3 = Canvas(apk, bg="Turquoise3", width=200, height=30)
canvas3.create_text(100, 15, text="Mematikan PC", font=('Comic Sans MS', 12))
canvas3.pack()

start3 = ttk.Button(apk, text="Start", command=on_start3)
start3.pack(padx=10)

stop3 = ttk.Button(apk, text="Stop", command=on_stop3)
stop3.pack(padx=10)

apk.after(40, change_app)
apk.after(40, close_app)
apk.after(40, shut)
apk.mainloop()