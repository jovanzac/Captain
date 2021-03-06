import tkinter as tk
from tkinter.ttk import Button
from PIL import Image, ImageTk
import time
from cv2 import cv2
from threading import Thread
from Scripts.music_player import m_player


# The Video Player
class VideoPlayer :
    def __init__(self,parent:object) :
        """Initialize the parent window and set play to false."""
        self.parent = parent
        self.play = False

    def player(self,vid_file:str,m_file:str,nxt_func:object):
        def get_frame():
            ret,frame = vid.read()
            if ret and self.play :
                return(ret,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
            else :
                return(ret,None)
        def update() :
            ret,frame = get_frame()
            if ret and self.play :
                img = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image=img)
                photo.image=img
                self.canvas.itemconfig(self.vid_frame,image=photo)
                self.canvas.image=photo
                self.parent.after(delay,update)
            else :
                # stopping vid_music and starting game music
                m_player.playing = ""
                time.sleep(0.01)
                nxt_func()

        def skip() :
            self.play = False

        self.parent.clear()
        self.play = True

        # starting music
        m_player.playing = m_file
        vid = cv2.VideoCapture(vid_file)
        width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas = tk.Canvas(self.parent, width = width, height = height)
        self.canvas.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        self.vid_frame = self.canvas.create_image(0, 0, anchor = tk.NW)

        # Skip button
        if vid_file != "project_media\\glitch.mp4" :
            skip_thread = Thread(target=skip)
            skip = Button(self.parent,text="Skip",command=skip_thread.start,style="skip.TButton")
            skip.place(relx=0.88,rely=0.04)

        delay = 5
        update()