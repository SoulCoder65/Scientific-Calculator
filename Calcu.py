from tkinter import *
from tkinter.messagebox import showerror
import pyttsx3 #FOR VOICE
import speech_recognition as sr
import math as ma

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',b'\x02en-gb')

#FUN FOR SPEAK
def button_sound(audio):
    engine.say(audio)
    engine.runAndWait()
# FONT
font_title=('verdana',22,'bold')
font=('verdana',15,'bold')

def voice_btn(event):
    text_wid=event.widget
    text=text_wid['text']
    print(text)
    button_sound(text)
# SCREEN LOOK
Screen=Tk()
Screen.title("Scientific Calculator")
pic=PhotoImage(file='images/Calculator-icon.png')
heading_label=Label(Screen,image=pic)
heading_label.pack(side=TOP,pady=15)
heading_text=Label(Screen,text='My Calculator',font=font_title)
heading_text.pack(side=TOP,pady=10)

# TEXTAREA FOR INPUT AND BUTTONS
text_input=Entry(Screen,font=font_title,justify=CENTER)
text_input.pack(side=TOP,pady=10,padx=5)
frame_button=Frame(Screen)

# FUNCTION FOR CLEARING SCREEN
def all_clear_fun():
    text_input.delete(0,END)
def clear_fun():
    new_text=text_input.get()
    text_input.delete(0,END)
    text_input.insert(END,new_text[0:len(new_text)-1])

# FUNCTION FOR PERFORMING EVENT WHEN USER CLICK ON BUTTON
def button_click(event):
    but_text=event.widget
    text=but_text['text']
    if text=="%":
        button_sound("Divide")
    else:
        button_sound(text)
    try:
        if text=="AC":
            all_clear_fun()
        elif text=="CLEAR":
            clear_fun()
        elif text=="=":
            string_result=text_input.get()
            result=eval(string_result)
            button_sound(str(result))
            text_input.delete(0,END)
            text_input.insert(END,result)
        else:
            text_input.insert(END,text)
        if text=="X":
            clear_fun()
            text_input.insert(END,"*")
        if text == "^":
            clear_fun()
            text_input.insert(END, "**")

    except Exception as e:
        showerror("Expression Error","Please Write Logical Expression")
def SciClick(event):
    data=text_input.get()
    but_text=event.widget
    text=but_text['text']
    button_sound(text)
    if text=="ToRad":
        result=ma.radians(float(data))
    elif text=="ToDeg":
        result=ma.degrees(float(data))
    elif text=="√":
        result=ma.sqrt(float(data))
    elif text=="Sinθ":
        result=ma.sin(ma.radians(int(data)))
    elif text == "Cosθ":
        result = ma.cos(ma.radians(int(data)))
    elif text == "Tanθ":
        result = ma.tan(ma.radians(int(data)))
    elif text=="X!":
        result=ma.factorial(int(data))
    text_input.delete(0,END)
    text_input.insert(END,str(result))


toggle=TRUE
def Toggle_fun():
    global toggle
    if toggle==FALSE:
        frame_button.pack_forget()
        sciFrame.pack(side=TOP,pady=10)
        frame_button.pack(side=TOP)
        toggle=True
        Screen.geometry("350x550")

        print("ON")
    else:
        sciFrame.pack_forget()
        frame_button.pack(side=TOP)
        toggle=False
        print("OFF")
        Screen.geometry("350x500")


# LOGIC FOR DISPLAYING BUTTON FROM 1-9
no_counter=1
for i in range(0,3):
    for j in range(0,3):
        button=Button(frame_button,text=str(no_counter),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
        button.grid(row=i,column=j,pady=1)
        no_counter+=1
        button.bind('<Button-1>',button_click)
dot_buttton=Button(frame_button,text=str("."),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
zero_button=Button(frame_button,text=str("0"),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
clear_button=Button(frame_button,text=str("CLEAR"),font=font,width=10,relief='solid',activebackground='blue',activeforeground='white')
equal_button=Button(frame_button,text=str("="),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
add_button=Button(frame_button,text=str("+"),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
minus_button=Button(frame_button,text=str("-"),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
multiply_button=Button(frame_button,text=str("X"),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
divide_button=Button(frame_button,text=str("%"),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
all_clear_button=Button(frame_button,text=str("AC"),font=font,width=10,relief='solid',activebackground='blue',activeforeground='white')

# APPLY GRID TO BUTTONS
zero_button.grid(row=3,column=0)
dot_buttton.grid(row=3,column=1)
clear_button.grid(row=4,column=0,columnspan=2)
equal_button.grid(row=3,column=2)
add_button.grid(row=0,column=3)
minus_button.grid(row=1,column=3)
multiply_button.grid(row=2,column=3)
divide_button.grid(row=3,column=3)
all_clear_button.grid(row=4,column=2,columnspan=2)

# BINDING OF BUTTONS
zero_button.bind('<Button-1>', button_click)
dot_buttton.bind('<Button-1>', button_click)
clear_button.bind('<Button-1>', button_click)
equal_button.bind('<Button-1>', button_click)
add_button.bind('<Button-1>', button_click)
minus_button.bind('<Button-1>', button_click)
multiply_button.bind('<Button-1>', button_click)
divide_button.bind('<Button-1>', button_click)
all_clear_button.bind('<Button-1>', button_click)

# SCIENTIFIC Button
sciFrame=Frame(Screen)

sqrt_button=Button(sciFrame,text=str("√"),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
fact_button=Button(sciFrame,text=str("X!"),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
rad_button=Button(sciFrame,text=str("ToRad"),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
deg_button=Button(sciFrame,text=str("ToDeg"),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
sin_button=Button(sciFrame,text=str("Sinθ"),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
cos_button=Button(sciFrame,text=str("Cosθ"),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
tan_button=Button(sciFrame,text=str("Tanθ"),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
pie_button=Button(sciFrame,text=str("π"),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')
pow_button=Button(sciFrame,text=str("^"),font=font,width=4,relief='solid',activebackground='blue',activeforeground='white')

# BUTTTONS GRID(SCIENTIFIC)
sqrt_button.grid(row=0,column=0,pady=1)
fact_button.grid(row=0,column=1,pady=1)
rad_button.grid(row=0,column=2,pady=1)
deg_button.grid(row=0,column=3,pady=1)
sin_button.grid(row=1,column=0,pady=1)
cos_button.grid(row=1,column=1,pady=1)
tan_button.grid(row=1,column=2,pady=1)
#pie_button.grid(row=2,column=1,pady=1)
pow_button.grid(row=1,column=3,pady=1)

# BUTTTONS BIND(SCIENTIFIC)
sqrt_button.bind('<Button-1>',SciClick)
fact_button.bind('<Button-1>',SciClick)
rad_button.bind('<Button-1>',SciClick)
deg_button.bind('<Button-1>',SciClick)
sin_button.bind('<Button-1>',SciClick)
cos_button.bind('<Button-1>',SciClick)
tan_button.bind('<Button-1>',SciClick)
pie_button.bind('<Button-1>',SciClick)
pow_button.bind('<Button-1>',button_click)

# SCIENTIFIC MODE
fontmenu=('',10)
menu=Menu(Screen,font=font)
mode=Menu(menu,font=fontmenu,tearoff=0)
mode.add_checkbutton(label="Scientific",command=Toggle_fun)
menu.add_cascade(label="Mode",menu=mode)
Screen.config(menu=menu)
Toggle_fun()
Screen.mainloop()