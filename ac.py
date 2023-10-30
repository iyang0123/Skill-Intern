from textblob import TextBlob
from tkinter import *
def checkSpelling():
    a = text.get()
    b = TextBlob(a)
    correctedText.set("The corrected word is: "+str(b.correct()))
wn = Tk() 
wn.title("DataFlair Spell Checker")
wn.geometry('500x250')
wn.config(bg='SlateGray1')
text=StringVar(wn)
correctedText =StringVar(wn)
Label(wn, text='DataFlair Spell Checker',bg='SlateGray1',
  fg='gray30', font=('Times', 20,'bold')).place(x=100, y=10)
#Getting the input of word from the user
Label(wn, text='Please enter the word',bg='SlateGray1',font=('calibre',13,'normal'), anchor="e", justify=LEFT).place(x=20, y=70)
Entry(wn,textvariable=text, width=35,font=('calibre',13,'normal')).place(x=20,y=110)
#Label to show the correct word
opLabel = Label(wn, textvariable=correctedText, bg='SlateGray1',anchor="e",font=('calibre',13,'normal'), justify=LEFT).place(x=20, y=130)
Button(wn, text="Click Me", bg='SlateGray4',font=('calibre', 13),
   command=checkSpelling).place(x=230, y=190)
wn.mainloop()