from tkinter import *
from tkinter import filedialog
from pygame import mixer


class MusicPlayer:
    #GUI設計
    def __init__(self, window):
        self.Music_File = False 
        self.Playing_State = False

        #設置物件
        window.geometry('320x100'); window.title('Tkinter_Music_Player'); window.resizable(0,0)
        Load = Button(window, text = '載入',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = '播放',  width = 10,font = ('Times', 10), command = self.play)
        self.Pause = Button(window,text = '暫停',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = '停止',  width = 10, font = ('Times', 10), command = self.stop)
        #設置物件位置
        Load.place(x=0,y=20)
        Play.place(x=110,y=20)
        self.Pause.place(x=220,y=20)
        Stop.place(x=110,y=60) 
           
    #載入
    def load(self):
        self.Music_File = filedialog.askopenfilename() #選擇音樂檔案

    #播放
    def play(self):
        if self.Music_File: #已選擇音樂檔案
            mixer.init()
            mixer.music.load(self.Music_File)
            mixer.music.play()

    #暫停
    def pause(self):
        if not self.Playing_State: #若不在播放
            mixer.music.pause()
            self.Playing_State=True
            self.Pause.configure(text='繼續') #修改物件名稱
        else:
            mixer.music.unpause()
            self.Playing_State = False
            self.Pause.configure(text='暫停') #修改物件名稱

    #停止
    def stop(self):
        mixer.music.stop()

root = Tk()
app= MusicPlayer(root)
root.mainloop()