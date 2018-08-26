

class HTML_Error(Exception):
    pass

class File_Not_Loaded_Error(Exception):
    """Raised when an html file hasn't been loaded into the handler yet"""
    pass

class Button_Has_No_Table(Exception):
    """Raised when a null table has been returned by id"""
    pass


