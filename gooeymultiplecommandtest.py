from gooey import Gooey, GooeyParser
import tkinter
from tkinter import filedialog


@Gooey(show_sidebar = True, navigation='SIDEBAR',navigation_title='Choose an Action')
def action_one():
    desc = "Example application to see if we can process two commands at once"
    my_cool_parser = GooeyParser(description=desc)
    #adding subparsers
    subparsers = my_cool_parser.add_subparsers(help="Subparser help")
    subparser_1 = subparsers.add_parser('s1', help = 'subparser 1 help')
    subparser_1.add_argument('--s1', widget="CheckBox",action='store_true')
    subparser_2 = subparsers.add_parser('s2', help='subparser 2 help')
    subparser_2.add_argument('--s2',widget="CheckBox",action='store_true')

    my_cool_parser.parse_args()


if __name__ =='__main__':
#we're using tkinter to open the file first, because we can't run gooey twice in the same script
#for this script, we need to see what buttons are already there before we do anything
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    button_names = ['Button 1', 'Button 2', 'Button 3', 'Button 4']
    action_one()


