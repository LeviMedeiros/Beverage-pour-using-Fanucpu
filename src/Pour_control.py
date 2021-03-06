#Import multiprocessing library
import imp
import multiprocessing
from multiprocessing import Process
from multiprocessing.connection import wait

#Import GUI library
import tkinter
from tkinter import *
from tkinter import ttk

#import sleep timer
import time

#Import Files that contain the routines for each robot
from Right_Bot_Routine import right_bot_routine
from Left_Bot_Routine import left_bot_routine

#Declare variables used to change routine per beverage selection
global maxspeed
global maxaccel

maxspeed = 100
maxaccel = 100

#functions to select the routine
def callroutine1():
    callRoutines(1)

def callroutine2():
    callRoutines(2)

def callroutine3():
    callRoutines(3)


#Function to call the routines
def callRoutines(routine):
    #Initializing the multiprocessing
    if __name__ == '__main__':
        
        print(f"got into if statement ")
        p1 = multiprocessing.Process(target = left_bot_routine, args= (routine,))
        p2 = multiprocessing.Process(target = right_bot_routine, args= (routine,))
        p3 = multiprocessing.Process(target = pouringInProg)
        #Start the processes
        p1.start()
        p2.start()
        p3.start()
        
        p1.join()
        p2.join()
        
    #Close the in progress window

#Popup Pouring in progress
def pouringInProg():
    #Pop Up in progress Window
    inProgress = Toplevel(root)
    inProgress.geometry("750x250")
    inProgress.title("Pouring in Progress")
    Label(inProgress, text= "Pouring in progress", font=('Mistral 18 bold')).place(x=150,y=80)

#Setup GUI
root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()

#Code For First option
Option1Image = tkinter.PhotoImage(file='bubly_Rasp_12.png')
ttk.Label(frm,text="Bubly Option 1",font=("Arial",25)).grid(column=1,row=0)
ttk.Button(frm, image=Option1Image, command=callroutine1).grid(column=1, row=1)

#Code for second option
Option2Image = tkinter.PhotoImage(file='bubly_Straw.png')
ttk.Label(frm,text="Bubly Option 2",font=("Arial",25)).grid(column=2,row=0)
ttk.Button(frm, image=Option2Image, command=callroutine2).grid(column=2, row=1)

#Code for third option
Option3Image = tkinter.PhotoImage(file='bubly_Straw.png')
ttk.Label(frm,text="Option 3",font=("Arial",25)).grid(column=3,row=0)
ttk.Button(frm,image=Option3Image, command=callroutine3).grid(column=3, row=1)


ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=3)

#Use GUI
if __name__=='__main__':
    root.mainloop()



