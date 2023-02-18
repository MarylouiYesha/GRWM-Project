from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer 
import os
import tkinter as tk 
import speech_recognition as sr
import pyttsx3
import pywhatkit

mixer.init()

def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

    status.set("Song PLAYING")

def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")

def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))

    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)


def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song PAUSED")

def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song RESUMED")

def talk(command):
    engine=pyttsx3.init()
    voice=engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.say("Playing "+ command)
    engine.runAndWait()

def takeCommand():
    listener=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("WORK PLEASE!")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            song= command.replace('play','')

            talk(song)
            pywhatkit.playonyt(song)
    except:
        pass

root= Tk()
root.geometry('950x500')
root.title('Music Player')
root.resizable(0, 0)

labelbg=PhotoImage(file="labelbg.png")
pause_img = tk.PhotoImage(file ='pause.png')
play_img = tk.PhotoImage(file="play.png")
resume_img= tk.PhotoImage(file="resume.png")
stop_img= tk.PhotoImage(file="stop.png")
search_img= tk.PhotoImage(file="search.png")
control=PhotoImage(file= "gray.png")


song_frame = Label(root, image=labelbg, width=700, height=250)
song_frame.place(x=0, y=0)

button_frame = Label(root, image=control, width=950, height=100)
button_frame.place(y=380)


listbox_frame = LabelFrame(root, text='Playlist', bg='RoyalBlue')
listbox_frame.place(x=650, y=0, height=500, width=300)

current_song = StringVar(root, value='<Not selected>')

song_status = StringVar(root, value='<Not Available>')

playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Gold')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)

Label(song_frame, text='C U R R E N T L Y    P L A Y I N G:', font=('Courier', 10, 'bold'), height=1, width=65).place(x=-1, y=-2)

song_lbl = Label(song_frame, textvariable=current_song, bg='White', font=("Courier", 9), width=30, height=1)
song_lbl.place(x=180, y=200)

pause_btn = Button(button_frame, image= pause_img, height=30, width=30,
                    command=lambda: pause_song(song_status))
pause_btn.place(x=15, y=10)

stop_btn = Button(button_frame, image= stop_img, height= 30, width=30,
                  command=lambda: stop_song(song_status))
stop_btn.place(x=105, y=10)

play_btn = Button(button_frame, image= play_img, height=30,width=30,
                  command=lambda: play_song(current_song, playlist, song_status))
play_btn.place(x=195, y=10)

resume_btn = Button(button_frame, image= resume_img, height=30, width=30,
                    command=lambda: resume_song(song_status))
resume_btn.place(x=285, y=10)

load_btn = Button(button_frame, text='Load Directory', font=("Courier", 9), width=35,
                  command=lambda: load(playlist))
load_btn.place(x=70, y=55)

search_btn = Button(button_frame, image= search_img, height=30, width=30,
                  command=lambda: takeCommand())
search_btn.place(x=300, y=10)

Label(root, textvariable=song_status, bg='SteelBlue', font=('Times', 9), justify=LEFT).pack(side=BOTTOM, fill=X)

root.update()
root.mainloop()
takeCommand()

