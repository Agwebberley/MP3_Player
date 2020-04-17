from pygame import mixer
from tkinter import *
root = Tk()
root.title("MP3")

def play():
	print("playing")

	mixer.music.load(directorye.get())
	mixer.music.play()

def unpause():
	print("testing if unpause is needed")
	try:
		print("still testing")
		if unpause == True:
			print("unpausing")
			print(lastpos)
			mixer.music.unpause()
	except:
		print("unpause not needed")
		play()


def pause():
	global unpause
	global lastpos

	lastpos = mixer.music.get_pos()
	unpause = True
	mixer.music.pause()


mixer.init()


directoryl = Label(text="Enter the Directory of the MP3")
directoryl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

directorye = Entry(root, )
directorye.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

playB = Button(root, text="Play", command=unpause)
playB.grid(row=2, column=0)
pauseB = Button(root, text="Pause", command=pause)
pauseB.grid(row=2, column=1)

root.mainloop()