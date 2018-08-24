from bs4 import BeautifulSoup
import re
import copy


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


def copy_last_table_entry(list_table_entries):
    return copy.copy(list_table_entries[len(list_table_entries) - 1])


def create_new_table_entry(soup, href, new_name):
    new_entry = soup.new_tag(name='tr')
    level1_entry = soup.new_tag(name='td')
    level2_entry = soup.new_tag('a', attrs={'href':href})
    level2_entry.string = new_name
    new_entry.append(level1_entry)
    level1_entry.append(level2_entry)

    print(new_entry.prettify())

# TODO: this sets that HREF to a RELATIVE PATH so we need to figure out a way to get a file's relative path
# to the location the original file is in.


def update_href(old_href, new_href):
    href_list = top_menu_buttons(soup)
    for ref in href_list:

        if ref['href'] == old_href:
            ref['href'] = new_href
            print(old_href + " has been set to " + new_href + " for button " + ref.string)
            break
    return


# TODO: Method that will get images out of a project


def find_all_tables(soup):
    return soup.find_all(find_tables)


def find_tables(tag):
    return tag.name == "table"


def change_table_entry_title(table_entry, new_entry_name):
    table_entry.a.string = new_entry_name
    return


def change_table_entry_file(table_entry, new_href):
    table_entry.a['href'] = new_href
    return


def return_table_contents_by_id(soup, table_id):
    table_list = find_all_tables(soup)
    table_contents = []
    for item in table_list:
        if (item['id'] == table_id):
            table_contents = item.find_all("tr")
    return table_contents


def add_table_entry(table_entry_list: object, new_entry_name: str, new_entry_file: str):
    new_entry = copy_last_table_entry(table_entry_list)
    last_entry = table_entry_list[-1]
    change_table_entry_file(new_entry, new_entry_file)
    change_table_entry_title(new_entry, new_entry_name)
    new_entry.parent = None
    new_entry.successor = None
    print("New entry is " + new_entry.prettify())
    table_entry_list[len(table_entry_list)-1].insert_after(last_entry)


my_file = open("Index.html", 'r')

soup = BeautifulSoup(my_file, 'html.parser')

create_new_table_entry(soup, href="hewhref", new_name="Brand New Entry")


table_list = find_all_tables(soup)

# this returns a list of content tags for each table! yay :)
for item in table_list:
    table_contents = return_table_contents_by_id(soup, item['id'])
    print("This is a new table with the id " + item['id'])  # this works
    print("The items in this table are %s " % return_table_contents_by_id(soup, item['id']))
    create_new_table_entry(soup, new_entry_name="New Entry",
                           new_entry_file="C:\\Users\\stens\\Documents")
#
# print("Now seeing if tables have updated")
# for item in find_all_tables(soup):
#     table_contents = return_table_contents_by_id(soup, item['id'])
#     print("This is a new table with the id " + item['id'])  # this works
#     print("The items in this table are %s " % return_table_contents_by_id(soup, item['id']))



# output_string = soup.prettify()
# with open("New_Index.html", "w+") as output_file:
# #     output_file.write(output_string)
# #     output_file.close()
my_file.close()
