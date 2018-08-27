import soupaccessories
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

def update_href(old_href, new_href):
    href_list = soupaccessories.top_menu_buttons(soup_wrapper)
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

soup_wrapper = soupaccessories.SoupHandler()

table_list = soup_wrapper.find_all_tables()
button_list = soup_wrapper.first_buttons()
for item in soup_wrapper.second_buttons():
    button_list.append(item)
for item in soup_wrapper.third_buttons():
    button_list.append(item)

soupaccessories.write_list_output(button_list)

# this returns a list of content tags for each table! yay :)
for item in button_list:
    if item.string is None:
        print("This Button %s has a file reference %s" %(item.span.string, item['href']))
    else:
        print("This button  %s has a file reference %s" %(item.string, item['href']))
    prompt = input("What would you like to change? ")
    if prompt == 'href':
        item.href = filedialog.askopenfilename()
    elif prompt == 'table':
        print("This is a new table with the id " + item['id'])  # this works
        table_contents = return_table_contents_by_id(soup_wrapper.instance.soup, item['id'])
        print("The items in this table are %s " % table_contents)

        for entry in table_contents:
            answer = input("Would you like to change the name of the entry or the file reference?")
            if answer == 'name':
                new_name = input("Enter a new name")
                change_table_entry_title(entry, new_name)
            elif answer == 'file':
                new_file = filedialog.askopenfilename()
                change_table_entry_file(entry, new_file)
                print(entry)
            else:
                pass
        new_entry = input("Would you like to add a new entry to this table or delete an entry? ")
        if new_entry == "new":
            new_name = input("Enter the new entry name: ")
            new_file = input("Is the new entry a file or a link?")
            if new_file == "link":
                file = input("Please enter the web address to link.")
            elif new_file == "file":
                file = filedialog.askopenfilename()
            else:
                print("New Entry Addition Canceled")
                pass
            table_contents[-1].insert_after(soup_wrapper.create_new_table_entry(file, new_name))
        elif new_entry == "delete":
            entry_to_delete = input("Please enter the name of the entry you'd like to delete")
            for entry in table_contents:
                if entry.a.string == entry_to_delete:
                    entry.extract()
                    print(entry + " was deleted")




    elif prompt == 'link':
        item.href = input("Enter a website link ")

    else:
        pass


output_string = soup_wrapper.instance.soup.prettify()
with open("BSLMC McNair Campus\\New_Table_Index.html", "w+") as output_file:
    output_file.write(output_string)
    output_file.close()
