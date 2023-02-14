from tkinter import*
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer 
import os

canvas= tk.Tk()
canvas.title("Music Player")
canvas.geometry("920x670+290+85")
canvas.configure(bg="#0f1a2b")
canvas.resizable(False,False)

mixer.init()



canvas.mainloop()
