from tkinter import*
import tkinter as tk
import fnmatch
from tkinter import ttk, filedialog
from pygame import mixer 
import os

mixer.init()

def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

    status.set("Song PLAYING")

canvas= tk.Tk()
canvas.title("Music Player")
canvas.geometry("920x670+290+85")
canvas.configure(bg="#0f1a2b")
canvas.resizable(False,False)



#button
play_button=PhotoImage(file="play.jpg")
Button(canvas, image=play_button, bg="#0f1").place(x=100,y=400)



canvas.mainloop()
