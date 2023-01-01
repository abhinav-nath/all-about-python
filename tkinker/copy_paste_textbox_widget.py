from tkinter import *


# Select all the text in textbox
def select_all(event):
    textbox.tag_add(SEL, "1.0", END)
    textbox.mark_set(INSERT, "1.0")
    textbox.see(INSERT)
    return 'break'


# Open a window
mainwin = Tk()

# Create a text widget
textbox = Text(mainwin, width=40, height=10)
textbox.pack()

# Add some text
textbox.insert(INSERT, "Select some text then right click in this window")

# Add the binding
textbox.bind("<Control-Key-a>", select_all)
textbox.bind("<Control-Key-A>", select_all)  # just in case caps lock is on

# Start the program
mainwin.mainloop()
