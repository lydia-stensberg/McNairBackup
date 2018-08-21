import tkinter as tk
from tkinter import ttk
import soupaccessories

def print_hello(): print("Hello! Button Clicked!")


def write_slogan(): print("Writing a slogan!")

def mycommand(): print("Chosen.")

root = tk.Tk()
root.title = "McNair HTML Editor"
frame = tk.Frame(root)
frame.grid()
welcome_message = "Please load in the HTML file you'd" \
                  "like to change first, \n then select a command."
tk.Label(root, text=welcome_message).grid(row=0,columnspan=2)


#We're trying out a tabbed notebook -may be better than a menu?
n = ttk.Notebook(root)
f1 = tk.Frame(n)   # first page, which would get widgets gridded into it
f2 = tk.Frame(n)   # second page
n.add(f1, text='Edit Top Buttons')
n.add(f2, text='Edit Side Buttons')
n.grid()


tk.Label(f1, text="Enter New Top Button Name").grid(row=1)
tk.Label(f2, text="Enter New Side Button Name").grid(row=2)

new_button_name = tk.StringVar()
new_button_entry = tk.Entry(f1, textvariable=new_button_name)
entry2 = tk.Entry(f2)

new_button_entry.grid(row=1, column=1)

entry2.grid(row=2, column=1)

#button to delete a button
delete_button = tk.Button(text="Delete Blank Buttons",fg = "blue", command = print_hello)
delete_button.grid(row = 3, column = 1)

#button to show all buttons
show_buttons = tk.Button(text="Show Existing Buttons", command=write_slogan)
show_buttons.grid(row = 4, column = 1)

# Button to load existing file
load_existing_file_button = tk.Button(text="Load Existing File", command=print_hello)
load_existing_file_button.grid(row=5, column=1)

#Setting up options menu
sample_var = tk.StringVar(root)
sample_var.set("Default Value")
choices = ["one","two","three","four"]
button_select = tk.Listbox(root)
for item in choices:
    button_select.insert(tk.END,item)
button_select.grid(column = 1, row = 6)

tk.Label(root,text="Pick a button to edit").grid(row=6,column=0)

#TODO Edit menu to include various commands: suggested list below
#1. Pick a new file to edit
#2. Top Button Edits
#2. Side Button edits
#3. Central Image edits

#Replace File Path Handler
menu_bar = tk.Menu(root)

top_button_menu = tk.Menu(menu_bar, tearoff=0)
top_button_menu.add_command(label="New", command=mycommand)
top_button_menu.add_command(label="Clone", command=mycommand)
top_button_menu.add_separator()
top_button_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="Edit Top Buttons", menu=top_button_menu)

side_button_menu = tk.Menu(menu_bar, tearoff=0)
side_button_menu.add_command(label="Oval", command=mycommand)
side_button_menu.add_command(label="Rectangle", command=mycommand)
menu_bar.add_cascade(label="Edit Side Buttons", menu=side_button_menu)

root.config(menu=menu_bar)






root.mainloop()

