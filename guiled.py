from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

#GUI DEFINITIONS
root = Tk()
root.title("LED Toggler")

var=IntVar()


##EVENT FUNCTIONS



def REDledtoggle():
	GPIO.output(40, GPIO.HIGH)	# Turn on red
	GPIO.output(38, GPIO.LOW)	# Turn off yellow
	GPIO.output(36, GPIO.LOW)	# Turn off green

def YELLOWledtoggle():
	GPIO.output(40, GPIO.LOW)	# Turn off red
	GPIO.output(38, GPIO.HIGH)	# Turn on yellow
	GPIO.output(36, GPIO.LOW)	# Turn off green

def GREENledtoggle():
	GPIO.output(40, GPIO.LOW)	# Turn off red
	GPIO.output(38, GPIO.LOW)	# Turn off yellow
	GPIO.output(36, GPIO.HIGH)	# Turn on green
	
	
     


def close():
	GPIO.cleanup()
	root.destroy()



##WIDGETS##
R1=Radiobutton(root,text="Red Led Toggle",variable=var,value=1,command=REDledtoggle, bg='red')
R1.pack();

R2=Radiobutton(root,text="Yellow Led Toggle",variable=var,value=2,command=YELLOWledtoggle, bg='yellow')
R2.pack()

R3=Radiobutton(root,text="Green Led Toggle",variable=var,value=3,command=GREENledtoggle, bg='green')
R3.pack()

exitbutton=Button(root, text='Exit',command=close, bg='blue')
exitbutton.pack()

root.protocol("WM_DELETE_WINDOW", close) #exit cleanly

root.mainloop()
