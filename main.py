from tkinter import *
import pyttsx3

root = Tk()
root.title("Text to speech")
root.geometry("400x300+400+200")
root.resizable(False, False)

var_txt = StringVar()
engine = pyttsx3.init()

# rate = engine.getProperty('rate')
# engine.setProperty('rate', 120)
#
# volume = engine.getProperty('volume')
# engine.setProperty('volume', 0.5)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

lbl_frame = LabelFrame(root, text="Text to speech", font=20, bd=2)
lbl_frame.pack(fill="both", expand='yes', padx=20, pady=20)

rate_lbl = Label(lbl_frame, text="Rate", font=("goudy old style", 15))
rate_lbl.place(x=10, y=100)

rate_slider = Scale(lbl_frame, from_=0, to=200, orient=HORIZONTAL)
rate_slider.place(x=58, y=85)
rate_slider.set('100')

vol_lbl = Label(lbl_frame, text="Volume", font=("goudy old style", 15))
vol_lbl.place(x=180, y=100)

vol_slider = Scale(lbl_frame, from_=0, to=1, tickinterval=0.1, orient=HORIZONTAL)
vol_slider.place(x=250, y=85)
vol_slider.set('1')

voice = StringVar()
male_button = Radiobutton(lbl_frame, text="Male", variable=voice, value=0)
male_button.place(x=10, y=170)

female_button = Radiobutton(lbl_frame, text="Female", variable=voice, value=1)
female_button.place(x=10, y=190)
voice.set('1')


def change_rate():
    engine.setProperty('rate', rate_slider.get())


def change_vol():
    engine.setProperty('volume', vol_slider.get())


def change_voice():
    engine.setProperty('voice', voices[int(voice.get())].id)


lbl_text = Label(lbl_frame, text="Text:", font=("verdana", 13, "bold"))
lbl_text.place(x=10, y=50)

entry_text = Entry(lbl_frame, textvariable=var_txt, font=("verdana", 12), bd=1)
entry_text.place(x=65, y=53)


def speak():
    engine.say(var_txt.get())
    engine.runAndWait()
    engine.stop()
    var_txt.set("")


btn_speak = Button(lbl_frame, text="Speak", bg="green", fg="white", command=speak)
btn_speak.place(x=285, y=52)

btn_rate = Button(lbl_frame, text="Change rate", bg="red", fg="white", command=change_rate)
btn_rate.place(x=40, y=135)

btn_rate = Button(lbl_frame, text="Change volume", bg="red", fg="white", command=change_vol)
btn_rate.place(x=230, y=135)

btn_voice = Button(lbl_frame, text="Change voice", bg="blue", fg="white", command=change_voice)
btn_voice.place(x=10, y=210)

root.mainloop()
