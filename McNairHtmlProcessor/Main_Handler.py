import tkinter as tk
import soupaccessories

def print_hello():
    print("Hello! Button Clicked!")

def write_slogan():
    print("Writing a slogan!")

root = tk.Tk()
frame = tk.Frame(root)
frame.grid()

welcome_message = "Welcome to the McNair HTML Editor! \n Please load in the HTML file you'd" \
                  "like to change first, \n then select a command."

tk.Label(root, text=welcome_message).grid(row=0,columnspan=2)
tk.Label(root, text="First Name").grid(row=1)
tk.Label(root, text="Last Name").grid(row=2)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=1, column=1)

entry2.grid(row=2, column=1)

delete_button = tk.Button(text="Delete Blank Buttons",fg = "blue", command = print_hello)

delete_button.grid(row = 3, column = 1)

show_buttons = tk.Button(text="Hello", command=write_slogan)

show_buttons.grid(row = 4, column = 1)
# Setting up the options menu
sample_var = tk.StringVar(root)
sample_var.set("Default Value")
button_select = tk.OptionMenu(root, sample_var,"one","two","three","four")
button_select.grid(column = 0, columnspan=2, row = 5)



root.mainloop()

