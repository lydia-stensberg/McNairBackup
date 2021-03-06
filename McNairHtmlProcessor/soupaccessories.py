from bs4 import BeautifulSoup
import re
import tkinter
from tkinter import filedialog
from tkinter import messagebox
import tkinteraccessories
import Error_Handler


# singleton class to control the soup
class SoupHandler:
    class _SingleSoup:
        def __init__(self, soup, file):
            self.soup = soup
            self.file = file

        def __str__(self):
            return repr(self) + self.soup

        def override(self, soup, file):
            self.soup = soup
            self.file = file

    # object to represent soup instance! should only be one! should I add a file to the internal class?
    instance = None
    # objects to represent the open files. Mainly stored so that we have access to the file paths.
    comparative_file = None

    def __init__(self):
        if not SoupHandler.instance:
            file = filedialog.askopenfile(mode="r")
            soup = BeautifulSoup(file, 'html.parser')
            SoupHandler.instance = SoupHandler._SingleSoup(soup, file)
        else:
            if tkinteraccessories.are_you_sure() == 'yes':
                file = filedialog.askopenfile(mode="r")
                soup = BeautifulSoup(file, 'html.parser')
                SoupHandler.instance.override(soup, file)
            else:
                messagebox.showerror("New File Canceled", "No new file will be loaded.")

    # def __getattr__(self, item):
    #     return getattr(self, item)


    def open_comparative_file(self):
        if not SoupHandler.comparative_file:
            file = filedialog.askopenfile(mode = "r")
            soup = BeautifulSoup(file, 'html.parser')
            SoupHandler.comparative_file = SoupHandler._SingleSoup(soup, file)
        else:
            if (tkinteraccessories.are_you_sure() == 'yes'):
                file = filedialog.askopenfile(mode = "r")
                soup = BeautifulSoup(file, 'html.parser')
                SoupHandler.comparative_file.override(soup, file)
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
        side_buttons = self.second_buttons(soup)
        for button in side_buttons:
            side_button_names.append(button.string)
        return {'Side Button Names': side_button_names,'Side Buttons': side_buttons}


    def has_class(css_class):
        return css_class is not None


    def has_class_no_id(tag):
        return tag.has_attr('class') and not tag.has_attr('id')


    def second_buttons(self):
        return self.instance.soup.find_all(class_="Button2")


    def third_buttons(self):
        return self.instance.soup.find_all(class_="Button3")


    def has_file(href):
        return href is not None and re.compile("Files").search(href)


    def find_button_by_tag(self, old_name):
        def string_is_tag(tag):
            return tag.string == old_name
        buttons = self.instance.soup.find_all(string_is_tag)
        for tag in buttons:
            i = 0
            for item in tag.descendants:
                i = i+1
            if(i > 1):
                return tag
        raise Error_Handler.Button_Has_No_Table("This button has no tables associated with it")


    def get_blank_buttons(self):
        buttons =self.instance.soup.find_all(get_blanks)
        blank_buttons = []
        for tag in buttons:
            i = 0
            for item in tag.descendants:
                i = i+1
            if(i > 1):
                blank_buttons.append(tag)
        return blank_buttons


    def remove_blank_buttons(self):
        for tag in self.get_blank_buttons():
            tag.extract()
        return


    def change_third_button_name(self, button_name, new_button_name):
        self.change_button(self.third_buttons(), button_name, new_button_name)
        return

    def change_first_button_name(self, button_name, new_button_name):
        self.change_button(self.first_buttons(), button_name, new_button_name)


    def change_second_button_name(self, button_name, new_button_name):
        self.change_button(self.second_buttons(), button_name, new_button_name)
        return

    def change_button_name(self, button, new_button_name):
        if (self.is_first_button(button)):
            self.change_first_button_name(button,new_button_name)
            return

        elif(self.is_second_button(button)):
            self.change_second_button_name(button,new_button_name)
            return

        elif(self.is_third_button(button)):
            self.change_third_button_name(button, new_button_name)
            return

        else:
            raise Error_Handler.Button_DNE("There has been an error figuring out which type of button you have. Button name not changed.")


    def is_first_button(self, button):
        return button['class'] == 'Button1'

    def is_second_button(self,button):
        return button['class'] == 'Button2'

    def is_third_button(self,button):
        return button['class'] == 'Button3'

    def change_button(self, button_list, button_name, new_button_name):
        is_found = False
        for item in button_list:
            for child in item.contents:
               if (is_found):
                   break
               if(child.name=="span" and child.string==button_name):
                   # print("We're changing the button " + child.string + " to " + new_button_name)
                   child.string = new_button_name
                   is_found = True
                   break
        return

    def clear_all_soup(self):
        pass

    def write_output(self, override_filepath=False):
        output_string = self.instance.soup.prettify()
        if not override_filepath:
            with filedialog.asksaveasfile("w+") as new_file:
                new_file.write(output_string)
                new_file.close()
        else:
            with open(self.instance.file, "w+") as file:
                file.write(output_string)
                file.close()

    def create_new_table_entry(self, href, new_name):
        new_entry = self.instance.soup.new_tag(name='tr')
        level1_entry = self.instance.soup.new_tag(name='td')
        level2_entry = self.instance.soup.new_tag('a', attrs={'href': href, 'target': "_blank"})
        level2_entry.string = new_name
        new_entry.append(level1_entry)
        level1_entry.append(level2_entry)
        return new_entry

    def first_buttons(self):
        return self.instance.soup.find_all(class_="Button1")

    # def return_table_contents_by_id(self, table_id):
        table_list = self.find_all_tables()
        table_contents = []
        for item in table_list:
            if (item['id'] == table_id):
                table_contents = item.find_all("tr")
        return table_contents

    def find_all_tables(self):
        return self.instance.soup.find_all(find_tables)


    def create_new_side_button(self, button_href, button_id, button_style, button_string, button_class="Button2"):
        new_button = self.instance.soup.new_tag('a', attrs={'class': button_class, 'href': button_href, 'id': button_id,
                                              'style': self.new_style_from_existing_style(button_style)})
        span_tag = self.instance.soup.new_tag('span')
        new_button.append(span_tag)
        span_tag.string = button_string
        return new_button

    def add_new_button_image(self, previous_image):
        new_image = self.instance.soup.new_tag('img',
                                               attrs={'alt': previous_image['alt'], 'border': previous_image['border'],
                                               'onload': previous_image['onload'],
                                                      'src': previous_image['src'],
                                               'style': self.new_style_from_existing_style(self.instance.soup,
                                                                                      previous_image['style']),
                                               'width': previous_image['width'], 'height': previous_image['height']})
        previous_image.insert_after(new_image)
        return new_image

    def new_style_from_existing_style(self, existing_style_string):
        top_index = existing_style_string.find("top:")
        existing_position = existing_style_string[(top_index + 4):(top_index + 7)]
        new_position = int(existing_position) + 34
        new_style = existing_style_string.replace(str(existing_position), str(new_position))
        return new_style

    def save_file(self):
        soupstring = self.instance.soup .prettify()
        with filedialog.asksaveasfile(mode="w+") as file:
            file.write(soupstring)
            file.close()


    def delete_table_entry(self, table_entry):
        table_entry.extract()


def get_blanks(tag):
    return tag.string=="Blank"

def has_file(href):
    return href is not None and re.compile("Files").search(href)

def find_tables(tag):
    return tag.name == "table"

def side_menu_buttons(soup):
    return soup.find_all(class_="Button2")


def top_menu_buttons(soup):
    return soup.find_all(class_="Button3")

def has_class(css_class):
    return css_class is not None


def has_class_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


def write_list_output(list):
    print('\n'.join('{}:{}'.format(*k) for k in enumerate(list)))

def change_table_entry_title(table_entry, new_entry_name):
    table_entry.a.string = new_entry_name
    return

def change_table_entry_file(table_entry, new_href):
    table_entry.a['href'] = new_href
    return








