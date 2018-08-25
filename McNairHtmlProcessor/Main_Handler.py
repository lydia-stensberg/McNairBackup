import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import soupaccessories

"""General Notes"""
"""No error-handling takes place in this file. All error-handling happens in underlying methods."""

#Button Methods

def load_comparative_file():
    global base_soup
    if base_soup is not None:
        base_soup.open_comparative_file()
    else:
        print("Soup is None")
        pass

class SoupInterface(tk.Tk):

    base_soup = None
    button1_frame = None
    button2_frame = None
    button3_frame = None
    button1_select = None
    button2_select = None
    button3_select = None
    selected_button = ""
    new_button1_label = None
    new_button2_label = None
    new_button3_label = None

    def save_new_file(self):
        if self.base_soup is not None:
            self.base_soup.write_output(False)
        else:
            print("Soup is none")
            pass

    def overwrite_file(self):
        if self.base_soup is not None:
            self.base_soup.write_output(True)
        else:
            print("Soup is none")
            pass

    def update_first_buttons(self):
        self.button1_select.delete(0,tk.END)
        button_list = self.base_soup.first_buttons()
        soupaccessories.write_list_output(button_list)
        for item in button_list:
            self.button1_select.insert(tk.END, item.string)
        self.button1_select.update()
        return

    def update_second_buttons(self):
        self.button2_select.delete(0,tk.END)
        button_list = self.base_soup.second_buttons()
        for item in button_list:
            self.button2_select.insert(tk.END, item.string)
        self.button2_select.update()

    def update_third_buttons(self):
        self.button3_select.delete(0,tk.END)
        button_list = self.base_soup.third_buttons()
        for item in button_list:
            self.button3_select.insert(tk.END, item.string)
        self.button3_select.update()

    def initialize_soup(self):
        self.base_soup = soupaccessories.SoupHandler()
        self.update_first_buttons()
        self.update_second_buttons()
        self.update_third_buttons()
        print("Chosen.")


    def change_button1_name(self):
        self.base_soup.change_first_button_name(button_name=self.selected_button,
                                                 new_button_name=self.new_button1_label.get())
        self.update_first_buttons()
        return

    def change_button2_name(self):
        self.base_soup.change_second_button_name(button_name=self.selected_button,
                                                 new_button_name=self.new_button2_label.get())
        self.update_second_buttons()
        return

    def change_button3_name(self):
        self.base_soup.change_third_button_name(button_name=self.selected_button,
                                                 new_button_name=self.new_button3_label.get())
        self.update_third_buttons()
        return

    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        self.selected_button = widget.get(selection[0])
        print("selection:", selection, ": '%s'" % self.selected_button)


    def delete_blanks(self):
        if self.base_soup is not None:
            self.base_soup.remove_blank_buttons()
            self.update_first_buttons()
        else:
            pass


    # Method to add identical buttons to the top and side button frames
    def add_required_buttons(self, tkinter_frame):
        # button to delete a button
        delete_button = tk.Button(tkinter_frame, text="Delete Blank Buttons", fg="blue",
                                  command=self.delete_blanks)
        delete_button.grid(row=3, column=1)



        return


    def __init__(self):
        #Set up interface root and frame
        tk.Tk.__init__(self,className="McNair HTML Editor")
        self.title = "McNair HTML Editor"
        frame = tk.Frame(self)
        frame.grid()
        welcome_message = "Please use the File Menu to load in the HTML file you'd \n" \
                      "like to change first, then select a command."
        tk.Label(self, text=welcome_message).grid(row=0,columnspan=2)

        # Set up notebooks for top menu buttons, side menu buttons, and Images on page
        notebook = ttk.Notebook(self)
        self.button1_frame = tk.Frame(notebook)  # first button page, which would get widgets gridded into it
        self.button2_frame = tk.Frame(notebook)  # second  button page
        self.button3_frame = tk.Frame(notebook)  # third button page
        notebook.add(self.button1_frame, text='Edit Button1')
        notebook.add(self.button2_frame, text='Edit Button2')
        notebook.add(self.button3_frame, text='Edit Button3')
        notebook.grid()

        # Setting up button1
        tk.Label(self.button1_frame, text="Enter New Name").grid(row=1)
        new_button_name = tk.StringVar()
        self.new_button1_label = tk.Entry(self.button1_frame, textvariable=new_button_name)
        self.new_button1_label.grid(row=1, column=1)


        # Setting up button2 frame
        tk.Label(self.button2_frame, text="Enter New Name").grid(row=2)
        self.new_button2_label = tk.Entry(self.button2_frame)
        self.new_button2_label.grid(row=2, column=1)

        # Setting up button3 grams
        tk.Label(self.button3_frame, text="Enter New Name").grid(row=2)
        self.new_button3_label = tk.Entry(self.button3_frame)
        self.new_button3_label.grid(row=2, column=1)

        # Setting up options menu
        sample_var = tk.StringVar(self.button1_frame)
        sample_var.set("Default Value")
        choices = ["one", "two", "three", "four"]
        self.button1_select = tk.Listbox(self.button1_frame)
        for item in choices: self.button1_select.insert(tk.END, item)
        self.button1_select.grid(column=1, row=6)
        tk.Label(self.button1_frame, text="Pick a button to edit").grid(row=6, column=0)
        self.button1_select.bind('<<ListboxSelect>>', self.OnDouble)
        self.button1_select.bind("<Double-Button-1>", self.OnDouble)

        # Setting up options menu
        sample_var = tk.StringVar(self.button2_frame)
        sample_var.set("Default Value")
        choices = ["one", "two", "three", "four"]
        self.button2_select = tk.Listbox(self.button2_frame)
        for item in choices: self.button2_select.insert(tk.END, item)
        self.button2_select.grid(column=1, row=6)
        tk.Label(self.button2_frame, text="Pick a button to edit").grid(row=6, column=0)
        self.button2_select.bind('<<ListboxSelect>>', self.OnDouble)
        self.button2_select.bind("<Double-Button-1>", self.OnDouble)

        # Setting up options menu
        sample_var = tk.StringVar(self.button3_frame)
        sample_var.set("Default Value")
        choices = ["one", "two", "three", "four"]
        self.button3_select = tk.Listbox(self.button3_frame)
        for item in choices: self.button3_select.insert(tk.END, item)
        self.button3_select.grid(column=1, row=6)
        tk.Label(self.button2_frame, text="Pick a button to edit").grid(row=6, column=0)
        self.button3_select.bind('<<ListboxSelect>>', self.OnDouble)
        self.button3_select.bind("<Double-Button-1>", self.OnDouble)

        #adding button1 label change
        # button to change a button's name
        change_button1 = tk.Button(self.button1_frame, text="Change Button Text", fg="blue",
                                  command=self.change_button1_name)
        change_button1.grid(row=4, column=1)

        # button to change button2 name
        change_button2 = tk.Button(self.button2_frame, text="Change Button Text", fg="blue",
                                  command=self.change_button2_name)
        change_button2.grid(row=4, column=1)

        # button to change button2 name
        change_button3 = tk.Button(self.button3_frame, text="Change Button Text", fg="blue",
                                  command=self.change_button3_name)
        change_button3.grid(row=4, column=1)

        self.add_required_buttons(self.button2_frame)
        self.add_required_buttons(self.button1_frame)
        self.add_required_buttons(self.button3_frame)

        # TODO Edit menu to include various commands: suggested list below
        # 1. Pick a new file to edit
        # 2. Top Button Edits
        # 2. Side Button edits
        # 3. Central Image edits

        # Replace File Path Handler
        menu_bar = tk.Menu(self)

        top_button_menu = tk.Menu(menu_bar, tearoff=0)
        initialize_command = top_button_menu.add_command(label="Load Existing File", command=self.initialize_soup)
        top_button_menu.add_command(label="Save New File", command=self.save_new_file)
        top_button_menu.add_command(label="Overwrite Existing File", command=self.overwrite_file)
        top_button_menu.add_separator()
        top_button_menu.add_command(label="Reset Program", command=self.quit)
        menu_bar.add_cascade(label="File Menu", menu=top_button_menu)

        # Use to load second file to compare to first file.
        side_button_menu = tk.Menu(menu_bar, tearoff=0)
        side_button_menu.add_command(label="Load New File", command=load_comparative_file)
        menu_bar.add_cascade(label="Compare Loaded File to New File", menu=side_button_menu)

        # TODO bind event to update choice list once file is loaded
        # initialize_command.bind('<Button-1>',)

        self.config(menu=menu_bar)


if __name__ == '__main__':
    app = SoupInterface()
    app.mainloop()





