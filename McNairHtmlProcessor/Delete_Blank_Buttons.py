from bs4 import BeautifulSoup
from gooey import Gooey, GooeyParser
import soupaccessories
import argparse

import sys
sys.path.append('C:/Users/lydia.stensberg/Documents/Programming/McNairDev_local')


class Soup_Handler(BeautifulSoup):
    soup = None
    original_file_path = ""

    def __init__(self, existing_file_path):
        self.soup = BeautifulSoup(existing_file_path, features="html.parser")
        self.original_file_path = existing_file_path
        return

    def delete_all_blank_top_buttons(self, soup):
        soupaccessories.remove_blank_buttons(soup)
        return

    def overwrite_input_file(self,soup):
        new_file_string = soup.prettify()
        with open(self.original_file_path, 'w+') as my_new_file:
            my_new_file.write(new_file_string)
            my_new_file.close()
        return

    def save_as_new_file(self, soup, new_file_path):
        new_file_string = soup.prettify()
        with open(new_file_path, 'w+') as my_new_file:
            my_new_file.write(new_file_string)
            my_new_file.close()
        return



@Gooey()
def main():
    parser = GooeyParser(description="Open HTML File")
    parser.add_argument("File Path", help="Provide a file path to an .html file.",widget='FileChooser')
    parser.add_argument('-d', '--Delete Blanks', choices=['yes', 'no'], help='Delete all blank buttons?')
    parser.add_argument("-o", "--Overwrite", action="store_true",
                        help="Overwrite input file")
    parser.add_argument('-n', "--New File Path", help="Provide a path to save processed file to", widget="FileSaver")
#get arguments from parser
    parser_args = parser.parse_args()
    parser_vars = vars(parser_args)
#open and prepare new html file for processing
    my_file = soupaccessories.open_existing_file(parser.parse_args())
    my_soup_handler = Soup_Handler(my_file)
#check to see what user wanted to do
    if (parser_vars['Delete Blanks'] == 'yes'):
        my_soup_handler.delete_all_blank_top_buttons(my_soup_handler.soup)

#check to see if we overwrite old file or create new one
    if(parser_vars['Overwrite']):
        my_soup_handler.overwrite_input_file(my_soup_handler.soup)

    else:
        my_soup_handler.save_as_new_file(my_soup_handler.soup, parser_vars['New File Path'])

if __name__ == '__main__':
  main()


