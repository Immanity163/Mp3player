from tkinter import *
from tkinter import filedialog, messagebox
from pygame import mixer
import os


class PLayer:

    def __init__(self, window):
        window.geometry("320x280")
        window.title("Simple Mp3 Player")
        window.resizable(False, False)
        window.configure(bg="#0086A8")

        self.load_button = Button(window, text='Open playlist',  width=10, font=('Times', 10), command=self.load)
        self.play_button = Button(window, text='Play',  width=10, font=('Times', 10), command=self.play)
        self.pause_button = Button(window, text='Pause',  width=10, font=('Times', 10), command=self.pause)
        self.next_song_button = Button(window, text='Next', width=10, font=('Times', 10), command=self.next)
        self.previous_song_button = Button(window, text='Previous', width=10, font=('Times', 10), command=self.previous)

        self.label = Label(text="Music not selected", bg="white")
        self.label.place(x=10, y=10, width=300, height=100)

        self.load_button.place(x=10, y=180)
        self.play_button.place(x=120, y=180)
        self.pause_button.place(x=230, y=180)
        self.next_song_button.place(x=230, y=240)
        self.previous_song_button.place(x=10, y=240)

        self.music_file = None
        self.playing_state = False
        self.song_queue = 0
        self.directory_playlist = None

    def load(self):
        path = filedialog.askdirectory()
        self.directory_playlist = os.listdir(path)

        for i in range(len(self.directory_playlist)):
            self.directory_playlist[i] = path + "/" + self.directory_playlist[i]
            print(self.directory_playlist[i])

        self.music_file = self.directory_playlist[self.song_queue]
        self.file_name_format()

    def play(self):
        if self.music_file is not None:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
        else:
            messagebox.showerror("Music_file_not_Found", "Error: file do not exist or not found."
                                                         "\nPlease open directory with music.")

    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
            if self.playing_state:
                self.pause_button.configure(text="Continue")
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_button.configure(text="Pause")

    def stop(self):
        mixer.music.stop()

    def next(self):
        if self.song_queue < len(self.directory_playlist) - 1:
            self.song_queue += 1
        else: self.song_queue = 0
        if self.music_file is not None:
            self.__play()

    def previous(self):
        if self.song_queue > 0:
            self.song_queue -= 1
        else:
            self.song_queue = len(self.directory_playlist) - 1
        if self.music_file is not None:
            self.__play()


    def file_name_format(self):
        label_name = self.music_file.split(sep="/")[-1]

        self.label.configure(
            text=(lambda label_name:
                  label_name[:30] + "..." if (len(label_name) > 30) else label_name[:30])(label_name))

    def __play(self):
        self.music_file = self.directory_playlist[self.song_queue]
        self.play()
        self.playing_state = False
        self.pause_button.configure(text="Pause")
        self.file_name_format()

win = Tk()
app = PLayer(win)
win.mainloop()
