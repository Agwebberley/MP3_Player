from pygame import mixer
from tkinter import *
root = Tk()
root.title("MP3")

def play():
	mixer.init()
	mixer.music.load(directorye.get())
	mixer.music.play(start=lastpos)




def pause():
	lastpos = mixer.music.get_pos()
	mixer.music.pause()


global lastpos

lastpos = 0

directoryl = Label(text="Enter the Directory of the MP3")
directoryl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

directorye = Entry(root, )
directorye.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

playB = Button(root, text="Play", command=play)
playB.grid(row=2, column=0)
pauseB = Button(root, text="Pause", command=pause)
pauseB.grid(row=2, column=1)

root.mainloop()