from tkinter import *
from tkinter import filedialog
import time
import pygame
import os

root = Tk()
#button images
play_button_image = PhotoImage(file='assets/play_button.png')
pause_button_image = PhotoImage(file='assets/pause_button.png')
prev_button_image = PhotoImage(file='assets/prev_button.png')
next_button_image = PhotoImage(file='assets/next_button.png')

#taking time
greeting_time = time.localtime()


#create the window and its properties
root.title("MusicPlayerTest")
root.geometry("640x500")
root.resizable(False, False)
pygame.mixer.init()

def load_music():
    global current
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current = songs[songlist.curselection()[0]]
#button functions
def play_song():
    global current, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_song():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_song():
    global current, paused
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current) + 1)
        current = songs[songlist.curselection()[0]]
        play_song()
    except:
        pass

def prev_song():
    global current, paused
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current) - 1)
        current = songs[songlist.curselection()[0]]
        play_song()
    except:
        pass

#song list variables
songs = []
current = ""
paused = False;

songlist = Listbox(root, bg = "#706f6f", fg = "black", width = "100", height = "27")
songlist.pack()

#adding menubar
menubar = Menu(root)
root.config(menu = menubar)
add_menu = Menu(menubar, tearoff = False)
add_menu.add_command(label = 'Select Folder', command = load_music)
menubar.add_cascade(label='Add', menu = add_menu)

#initializing buttons
control_frame = Frame(root)
control_frame.pack()
play_button = Button(control_frame, image = play_button_image, borderwidth = 0, command = play_song)
pause_button = Button(control_frame, image = pause_button_image, borderwidth = 0, command = pause_song)
next_button = Button(control_frame, image = next_button_image, borderwidth = 0, command = next_song)
prev_button = Button(control_frame, image = prev_button_image, borderwidth = 0, command = prev_song)
#grid buttons
play_button.grid(row = 0, column = 1, padx = 7, pady = 10)
pause_button.grid(row = 0, column = 2, padx = 7, pady = 10)
next_button.grid(row = 0, column = 3, padx = 7, pady = 10)
prev_button.grid(row = 0, column = 0, padx = 7, pady = 10) 

root.mainloop()