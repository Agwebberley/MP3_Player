from pygame import mixer
from tkinter import *
import glob
import os
import time
from mutagen.mp3 import MP3
root = Tk()
root.title("MP3")
currentDirectory = os.getcwd()
root.iconbitmap(currentDirectory + "/ico.ico")

def play():
	print("playing")
	global playing
	playing = True
	direct = directorye.get()
	direct = direct.lower()

	if direct.endswith(".mp3"):
		mixer.music.load(directorye.get())
		mixer.music.play()
	else:
		dire = r"C:\Users\agweb\Downloads\Music"
		mp3s = glob.glob(dire + r"\*.MP3")
		print(dire)
		print(mp3s)
		print()
		#mp3s =+ glob.glob(directorye.get() + "*.MP3")
		for i in mp3s:
			print(i)

			mixer.music.load(i)
			mixer.music.play()
			audio = MP3(i)
			window.after(audio.info.length)
			#time.sleep(audio.info.length)
			#mixer.music.queue(mp3s[i+1])

def unpause():
	print("testing if unpause is needed")
	

	if willunpause == True:
		global playing
		playing = True
		print("unpausing")
		print(lastpos)
		mixer.music.unpause()
	elif willunpause == False:
		print("unpause not needed")
		play()


def pause():
	global willunpause
	global lastpos
	global playing
	playing = False

	lastpos = mixer.music.get_pos()
	willunpause = True
	mixer.music.pause()



def restart():
	mixer.music.rewind()





def pauseoplay():
	if playing == False:
		unpause()
	else:
		pause()


def homeF():
	player.grid_forget()
	instructionsLF.grid_forget()
	downloader.grid_forget()
	player.grid(row=0, column=1)

def downloaderF():
	player.grid_forget()
	instructionsLF.grid_forget()
	downloader.grid_forget()
	downloader.grid(row=0, column=1, pady=10, padx=10)

def instructionsF():
	player.grid_forget()
	downloader.grid_forget()
	instructionsLF.grid_forget()
	instructionsLF.grid(row=0, column=1, pady=10, padx=10)



global willunpause
willunpause = False

global playing
playing = False


mixer.init()

menu = LabelFrame(padx=5, pady=5)
menu.grid(row=0, column=0, pady=10, padx=10)

downloader = LabelFrame(root, padx=5, pady=5)

player = LabelFrame(padx=5, pady=5)
player.grid(row=0, column=1, pady=10, padx=10)


homeb = Button(menu, text="Home", command=homeF)
downloaderb = Button(menu, text="Downloader", command=downloaderF)
homeb.grid(row=0, column=0)
downloaderb.grid(row=1, column=0)

directoryl = Label(player, text="Enter the Directory of the MP3")
directoryl.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

directorye = Entry(player)
directorye.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
directory = r"C:\Users\agweb\Downloads\Music"
directorye.insert(0, directory)

playB = Button(player, text="Play", command=pauseoplay)
playB.grid(row=2, column=0)
pauseB = Button(player, text="Pause", command=pause)
pauseB.grid(row=2, column=1)
rewindB = Button(player, text="Restart", command=restart)
rewindB.grid(row=2, column=2)



downloaderL = Label(downloader, text="Incomplete")
downloaderL.grid(row=0, column=0)

instructionsLF = LabelFrame(root, padx=5, pady=5)
instructionsB = Button(menu, text="instructions", command=instructionsF)
instructionsB.grid(row=2, column=0)
instructionsL = Label(instructionsLF, text="Incomplete")
instructionsL.grid(row=0, column=0)

root.mainloop()