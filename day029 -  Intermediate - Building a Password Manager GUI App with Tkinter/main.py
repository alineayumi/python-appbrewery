from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password_gen = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password_gen)
    pyperclip.copy(password_gen)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(message="Please don't leave any fields empty!", title="Oops!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ------------------------- FIND PASSWORD ----------------------------- #


def find_password():
    try:
        with open("data.json", "r") as data_file:
            # reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message=f"No Data File Found", title="Oops!")
    else:
        website = website_entry.get()
        if website in data:
            search_data = data[website]
            email = search_data["email"]
            password = search_data["password"]
            messagebox.showinfo(message=f"Email: {email} \nPassword: {password}", title=website)
        else:
            messagebox.showinfo(message=f"No details for {website} exists", title="Oops!")

    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

#  window setup
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

#  canvas setup
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#  Labels setup
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

#  Entries setup
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "aline@email.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#  Buttons setup
gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

#  keep window alive
window.mainloop()
