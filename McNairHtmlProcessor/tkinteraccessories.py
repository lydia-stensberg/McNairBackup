import tkinter as tk
from tkinter import messagebox




def are_you_sure():
    result = messagebox.askquestion("New File", "Are you sure you want to override the existing file"
                                       " and load a new one?", icon='warning')
    return result
