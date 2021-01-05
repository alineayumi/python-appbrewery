import tkinter


def button_clicked():
    my_label['text'] = inputText.get()


window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text='I am a label', font=('Arial', 24))
my_label['text'] = 'New Text'
my_label.config(text='Label')
my_label.config(padx=20, pady=20)
my_label.grid(column=0, row=0)

# Button

button = tkinter.Button(text='Button', command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text='New Button', command=button_clicked)
new_button.grid(column=2, row=0)

# Entry

inputText = tkinter.Entry(width=10)
inputText.grid(column=4, row=3)
# inputText.pack()

window.mainloop()
