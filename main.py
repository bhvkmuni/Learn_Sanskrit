from tkinter import *
import pandas
import random
from time import *
BACKGROUND_COLOR = "#B1DDC6"
#----------------------Pick Random Sanskrit Word----------------------#
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("./data/sanskrit_words.csv")
finally:
    to_learn = df.to_dict(orient="records")
    master_dict = to_learn[:]
    current_card = {}

def next_card():
    global current_card, flip
    window.after_cancel(flip)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Sanskrit", fill="black")
    canvas.itemconfig(card_word, text=current_card["Sanskrit"], fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip = window.after(3000, flip_card)
    print(len(to_learn))

def remove_word():
    global to_learn
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip = window.after(3000, flip_card)

#Front and Back Image:
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

#Buttons
right_image = PhotoImage(file="images/right.png")
r_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_word)
r_button.grid(column=1, row=1)
wrong_image = PhotoImage(file="images/wrong.png")
w_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
w_button.grid(column=0, row=1)


next_card()


window.mainloop()
