import tkinter
from tkinter import filedialog
import soupaccessories
from bs4 import BeautifulSoup



def get_top_buttons():
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfile()
    soup = BeautifulSoup(file_path, "html.parser")
    top_button_names = []
    top_buttons = soupaccessories.top_menu_buttons(soup)
    for button in top_buttons:
        top_button_names.append(button.string)
    root.destroy()
    return {'Top Button Names': top_button_names,'Top Buttons':top_buttons}

def change_button_text(soup, old_button_text):
    buttons = soupaccessories.find_button_by_tag(soup, old_button_text)
    if (buttons.count>1):
        print("Somehow you've selected more than one button.")
    return buttons


if __name__ == '__main__':

    soup = soupaccessories.SoupHandler()
    top_buttons = []
    first_buttons = soup.first_buttons()
    second_buttons = soup.second_buttons()
    third_buttons = soup.third_buttons()
    if (len(first_buttons) > 0 and first_buttons[0].text.strip() != "Mechanical"
            and first_buttons[0].text.strip() != "Home"):
        top_buttons = first_buttons
    elif(len(second_buttons) > 0 and second_buttons[0].text.strip() != "Mechanical"
         and second_buttons[0].text.strip() != "Home"):
        top_buttons = second_buttons
    elif(len(third_buttons) > 0 and third_buttons[0].text.strip() != "Mechanical"
         and third_buttons[0].text.strip() != "Home"):
        top_buttons = third_buttons

    new_button_names = []

    soupaccessories.write_list_output(top_buttons)

    # for item in top_buttons:
    #     prompt = input("Please enter a new button name. If you're done, enter 'done'.")
    #     while(prompt != "done"):
    #         soup.change_button(item, prompt)


