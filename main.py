from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
# timer = None

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_record = original_data.to_dict(orient="records")
else:
    words_record = data.to_dict(orient="records")


def new_card():
    global current_word, timer
    window.after_cancel(timer)
    current_word = random.choice(words_record)
    canvas.itemconfig(current_image, image=front_image)
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=current_word["French"])
    timer = window.after(3000, func=flip_card)


def flip_card():

    canvas.itemconfig(current_image, image=back_image)
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=current_word["English"])


def save_progress():
    words_record.remove(current_word)
    word_frame = pandas.DataFrame(words_record)
    word_frame.to_csv("data/words_to_learn.csv")
    new_card()

window = Tk()
window.title("Flash card App")
window.minsize(width=900, height=900)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# front_image = PhotoImage(file="images/card_front.png")

back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
current_image = canvas.create_image(400, 270, image=front_image)
language_text = canvas.create_text(400, 200, text="", fill="black", font=("Arial", 12))
word_text = canvas.create_text(400, 250, text="", fill="black", font=("Arial", 35, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


wrong_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, command=new_card)
wrong_btn.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_image, highlightthickness=0, command=save_progress)
right_btn.grid(column=1, row=1)

new_card()

window.mainloop()

