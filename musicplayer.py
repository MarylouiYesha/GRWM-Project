from tkinter import*
import tkinter as tk
import fnmatch
from tkinter import ttk, filedialog
from pygame import mixer 
import os

canvas= tk.Tk()
canvas.title("Music Player")
canvas.geometry("920x670+290+85")
canvas.configure(bg="#0f1a2b")
canvas.resizable(False,False)

mixer.init()

#button
play_button=PhotoImage(file="play.jpg")
Button(canvas, image=play_button, bg="#0f1")



canvas.mainloop()
