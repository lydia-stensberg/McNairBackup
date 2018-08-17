from gooey import Gooey, GooeyParser
import tkinter
from tkinter import filedialog
import soupaccessories
from bs4 import BeautifulSoup


@Gooey(show_sidebar = True, navigation='SIDEBAR',navigation_title='Choose an Action')
def gooey_routine(buttons):
    desc_message = "Choose a Button Option: " + str(buttons)
    main_parser = GooeyParser(description=desc_message)
    subparsers = main_parser.add_subparsers()

    #adding parser and commands for changing button names
    name_parser = subparsers.add_parser("ChangeButtonName")
    name_parser.add_argument("--choosebutton",metavar="Choose A Button", choices=buttons)
    name_parser.add_argument("--newname",metavar="Enter a New Name", type=str)

    #adding parser and commands for showing top buttons with tables
    href_parser = subparsers.add_parser("ChangeButtonReferenceFiles")
    href_parser.add_argument("--choosefile",metavar="Choose A Button",choices=buttons)
    href_parser.add_argument("--select",metavar="Select a New File Reference", widget='FileChooser')

    #TODO: Add function for adding new buttons next to old ones

    #parse arguments from user
    args = main_parser.parse_args()

    return

# def get_top_buttons():
#     root = tkinter.Tk()
#     root.withdraw()
#     file_path = filedialog.askopenfile()
#     soup = BeautifulSoup(file_path, "html.parser")
#     top_button_names = []
#     top_buttons = soupaccessories.top_menu_buttons(soup)
#     for button in top_buttons:
#         top_button_names.append(button.string)
#     root.destroy()
#     return {'Top Button Names': top_button_names,'Top Buttons':top_buttons}

# def change_button_text(soup, old_button_text):
#     buttons = soupaccessories.find_button_by_tag(soup, old_button_text)
#     if (buttons.count>1):
#         print("Somehow you've selected more than one button.")
#     return buttons


if __name__ == '__main__':
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfile()
    soup = BeautifulSoup(file_path, "html.parser")
    top_button_names = []
    top_buttons = soupaccessories.top_menu_buttons(soup)
    for button in top_buttons:
        top_button_names.append(button.string)
    root.destroy()

    gooey_routine(top_button_names)
