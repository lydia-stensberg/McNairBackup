from gooey import Gooey, GooeyParser
import tkinter
from tkinter import filedialog
import soupaccessories
from bs4 import BeautifulSoup

def get_side_buttons():
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    file = soupaccessories.open_with_filepath(file_path)
    soup = BeautifulSoup(file, "html.parser")
    side_button_names = []
    side_buttons = soupaccessories.side_menu_buttons(soup)
    for button in side_buttons:
        side_button_names.append(button.string)
    return {'Side Button Names': side_button_names,'Side Buttons': side_buttons}

def change_button_text(soup, old_button_text):
    buttons = soupaccessories.find_button_by_tag(soup, old_button_text)
    if (buttons.count>1):
        print("Somehow you've selected more than one button.")
    return buttons

@Gooey(show_sidebar = True, navigation='SIDEBAR',navigation_title='Choose an Action')
def main():
    buttons = get_side_buttons()
    desc_message = "Choose a Button Option: " + str(buttons['Side Button Names'])
    main_parser = GooeyParser(description=desc_message)
    subparsers = main_parser.add_subparsers()

    #adding parser and commands for changing button names

    name_parser = subparsers.add_parser("ChangeButtonName")
    name_parser.add_argument("--choosename",metavar="Choose A Button", choices=buttons['Side Button Names'])
    name_parser.add_argument("--newname",metavar="Enter New Button Text")

    #adding parser and commands for showing top buttons with tables
    href_parser = subparsers.add_parser("UpdateButtonReferenceFiles")
    href_parser.add_argument("--chooseref",metavar="Choose A Button", choices=buttons['Side Button Names'])
    href_parser.add_argument("--select",metavar="Update File Reference", widget='FileChooser')

    #TODO: Add function for adding new buttons next to old ones

    #parse arguments from user
    main_parser.parse_args()

if __name__ == '__main__':
    main()




