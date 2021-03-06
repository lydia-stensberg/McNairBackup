from bs4 import BeautifulSoup
import soupaccessories
import re
import tkinter
from tkinter import filedialog

def all_script_tags(soup):
    return soup.find_all("script")

# TODO delete this method once you're done with tables -duplicated in soupaccessories mod
def create_new_table_entry(soup, href, new_name):
    new_entry = soup.new_tag(name='tr')
    level1_entry = soup.new_tag(name='td')
    level2_entry = soup.new_tag('a', attrs={'href': href})
    level2_entry.string = new_name
    new_entry.append(level1_entry)
    level1_entry.append(level2_entry)
    return new_entry

# TODO: this sets that HREF to a RELATIVE PATH so we need to figure out a way to get a file's relative path
# to the location the original file is in.
# Note: putting in complete files for an HREF results in a complete filepath for an output.
# previous issues probably caused by me just typing a word as the href, and there must be some sort of
# language in BeaurifulSoup that will take that as a relative instead of absolute path.


def update_href(old_href, new_href):
    href_list = soupaccessories.top_menu_buttons(soup)
    for ref in href_list:

        if ref['href'] == old_href:
            ref['href'] = new_href
            print(old_href + " has been set to " + new_href + " for button " + ref.string)
            break
    return


def new_button_id_from_existing(exiting_button_id):
    last_id_number = int(exiting_button_id[-1])
    last_id_number = last_id_number + 1
    return exiting_button_id[:-1] + str(last_id_number)

# TODO: Method that will get images out of a project

def find_all_tables(soup):
    return soup.find_all(find_tables)


def find_tables(tag):
    return tag.name == "table"


def change_table_entry_title(table_entry, new_entry_name):
    table_entry.a.string = new_entry_name
    return


def find_button_images(soup):
    all_images = soup.find_all('img')
    button_images = []
    for item in all_images:
        if int(item['height']) == 20 and int(item['width']) == 20:
            button_images.append(item)
    return button_images


def change_table_entry_file(table_entry, new_href):
    table_entry.a['href'] = new_href
    return


def return_table_contents_by_id(soup, table_id):
    table_list = find_all_tables(soup)
    table_id = table_id + "M"
    table_contents = []
    for item in table_list:
        if (item['id'] == table_id):
            table_contents = item.find_all("tr")
    return table_contents

# file = filedialog.askopenfile(mode="r")

soup = soupaccessories.SoupHandler()

table_list = soup.find_all_tables()
first_button_list = soup.first_buttons()
second_button_list =  soup.second_buttons()
third_button_list =  soup.third_buttons()

i = 1
for item in [first_button_list, second_button_list, third_button_list]:
    print('These are the Button{} types for this file.'.format(i))
    soupaccessories.write_list_output(item)
    i = i + 1

button_edit = input("Which button set do you want to edit?")
if button_edit == "1":
    input = first_button_list
elif button_edit == "2":
    input = second_button_list
elif button_edit == "3":
    input = third_button_list
else:
    input = "Invalid"




output_string = soup.instance.soup.prettify()
with open("BSLMC McNair Campus\\New_Table_Index.html", "w+") as output_file:
    output_file.write(output_string)
    output_file.close()


