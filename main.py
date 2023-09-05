import random
from tkinter import *

import pandas
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
FONT_BIG = ("Times New Roman", 36, "bold")
FONT_SMALL = ("Times New Roman", 20, "bold")

try:
    words = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("./data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn = words.to_dict(orient="records")
select_word ={}
def next_card():
    global select_word,flip_timer
    window.after_cancel(flip_timer)
    select_word = random.choice(to_learn)
    canvas.itemconfig(my_words, text=select_word["French"],fill="black")
    canvas.itemconfig(languages, text="French",fill="black")
    canvas.itemconfig(card_background,image=front_image)
    flip_timer=window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(languages,text="English",fill="white")
    canvas.itemconfig(my_words,text=select_word["English"],fill="white")
    canvas.itemconfig(card_background,image=back_card)
def is_known():
    to_learn.remove(select_word)
    data=pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv",index=False)


    next_card()

window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=50)
flip_timer=window.after(3000,func=flip_card)
front_image = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
canvas = Canvas(height=526, width=800)
card_background=canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
languages = canvas.create_text(400, 100, text="", font=FONT_SMALL)
my_words = canvas.create_text(400, 250, text="", font=FONT_BIG)

canvas.grid(column=0, row=0, columnspan=2)
right_image = PhotoImage(file="./images/right.png/")
check_button = Button(image=right_image,command=is_known, highlightthickness=0, highlightcolor=BACKGROUND_COLOR)
check_button.grid(column=1, row=1)
left_image = PhotoImage(file="./images/wrong.png/")
wrong_button = Button(image=left_image,command=next_card, highlightthickness=0, highlightcolor=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)




next_card()
window.mainloop()
