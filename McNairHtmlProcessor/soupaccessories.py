from bs4 import BeautifulSoup
import re

def open_existing_file(args):
    file_path = vars(args)
    my_file = open(file_path['File Path'],'r')
    return my_file

def open_with_filepath(file_path):
    my_file = open(file_path,'r')
    return my_file

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