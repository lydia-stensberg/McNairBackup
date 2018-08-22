from bs4 import BeautifulSoup
import re
import tkinter
from tkinter import filedialog
from tkinter import messagebox
import tkinteraccessories


#singleton class to control the soup
class Soup_Handler:
    class _SingleSoup:
        def __init__(self,soup,file):
            self.soup = soup
            self.file = file
        def __str__(self):
            return repr(self) + self.soup
        def override(self,soup,file):
            self.soup = soup
            self.file = file
    #object to represent soup instance! should only be one! should I add a file to the internal class?
    instance=None
    #objects to represent the open files. Mainly stored so that we have access to the file paths.
    comparative_file = None
    def __init__(self):
        if not Soup_Handler.instance:
            file = filedialog.askopenfile(mode="r")
            soup = BeautifulSoup(file,'html.parser')
            Soup_Handler.instance = Soup_Handler._SingleSoup(soup,file)
        else:
            if (tkinteraccessories.are_you_sure()=='yes'):
                file = filedialog.askopenfile(mode="r")
                soup = BeautifulSoup(file, 'html.parser')
                Soup_Handler.instance.override(soup,file)
            else:
                messagebox.showerror("New File Canceled", "No new file will be loaded.")


    def __getattr__(self, item):
        return getattr(self,item)


    def open_comparative_file(self):
        if not Soup_Handler.comparative_file:
            file = filedialog.askopenfile(mode="r")
            soup = BeautifulSoup(file, 'html.parser')
            Soup_Handler.comparative_file = Soup_Handler._SingleSoup(soup, file)
        else:
            if (tkinteraccessories.are_you_sure() == 'yes'):
                file = filedialog.askopenfile(mode="r")
                soup = BeautifulSoup(file, 'html.parser')
                Soup_Handler.comparative_file.override(soup, file)
            else:
                messagebox.showerror("New File Canceled", "No new file will be loaded.")

    def open_existing_file(self):
        return filedialog.askopenfile()

    def open_with_filepath(file_path):
        my_file = open(file_path,'r')
        return my_file

    def get_side_buttons(self):
        root = tkinter.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        file = self.open_with_filepath(file_path)
        soup = BeautifulSoup(file, "html.parser")
        side_button_names = []
        side_buttons = self.side_menu_buttons(soup)
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


    def find_button_by_tag(soup, old_name):
        return soup.find_all(string=old_name)


    def get_blank_buttons(self,soup):
        buttons =soup.find_all(get_blanks)
        blank_buttons = []
        for tag in buttons:
            i=0
            for item in tag.descendants:
                i=i+1
            if(i>1):
                blank_buttons.append(tag)
        return blank_buttons


    def remove_blank_buttons(self,soup):
        for tag in self.get_blank_buttons(soup):
            tag.extract()
        return


    def change_top_button_name(self,soup, button_name, new_button_name):
        self.change_button(self.top_menu_buttons(soup),button_name,new_button_name)
        return


    def change_side_button_name(self,soup,button_name,new_button_name):
        self.change_button(self.side_menu_buttons(soup),button_name,new_button_name)
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

    def clear_all_soup(self):
        pass

    def write_output(self,override_filepath=False):
        output_string = self.instance.soup.prettify()
        if not override_filepath:
            with filedialog.asksaveasfile("w+") as new_file:
                new_file.write(output_string)
                new_file.close()
        else:
            with open(self.instance.file,"w+") as file:
                file.write(output_string)
                file.close()





def get_blanks(tag):
    return tag.string=="Blank"



