from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import Scrollbar
root = tk.Tk()

root.title("APx")
#Settings
text=[]
def clear():
    swtext.delete(1.0,END)
def get_text():
    i=swtext.get(1.0,END).strip("\n")
    print(i)
def add():
    f=var.get()
    print(f)
    if f == 1:
        state = ACTIVE
        Bass = Checkbutton(secondframe,text="Bass", state=state, bg="blue", fg="white", selectcolor="grey")
        Bass.grid(row=14, column=2)
        Mid = Checkbutton(secondframe,text="Mid", state=state, bg="blue", fg="white", selectcolor="grey")
        Mid.grid(row=14, column=3)
        Treble = Checkbutton(secondframe,text="Treble", state=state, bg="blue", fg="white", selectcolor="grey")
        Treble.grid(row=14, column=4)
    if f == 0:
        state = DISABLED
        Bass = Checkbutton(secondframe,text="Bass", state=state, bg="blue", fg="white", selectcolor="grey")
        Bass.grid(row=14, column=2)
        Mid = Checkbutton(secondframe,text="Mid", state=state, bg="blue", fg="white", selectcolor="grey")
        Mid.grid(row=14, column=3)
        Treble = Checkbutton(secondframe,text="Treble", state=state, bg="blue", fg="white", selectcolor="grey")
        Treble.grid(row=14, column=4)
#Browse
mydir=""
def myplace():
    mydir=filedialog.askopenfile()
    l1.config(text=mydir)



#Background
h=600 #heigth
w=620 #width
root.geometry(f"{w}x{h}+100+100")#size settings
root.minsize(500,500)
root.maxsize(800,800)
root.resizable(False,True)
root.config(bg="white")#background color
root.attributes("-toolwindow", True)


# h = Scrollbar(root, orient='horizontal')
# h.pack(side=BOTTOM, fill=X)
# v = Scrollbar(root)
# v.pack(side=RIGHT, fill=Y)
# v.config(command=Can1.yview)
# h.config(command=Can1.xview)
FMas = Frame(root, bg="white")
FMas.pack(fill=BOTH,expand=1)

Can1=Canvas(FMas, bg="white")
Can1.pack(side=LEFT, fill=BOTH, expand=1)

myscrollbar=Scrollbar(FMas, orient=VERTICAL, command=Can1.yview)
myscrollbar.pack(side=RIGHT, fill=Y)

Can1.configure(yscrollcommand=myscrollbar.set)
Can1.bind("<Configure>", lambda e:Can1.configure(scrollregion=Can1.bbox("all")))
secondframe=Frame(Can1)
Can1.create_window((0,0),window=secondframe, anchor="nw")


#Border_Color

framemain=Frame(secondframe,highlightbackground="blue",highlightthickness=3, background="blue", borderwidth=10)
framemain.grid(row=0, column=0,padx=5,pady=5,columnspan=5)
framein=Frame(secondframe,width=20,highlightbackground="blue",highlightthickness=3)
framein.grid(row=5, column=0,pady=5, columnspan=2)
frameout=Frame(secondframe,width=20,highlightbackground="blue",highlightthickness=3)
frameout.grid(row=6, column=0,pady=5, columnspan=2)
frame2=Frame(secondframe,width=20,highlightbackground="blue",highlightthickness=3)
frame2.grid(row=4, column=0,pady=5, columnspan=5)
frame3=Frame(secondframe,width=42,highlightbackground="blue",highlightthickness=3, background="blue")
frame3.grid(row=9, column=0,columnspan=3, pady=5)






#Design
lmain=Label(framemain,text="Audio Precision",background="blue",fg="white",font=("Sans Serif",15,"bold"),width=24,height=8)
lmain.grid(row=0,column=0,columnspan=3)

#Tester
l1=Label(secondframe,text="Tester",background="blue",fg="white", width=18)
l1.grid(row=1,column=0)
tester=[1,2,3,4]
cmb=ttk.Combobox(secondframe,value=tester, width=18)
cmb.grid(row=2,column=0, pady=2)
#Project
l2=Label(secondframe,text="Project",background="blue",fg="white",width=18)
l2.grid(row=3,column=0)
project=["MMA","AUDI","ASTON MARTIN","VOLVO"]
cmb=ttk.Combobox(secondframe,value=project, width=18)
cmb.grid(row=4,column=0)
#Variant
l3=Label(secondframe,text="Variant",background="blue",fg="white",width=18)
l3.grid(row=3,column=2)
variant=["12D","8C","9F","4K"]
cmb=ttk.Combobox(secondframe,value=variant, width=18)
cmb.grid(row=4,column=2)
#EQ Type
l4=Label(secondframe,text="EQ Type",background="blue",fg="white",width=18)
l4.grid(row=3,column=4)
eqtype=["12D","8C","9F","4K"]
cmb=ttk.Combobox(secondframe,value=eqtype, width=18)
cmb.grid(row=4,column=4)
#Audio Input
lin=Label(framein,text="Audio Input",width=16,background="blue",fg="white")
lin.grid(row=5,column=0)
numbers1= Label(framein,text="Xnumber",bg="white",state=tk.NORMAL,width=10)
numbers1.grid(row=5,column=1)
#Number of Outputs
lout=Label(frameout,text="Number of Outputs",width=16,background="blue",fg="white")
lout.grid(row=6,column=0)
numbers2= Label(frameout,text="Xnumber",bg="white",state=tk.NORMAL,width=10)
numbers2.grid(row=6,column=1)
#Release type
l5=Label(secondframe,text="Release Type",background="blue",fg="white", width=18)
l5.grid(row=7,column=0)
Release=["CI","CR","Test"]
cmb=ttk.Combobox(secondframe,value=Release, width=18)
cmb.grid(row=8,column=0)




#Software version
sw=Label(frame3,text="Software Version:",width=17,background="blue",fg="white",justify=CENTER,anchor="center")
sw.grid(row=9,column=0)
swtext=Text(frame3,width=27,height=1)
swtext.grid(row=9,column=1)
clear_button=Button(secondframe,text="Clear", width=6,height=1,command=clear,bg="blue",fg="white")
clear_button.grid(row=9,column=3)
get_text_button=Button(secondframe,text="Get", width=6,height=1,command=get_text,bg="blue",fg="white")
get_text_button.grid(row=9,column=4)

#Golden Sample
GoldenSample=Checkbutton(secondframe,text="Golden Sample", bg="blue", fg="white",selectcolor="grey",width=15, anchor=W)
GoldenSample.grid(row=10,column=0)
#Browse

b1=tk.Button(secondframe,text="Browse", command=lambda:myplace(), bg="blue",fg="white")
b1.grid(row=10,column=1)
l1=Label(secondframe,text=mydir,bg="blue", fg="white",width=46)
l1.grid(row=10, column=2,columnspan=3, pady=5)

#Check Buttons
var=IntVar()
#Frequency
Frequency=Checkbutton(secondframe,text="Frequency response", bg="blue", fg="white",selectcolor="grey",width=15)
Frequency.grid(row=13,column=0,pady=5)
#Bass-Mid-Treble
BMT=Checkbutton(secondframe,text="BMT measurements",variable=var,state=NORMAL,bg="blue", fg="white",selectcolor="grey")
BMT.grid(row=14,column=0,pady=5)
BMTbutton=Button(secondframe,text="On/Off",command=add,bg="blue",fg="white")
BMTbutton.grid(row=14,column=1,pady=5)

BMT=Checkbutton(secondframe,text="BMT measurements",variable=var,state=NORMAL,bg="blue", fg="white",selectcolor="grey")
BMT.grid(row=14,column=0,pady=5)

#Balance Feder
Balance_Feder=Checkbutton(secondframe,text="Balance Feder",width=15,bg="blue", fg="white",selectcolor="grey",anchor=W)
Balance_Feder.grid(row=15,column=0,pady=5)
#THDn
THDn=Checkbutton(secondframe,text="THDn",width=15,bg="blue", fg="white",selectcolor="grey",anchor=W)
THDn.grid(row=16,column=0,pady=5)
#Limiter
Limiter=Checkbutton(secondframe,text="Limiter",width=15,bg="blue", fg="white",selectcolor="grey",anchor=W)
Limiter.grid(row=17,column=0, pady=5)
#Pulse_response
Pulse_response=Checkbutton(secondframe,text="Pulse response",width=15,bg="blue", fg="white",selectcolor="grey",anchor=W)
Pulse_response.grid(row=18,column=0,pady=5)
#Gain_Level
Gain_level=Checkbutton(secondframe,text="Gain level",width=15,bg="blue", fg="white",selectcolor="grey",anchor=W)
Gain_level.grid(row=19,column=0,pady=5)
#FFT
FFT=Checkbutton(secondframe,text="FFT",width=15,bg="blue", fg="white",selectcolor="grey",anchor=W)
FFT.grid(row=20,column=0,pady=5)
root.mainloop()
#ctrl-al meg lehet nézni miket tudsz beállitani egy hivatkozáson belül

# slideframe=Frame(root)
# slideframe.pack(fill=BOTH, expand=1)
# mycanvas=Canvas(slideframe)
# mycanvas.pack(side=LEFT, fill=BOTH, expand=1)
# myscrollbar=tk.Scrollbar(slideframe, orient=VERTICAL, command=mycanvas.yview)
# myscrollbar.pack(side=RIGHT, fill=Y)
# mycanvas.configure(yscrollcommand=myscrollbar)
# mycanvas.bind('<Configure>', lambda e:mycanvas.configure(scrollregion=mycanvas.bbox("all")))
# secondframe=Frame(mycanvas)
# mycanvas.create_window((f"{w}x{h}+100+100"), window=secondframe, anchor="nw")
