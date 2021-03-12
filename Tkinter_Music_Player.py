import tkinter.messagebox as msbox
from tkinter import *
from tkinter import filedialog
from pygame import mixer


class MusicPlayer:
    #GUI設計
    def __init__(self, window):
        self.Music_File = False 
        self.File_name = StringVar()
        self.File_name.set('歌名:')
        self.Playing_State = False

        #設置物件
        window.geometry('320x100')
        window.title('Tkinter_Music_Player')
        window.resizable(0,0)
        File_name = Label(window, textvariable = self.File_name, width = 0, font = ('Times', 12))
        Load = Button(window, text = '載入',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = '播放',  width = 10,font = ('Times', 10), command = self.play)
        self.Pause = Button(window,text = '暫停',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = '停止',  width = 10, font = ('Times', 10), command = self.stop)
        
        #設置物件位置
        File_name.place(x=0,y=10)
        Load.place(x=0,y=35)
        Play.place(x=110,y=35)
        self.Pause.place(x=220,y=35)
        Stop.place(x=110,y=65) 

    #載入
    def load(self):
        self.Music_File = filedialog.askopenfilename() #選擇音樂檔案
        self.File_name.set('歌名: ' + self.Music_File.split('/')[-1])
        
    #播放
    def play(self):
        if self.Music_File: #已選擇音樂檔案
            mixer.init()
            mixer.music.load(self.Music_File)
            mixer.music.play()
            self.Playing_State = True
        else:
            msbox.showinfo('提示','尚未選擇檔案')
            self.Playing_State = False

    #暫停
    def pause(self):
        if self.Playing_State: 
            try:
                mixer.music.pause()
                self.Playing_State = False
                self.Pause.configure(text='繼續') #修改物件名稱
            except:
                pass
        else:
            try:
                mixer.music.unpause()
                self.Playing_State = True
                self.Pause.configure(text='暫停') #修改物件名稱
            except:
                pass

    #停止
    def stop(self):
        try:
            mixer.music.stop()
        except:
            pass


if __name__ == '__main__':
    root = Tk()
    app= MusicPlayer(root)
    root.mainloop()
