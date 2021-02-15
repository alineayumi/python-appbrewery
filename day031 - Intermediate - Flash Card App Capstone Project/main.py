from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
words_to_learn = df.to_dict(orient="records")
current_card = {}

# ---------- CREATE NEW FLASHCARDS ----------


def on_right_click():
    words_to_learn.remove(current_card)
    pandas.DataFrame(words_to_learn).to_csv("./data/words_to_learn.csv", index=False)
    generate_random_card()


def generate_random_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(card, image=front_card_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(card, image=back_card_img)


# ---------- UI SETUP ----------

# window
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")

card = canvas.create_image(400, 263, image=front_card_img)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_random_card)
right_button = Button(image=right_img, highlightthickness=0, command=on_right_click)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

generate_random_card()

window.mainloop()








