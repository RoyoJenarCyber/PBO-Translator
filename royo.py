from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Create the root window
root = Tk()
root.title("Google Translator 2.0")
root.geometry("720x300")  # Reduced size
root.resizable(False, False)
root.configure(background="white")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    text_ = text1.get(1.0, END)
    t1 = Translator()
    # Get language codes instead of names
    src_lang = [key for key, value in LANGUAGES.items() if value == combo1.get()][0]
    dest_lang = [key for key, value in LANGUAGES.items() if value == combo2.get()][0]
    
    trans_text = t1.translate(text_, src=src_lang, dest=dest_lang)
    trans_text = trans_text.text

    text2.delete(1.0, END)
    text2.insert(END, trans_text)

# Icon
try:
    image_icon = PhotoImage(file="Google.png")
    root.iconphoto(False, image_icon)
except Exception as e:
    print("Error loading icon:", e)

# Arrow
try:
    arrow_image = PhotoImage(file="arrow.png")
    image_label = Label(root, image=arrow_image, width=100)  # Adjusted width
    image_label.place(x=310, y=-10)  # Adjusted position
except Exception as e:
    print("Error loading arrow image:", e)

# Language setup
language = LANGUAGES
languageV = list(language.values())

# First combobox
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 10", state="r")  # Smaller font
combo1.place(x=80, y=20)  # Adjusted position
combo1.set("english")

label1 = Label(root, text="ENGLISH", font="segoe 20 bold", bg="white", width=15, bd=5, relief=GROOVE)  # Smaller font and width
label1.place(x=10, y=5)

# Second combobox
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 10", state="r")  # Smaller font
combo2.place(x=530, y=20)  # Adjusted position
combo2.set("select language")

label2 = Label(root, text="SELECT LANGUAGE", font="segoe 20 bold", bg="white", width=15, bd=5, relief=GROOVE)  # Smaller font and width
label2.place(x=440, y=5)

# First frame
f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=80, width=320, height=150)  # Adjusted size and position

text1 = Text(f, font="Roboto 14", bg="white", relief=GROOVE, wrap=WORD)  # Smaller font
text1.place(x=0, y=0, width=310, height=140)  # Adjusted size

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Second frame
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=390, y=80, width=320, height=150)  # Adjusted size and position

text2 = Text(f1, font="Roboto 14", bg="white", relief=GROOVE, wrap=WORD)  # Smaller font
text2.place(x=0, y=0, width=310, height=140)  # Adjusted size

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, text="Translate", font=("Roboto", 10), activebackground="white", cursor="hand2",  # Smaller font
                   bd=1, width=10, height=2, bg="black", fg="white", command=translate_now)
translate.place(x=310, y=240)  # Adjusted position

label_change()

root.mainloop()