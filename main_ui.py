"""
---------------------------------------------
  File Name:    main_ui
  Description:  Create a simple GUI of python based on tkinter(sudo apt-get install python3-tk)
  Author:       nycolas
  Date:         18-3-18
---------------------------------------------

"""

from tkinter import *


class MachineJokes(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.setup_label = Label(self)
        self.setup_label["text"] = "Input Set-up: "
        self.setup_label.grid(row=0, sticky=W)

        self.setup_entry = Entry(self, width=50)
        self.setup_entry.grid(row=1, column=0, stick=W)

        self.generation_button = Button(self, width=10)
        self.generation_button["text"] = "Generation"
        self.generation_button["command"] = self.generation_punchline
        self.generation_button.grid(row=1, column=1, sticky=W)

        self.punchline_label = Label(self)
        self.punchline_label["text"] = "Output Punch-line: "
        self.punchline_label.grid(row=2, sticky=W)

        self.punchline_text = Text(self, width=50, height=5, wrap=WORD)
        self.punchline_text.grid(row=3, column=0, columnspan=2, sticky=W)

        self.quit_button = Button(self, width=10)
        self.quit_button["text"] = "Quit"
        self.quit_button["fg"] = "red"
        self.quit_button["command"] = self.quit
        self.quit_button.grid(row=3, column=1, sticky=W)

    def generation_punchline(self):
        context = self.setup_entry.get()
        if context == "hello":
            message = "confirm"
        else:
            message = "sorry"
        self.punchline_text.delete(0.0, END)
        self.punchline_text.insert(0.0, message)


root = Tk()
root.title("Password")
root.geometry('460x170')
app = MachineJokes(root)
app.mainloop()
root.destroy()

