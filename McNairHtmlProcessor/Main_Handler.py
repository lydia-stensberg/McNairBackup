import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import soupaccessories
import Error_Handler

"""General Notes"""
"""No error-handling takes place in this file. All error-handling happens in underlying methods."""


#Set up interface root and frame
root = tk.Tk(className="McNair HTML Editor")
root.title = "McNair HTML Editor"
frame = tk.Frame(root)
frame.grid()
welcome_message = "Please use the File Menu to load in the HTML file you'd \n" \
                  "like to change first, then select a command."
tk.Label(root, text=welcome_message).grid(row=0,columnspan=2)

base_soup = None

#Button Methods
def print_hello(): print("Hello! Button Clicked!")

def write_slogan(): print("Writing a slogan!")

def load_comparative_file():
    global base_soup
    if base_soup is not None:
        base_soup.open_comparative_file()
    else:
        print("Soup is None")
        pass

def save_new_file():
    global base_soup
    if base_soup is not None:
        base_soup.write_output(False)
    else:
        print("Soup is none")
        pass

def overwrite_file():
    global base_soup
    if base_soup is not None:
        base_soup.write_output(True)
    else:
        print("Soup is none")
        pass

def initialize_soup():
    global base_soup
    base_soup = soupaccessories.Soup_Handler()
    print("Chosen.")


def update_choices():
    print("Choices are updated")
    global base_soup

    pass

#Method to add identical buttons to the top and side button frames
def add_required_buttons(tkinter_frame):
    # button to delete a button
    delete_button = tk.Button(tkinter_frame,text="Delete Blank Buttons", fg="blue", command=print_hello)
    delete_button.grid(row=3, column=1)

    # button to show all buttons
    show_buttons = tk.Button(tkinter_frame, text="Show Existing Buttons", command=write_slogan)
    show_buttons.grid(row=4, column=1)

    # Setting up options menu
    sample_var = tk.StringVar(tkinter_frame)
    sample_var.set("Default Value")
    choices = ["one", "two", "three", "four"]
    button_select = tk.Listbox(tkinter_frame)
    for item in choices: button_select.insert(tk.END, item)
    button_select.grid(column=1, row=6)
    tk.Label(tkinter_frame, text="Pick a button to edit").grid(row=6, column=0)


    return





#Set up notebooks for top menu buttons, side menu buttons, and Images on page
notebook = ttk.Notebook(root)
top_button_frame = tk.Frame(notebook)   # first page, which would get widgets gridded into it
side_button_frame = tk.Frame(notebook)   # second page
notebook.add(top_button_frame, text='Edit Top Buttons')
notebook.add(side_button_frame, text='Edit Side Buttons')
notebook.grid()

#Setting up top button frame notebook
tk.Label(top_button_frame, text="Enter New Top Button Name").grid(row=1)
new_button_name = tk.StringVar()
new_button_entry = tk.Entry(top_button_frame, textvariable=new_button_name)
new_button_entry.grid(row=1, column=1)

#Setting up side button frame notebook
tk.Label(side_button_frame, text="Enter New Side Button Name").grid(row=2)
entry2 = tk.Entry(side_button_frame)
entry2.grid(row=2, column=1)

add_required_buttons(side_button_frame)
add_required_buttons(top_button_frame)

#TODO Edit menu to include various commands: suggested list below
#1. Pick a new file to edit
#2. Top Button Edits
#2. Side Button edits
#3. Central Image edits

#Replace File Path Handler
menu_bar = tk.Menu(root)

top_button_menu = tk.Menu(menu_bar, tearoff=0)
initialize_command = top_button_menu.add_command(label="Load Existing File", command=initialize_soup)
top_button_menu.add_command(label="Save New File", command=save_new_file)
top_button_menu.add_command(label="Overwrite Existing File", command=overwrite_file)
top_button_menu.add_separator()
top_button_menu.add_command(label="Reset Program", command=root.quit)
menu_bar.add_cascade(label="File Menu", menu=top_button_menu)

#Use to load second file to compare to first file.
side_button_menu = tk.Menu(menu_bar, tearoff=0)
side_button_menu.add_command(label="Load New File", command=load_comparative_file)
side_button_menu.add_command(label="Rectangle", command=print_hello)
menu_bar.add_cascade(label="Compare Loaded File to New File", menu=side_button_menu)

#TODO bind event to update choice list once file is loaded
initialize_command.bind('<Button-1>',)


root.config(menu=menu_bar)

root.mainloop()

