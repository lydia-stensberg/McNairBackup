from bs4 import BeautifulSoup
import re


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

def all_script_tags(soup):
    return soup.find_all("script")

def write_output(list):
    print('\n'.join('{}:{}'.format(*k) for k in enumerate(list)))


#TODO: this sets that HREF to a RELATIVE PATH so we need to figure out a way to get a file's relative path
#to the location the original file is in.
def update_href(old_href, new_href):
    href_list = top_menu_buttons(soup)
    for item in href_list:
        if (item['href']==old_href):
            item['href'] = new_href
            print(old_href + " has been set to " + new_href + " for button " + item.string)
            break
    return


def find_all_tables(soup):
    return soup.find_all(find_tables)


def find_tables(tag):
    return tag.name == "table"


def return_table_contents_by_id(soup, table_id):
    table_list = find_all_tables(soup)
    table_contents = []
    for item in table_list:
        if(item['id']==table_id):
            table_contents = item.find_all("tr")
    return table_contents

my_file = open("Index.html",'r')

soup = BeautifulSoup(my_file, 'html.parser')

table_list = find_all_tables(soup)

#this returns a list of content tags for each table! yay :)
for item in table_list:
    print("This is a new table with the id " + item['id']) #this works
    print("The items in this table are %s " % return_table_contents_by_id(soup,item['id']))

# output_string = soup.prettify()
# with open("New_Index.html", "w+") as output_file:
#     output_file.write(output_string)
#     output_file.close()
my_file.close()


