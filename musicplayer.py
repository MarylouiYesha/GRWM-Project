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

def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")

def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song RESUMED")

canvas= Tk()
canvas.title("Music Player")
canvas.geometry('700x220')
canvas.configure(bg="#0f1a2b")
canvas.resizable(0.0)

song_frame = LabelFrame(canvas, text='Current Song', bg='LightBlue', width=400, height=80)
song_frame.place(x=0, y=0)


#button
play_button=PhotoImage(file="play.jpg")
Button(canvas, image=play_button, bg="#0f1").place(x=100,y=400)

button_frame = LabelFrame(canvas, text='Control Buttons', bg='Turquoise', width=400, height=120)
button_frame.place(y=80)

listbox_frame = LabelFrame(canvas, text='Playlist', bg='RoyalBlue')
listbox_frame.place(x=400, y=0, height=200, width=300)

current_song = StringVar(canvas, value='<Not selected>')
song_status = StringVar(canvas, value='<Not Available>')



canvas.mainloop()
