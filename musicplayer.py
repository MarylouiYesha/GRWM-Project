from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer 
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

playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Gold')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)

Label(song_frame, text='CURRENTLY PLAYING:', bg='LightBlue', font=('Times', 10, 'bold')).place(x=5, y=20)

song_lbl = Label(song_frame, textvariable=current_song, bg='Goldenrod', font=("Times", 12), width=25)
song_lbl.place(x=150, y=20)


canvas.update()
canvas.mainloop()

