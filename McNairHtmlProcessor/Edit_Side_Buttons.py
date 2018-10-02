from gooey import Gooey, GooeyParser
import tkinter
from tkinter import filedialog
import soupaccessories
from bs4 import BeautifulSoup

def change_button_text(soup, old_button_text):
    buttons = soupaccessories.find_button_by_tag(soup, old_button_text)
    if (buttons.count>1):
        print("Somehow you've selected more than one button.")
    return buttons

def main():
    soup = soupaccessories.SoupHandler()
    change_buttons = []
    first_buttons = soup.first_buttons()
    second_buttons = soup.second_buttons()
    third_buttons = soup.third_buttons()
    if (len(first_buttons) > 0 and first_buttons[0].text.strip() == "Mechanical"):
        change_buttons = first_buttons
    elif(len(second_buttons) > 0 and second_buttons[0].text.strip() == "Mechanical"):
        change_buttons = second_buttons
    elif(len(third_buttons) > 0 and third_buttons[0].text.strip() == "Mechanical"):
        change_buttons = third_buttons

    new_button_names = []

    # print("Change button length is " + str(len(change_buttons)))
    new_button = soup.create_new_side_button("../FireProtection/FireProtection.html", change_buttons[-1]['id'],change_buttons[-1]['style'],
                                "Commissioning",button_class=change_buttons[-1]['class'])

    new_button2 = soup.create_new_side_button("../FireProtection/FireProtection.html", change_buttons[-1]['id'],change_buttons[-1]['style'],
                                "Commissioning",button_class=change_buttons[-1]['class'])

    change_buttons[2].insert_after(new_button2)

    new_button.insert_after(new_button2)

    soup.save_file()



if __name__ == '__main__':
    main()





