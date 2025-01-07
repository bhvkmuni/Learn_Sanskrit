from tkinter import *
import pandas
import random
from time import *
BACKGROUND_COLOR = "#B1DDC6"
#----------------------Pick Random Sanskrit Word----------------------#
df = pandas.read_csv("./data/sanskrit_words.csv")
to_learn = df.to_dict(orient="records")
master_dict = to_learn[:]


new_dictionary = {}
new_list = {}

def next_card(dict_io):
    reset_card()
    current_card = random.choice(dict_io)
    global new_dictionary, flip_timer
    window.after_cancel(flip_timer)
    new_dictionary = current_card
    dict_io.remove(current_card)
    new_df = pandas.DataFrame(dict_io)
    new_df.to_csv('words_to_learn.csv', mode="w", index=False)
    canvas.itemconfig(card_title, text ="Sanskrit", fill="black")
    canvas.itemconfig(card_word, text=current_card["Sanskrit"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def check_new_words():
    try:
        new_df = pandas.read_csv('words_to_learn.csv')
        words_to_learn = new_df.to_dict(orient="records")
    except NameError:
        next_card(to_learn)
    except FileNotFoundError:
        next_card(to_learn)
    else:
        next_card(words_to_learn)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(card_title, text ="English", fill="white")
    canvas.itemconfig(card_word, text=new_dictionary["English"], fill="white")

# ---------------------------- UPDATE LIST ---------------------------- #



def reset_card():
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(card_title, fill="black")
    canvas.itemconfig(card_word, fill="black")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

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
r_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=check_new_words)
r_button.grid(column=1, row=1)
wrong_image = PhotoImage(file="images/wrong.png")
w_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=check_new_words)
w_button.grid(column=0, row=1)




check_new_words()



window.mainloop()