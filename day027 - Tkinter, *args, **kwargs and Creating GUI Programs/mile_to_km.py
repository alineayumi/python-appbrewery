from tkinter import *


def calculate():
    km_converted['text'] = f'{round(float(entry.get()) * 1.609343502101154)}'


window = Tk()
window.title('Miles to Km Converter')
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.insert(END, string='0')
entry.grid(row=0, column=1)

mile_text = Label(text='Miles')
mile_text.grid(row=0, column=2)

equal_to_text = Label(text='is equal to')
equal_to_text.grid(row=1, column=0)

km_converted = Label(text='0')
km_converted.grid(row=1, column=1)

km_text = Label(text='Km')
km_text.grid(row=1, column=2)

calc_button = Button(text='Calculate', command=calculate)
calc_button.grid(row=2, column=1)

window.mainloop()
