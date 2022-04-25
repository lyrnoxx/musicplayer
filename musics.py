from re import T
from xml.dom.pulldom import START_DOCUMENT
import pygame
from tkinter import *
import pygame.mixer
import os
import ntpath
from tkinter.messagebox import *


pygame.init()
pygame.mixer.init()
root=Tk()
root.geometry("1280x720+0+0")
root.configure(background="#5CDB95")
img=PhotoImage(file="bg-design.png")
label=Label(
  root,
  image=img
)
label.place(x=0,y=0)
Tops=Frame(root,width=1350,height=50,bd=8,bg="#85DCBC")
Tops.pack(side=TOP,anchor=NW)


lblinfo=Label(Tops,font=('sans',30,'italic'),text="Advanced Music Player",bd=10,bg="#85DCBC",fg="#05386B")
lblinfo.grid(row=0,column=0)
list=[]
list5=[]
for rt, dirs, files in os.walk('/home/'):
  for file in files:
    if file.endswith('.mp3'):
      list.append(os.path.join(rt,file))	
txtdisplay=Listbox(root,height=23,width=38,bd=16,font=('arial',15,'bold'),fg="#05386B",bg="#41B3A3")
txtdisplay.place(relx=0.8,rely=0.55,anchor=CENTER)
i=0
for name in list:
  list5.append(ntpath.basename(name))
  txtdisplay.insert(END,list5[i])
  i+=1					
index=0
def next():
  global index
  index+=1 
  if index==len(list):
    btn5['state']='disabled'
    pygame.mixer.music.stop()
    txtdisplay.itemconfig(index-1, {'fg': 'green'})
    index=0
    showinfo("FYI","your songs are over, if you want listen again press play button")
  else:
    txtdisplay.itemconfig(index-1, {'fg': 'green'})
    txtdisplay.itemconfig(index, {'fg': 'red'})
    pygame.mixer.music.load(list[index])
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause() 
def previous():
  global index
  index-=1               
  if index==-1:
    pygame.mixer.music.stop()
    txtdisplay.itemconfig(index+1, {'fg': 'green'})
    showinfo("FYI","your previous songs are over if u want play from starting press play button continue?")
    index=0
  else:
    txtdisplay.itemconfig(index, {'fg': 'red'})
    txtdisplay.itemconfig(index+1, {'fg': 'green'})            
    pygame.mixer.music.load(list[index])
    pygame.mixer.music.play() 
def play():
  global index
  btn5['state']='normal'
  txtdisplay.itemconfig(index, {'fg': 'red'})
  pygame.mixer.music.load(list[index])
  pygame.mixer.music.play()
def exit():
  exit=askyesno("exit","sure?")
  if exit>0:
    root.destroy()
    return    
btn6=Button(root,text="play",fg="#EDF5E1",padx=10,pady=10,bd=4,width=10,bg="#41B3A3",font=('arial',15,'bold'),command=play)
btn6.place(relx=0.3,rely=0.3,anchor=CENTER)                                                          
btn5=Button(root,text="next",fg="#EDF5E1",bg="#41B3A3",padx=10,pady=10,bd=4,width=10,state="normal",font=('arial',15,'bold'),command=next)
btn5.place(relx=0.3,rely=0.4,anchor=CENTER)        
btn1=Button(root,text="stop",fg="#EDF5E1",bg="#41B3A3",padx=10,pady=10,bd=4,width=10,font=('arial',15,'bold'),command=stop)
btn1.place(relx=0.3,rely=0.5,anchor=CENTER)
btn2=Button(root,text="pause",fg="#EDF5E1",bg="#41B3A3",padx=10,pady=10,bd=4,width=10,font=('arial',15,'bold'),command=pause)
btn2.place(relx=0.3,rely=0.6,anchor=CENTER)
btn3=Button(root,text="unpause",fg="#EDF5E1",bg="#41B3A3",padx=10,pady=10,bd=4,width=10,font=('arial',15,'bold'),command=unpause)
btn3.place(relx=0.3,rely=0.7,anchor=CENTER)
btn4=Button(root,text="previous",fg="#EDF5E1",bg="#41B3A3",padx=10,pady=10,bd=4,width=10,font=('arial',15,'bold'),command=previous)
btn4.place(relx=0.3,rely=0.8,anchor=CENTER)    
btn7=Button(root,text="Exit",fg="#EDF5E1",bg="#41B3A3",padx=10,pady=10,bd=4,width=10,font=('arial',15,'bold'),command=exit)
btn7.place(relx=0.3,rely=0.8,anchor=CENTER)
root.mainloop()                         
