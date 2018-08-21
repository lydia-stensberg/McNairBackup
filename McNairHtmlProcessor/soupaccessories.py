from bs4 import BeautifulSoup
import re
import tkinter
from tkinter import filedialog

def open_existing_file(args):
    file_path = vars(args)
    my_file = open(file_path['File Path'],'r')
    return my_file

def open_with_filepath(file_path):
    my_file = open(file_path,'r')
    return my_file

def get_side_buttons():
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    file = open_with_filepath(file_path)
    soup = BeautifulSoup(file, "html.parser")
    side_button_names = []
    side_buttons = side_menu_buttons(soup)
    for button in side_buttons:
        side_button_names.append(button.string)
    return {'Side Button Names': side_button_names,'Side Buttons': side_buttons}

def has_class(css_class):
    return css_class is not None

def has_class_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

def side_menu_buttons(soup):
    return soup.find_all(class_="Button2")

def top_menu_buttons(soup):
    return soup.find_all(class_="Button3")

def has_file(href):
    return href is not None and re.compile("Files").search(href)

def write_output(list):
    print('\n'.join('{}:{}'.format(*k) for k in enumerate(list)))

def get_blanks(tag):
    return tag.string=="Blank"

def find_button_by_tag(soup, old_name):
    return soup.find_all(string=old_name)

def get_blank_buttons(soup):
    buttons =soup.find_all(get_blanks)
    blank_buttons = []
    for tag in buttons:
        i=0
        for item in tag.descendants:
            i=i+1
        if(i>1):
            blank_buttons.append(tag)
    return blank_buttons

def remove_blank_buttons(soup):
    for tag in get_blank_buttons(soup):
        tag.extract()
    return

def change_top_button_name(soup, button_name, new_button_name):
    change_button(top_menu_buttons(soup),button_name,new_button_name)
    return

def change_side_button_name(soup,button_name,new_button_name):
    change_button(side_menu_buttons(soup),button_name,new_button_name)
    return

def change_button(button_list, button_name, new_button_name):
    is_found = False
    for item in button_list:
       for child in item.contents:
           if (is_found):
               break
           if(child.name=="span" and child.string==button_name):
               print("We're changing the button " + child.string + " to " + new_button_name)
               child.string = new_button_name
               is_found = True
               break
    return

class Soup_Handler:
    soup = None
    initial_path = ""
    def __init__(self,initial_path):
        self.soup = BeautifulSoup()
        self.initial_path = initial_path



