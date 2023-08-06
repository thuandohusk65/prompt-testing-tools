from tkinter import *
from tkinter import ttk
from tkinter.ttk import *


class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("Welcome to Test-Prompt Tools")
        # self.window.geometry('600x600')
        # Get screen width and height
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate 2/3 of the screen size
        width = 2 / 3 * screen_width
        height = 2 / 3 * screen_height

        # Set the window size
        self.window.geometry('%dx%d' % (width, height))

        # The frame for scrollable text fields
        self.text_field_frame = Frame(self.window)
        self.text_field_frame.pack(side=RIGHT, fill=BOTH, expand=1)

        # Scrollbar for the text field frame
        self.scrollbar = Scrollbar(self.text_field_frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # The canvas where text fields are going to be added
        self.canvas = Canvas(self.text_field_frame, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Configure the scrollbar to scroll the canvas
        self.scrollbar.config(command=self.canvas.yview)

        # This frame will contain the text fields
        self.inner_frame = Frame(self.canvas)

        # Add the inner frame to the canvas
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor='nw')

        # Add button to add text fields
        self.add_button = Button(self.window, text="Add Text Field", command=self.add_text_field)
        self.add_button.pack(side=LEFT)

        # Button at the bottom
        self.ok_button = Button(self.window, text="OK", command=self.ok_clicked)
        self.ok_button.pack(side=BOTTOM)

        # List to hold references to text field variables
        self.text_fields = []

    def old_add_text_field(self):
        # Create a frame for each text field group
        field_frame = Frame(self.inner_frame)
        field_frame.pack(fill=X)

        # Create Role label and entry
        role_label = Label(field_frame, text="Role:")
        role_label.pack()
        role_var = StringVar()
        role_entry = Entry(field_frame, textvariable=role_var)
        role_entry.pack()

        # Create Message label and entry
        message_label = Label(field_frame, text="Message:")
        message_label.pack()
        message_var = StringVar()
        message_entry = Entry(field_frame, textvariable=message_var)
        message_entry.pack()

        # Add to text_fields
        self.text_fields.append((role_var, message_var))

        # Update the scroll region of the canvas
        self.window.update()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def add_text_field(self):
        self.insert_text_field(len(self.text_fields))

    def insert_text_field(self, index):
        # Create a frame for each text field group
        field_frame = Frame(self.inner_frame)

        # Create Role label and entry
        role_label = Label(field_frame, text="Role:")
        role_label.grid(row=0, column=0)
        role_var = StringVar()
        role_combobox = ttk.Combobox(field_frame, textvariable=role_var, values=('assistant', 'user', 'system'))
        role_combobox.grid(row=0, column=1)

        # Create Message label and entry
        message_label = Label(field_frame, text="Message:")
        message_label.grid(row=0, column=2)
        message_text = Text(field_frame, width=60, height=5, wrap=WORD)
        message_text.grid(row=0, column=3, sticky="we")

        # Create a remove button
        remove_button = Button(field_frame, text="-", command=lambda: self.remove_field(field_frame))
        remove_button.grid(row=0, column=4)

        # Create an add button
        add_button = Button(field_frame, text="+", command=lambda: self.insert_text_field(index + 1))
        add_button.grid(row=0, column=5)

        # Configure the columns to adjust their sizes as the window is resized
        field_frame.columnconfigure(1, weight=1)  # for role_combobox
        field_frame.columnconfigure(3, weight=3)  # for message_text

        # Insert the new field_frame at the given index
        self.text_fields.insert(index, (role_var, message_text, field_frame))

        # Re-pack all frames in the correct order
        for i, (_, _, frame) in enumerate(self.text_fields):
            frame.grid(row=i, sticky="we")

        # Update the scroll region of the canvas
        self.window.update()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def remove_field(self, field_frame):
        # Find the field_frame in the text_fields list and remove it
        for i, (role_var, message_text, frame) in enumerate(self.text_fields):
            if frame == field_frame:
                frame.destroy()
                del self.text_fields[i]
                break

        # Re-pack remaining frames in the correct order
        for i, (_, _, frame) in enumerate(self.text_fields):
            frame.grid(row=i, sticky="we")

        # Update the scroll region of the canvas
        self.window.update()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def ok_clicked(self):
        for role_var, message_var, _ in self.text_fields:
            print(f"Role: {role_var.get()}, Message: {message_var.get()}")

    def run(self):
        self.window.mainloop()


app = App()
app.run()
