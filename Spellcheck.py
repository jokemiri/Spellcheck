import tkinter
from tkinter import *
from spellchecker import SpellChecker

root = Tk()
root.title("Spell Check")
root.geometry("700x400")
root.configure(bg='#326273') #background
spell = SpellChecker()

#main window logo
logo = PhotoImage(file='logo.png')
Label(root, image=logo, bg='#326273').place(x=5, y=0)

#main window icon
main_window_icon = PhotoImage(file='icon.png')
root.iconphoto(False, main_window_icon)



def spellchack():
    check_word = text_entry.get()
    test_word = spell.candidates(check_word)
    # right = str(test_word.correct)
    # wrong = str(a.incorrect)

    correct_spelling = Label(root, text=f'Did you mean: {test_word}', font=('Verdana', 16), wraplength=300, justify=LEFT, bg='#326273', fg='white')
    correct_spelling.place(x=10, y=250)
 
    
heading = Label(root, text="Spellcheck", font=("Saint Carell PERSONAL", 30, "bold"), bg='#326273')
heading.pack(pady=(50,0))

text_entry = Entry(root, justify='center', width=30, font=('Verdana', 16), bg='#326273', border=1)
text_entry.place(x= 150, y=150)
text_entry.focus()

check_button = Button(root, text='Check', font=('Verdana', 16), fg='#dae6f6', bg='#326273', command=spellchack)
check_button.place(x=300, y=200)

clear_button = Button(root, text='Clear', font=('Verdana', 16), fg='#dae6f6', bg='#326273', command=clear)
clear_button.place(x=300, y=200)

spells = Label(root, font=('Verdana', 16), bg='#326273', fg='#dae6f6')
spells.place(x= 100, y=300)
root.mainloop()