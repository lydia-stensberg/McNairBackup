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


my_file = open("Index.html",'r')

soup = BeautifulSoup(my_file, 'html.parser')

href_list = soup.find_all(href=has_file)

script_list = all_script_tags(soup)

print(*top_menu_buttons(soup), sep="\n")

# write_output(blank_buttons)

# blank_buttons[4].extract()


# new_file_string = soup.prettify()
# with open("New_Index.html", 'w+') as my_new_file:
#     my_new_file.write(new_file_string)
#     my_new_file.close()
