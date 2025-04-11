import dearpygui.dearpygui as dpg

class BasePage:
    def __init__(self, tag: str, visible: bool = False, parent_window_tag = None):
        self.tag: str = tag
        self.parent_window_tag: str = parent_window_tag
        self.visible = visible
        self.state = {}
        #Controls if the page has been built already in the current application run
        self.is_built = False
    
    def build(self):
        """
        Builds the UI of the page
        The UI of each page must be built here
        Each page implements the build method itslef (must be implemented by subclasses)
        """
        raise NotImplementedError("Each page must be built")
    
    def show(self):
        """
        Shows the built page on screen
        Calls the dearpygui show_item method
        """
        try:
            dpg.show_item(self.tag)
            self.visible = True
        except Exception as ex:
            print(f"Error showing page with tag: {self.tag} ", type(ex), ex.args)


    def hide(self):
        """
        Hides the page from screen
        Calls the dearpygui hide_item method
        """
        try:
            dpg.hide_item(self.tag)
            self.visible = False
        except Exception as ex:
            print(f"Error hiding page with tag: {self.tag} ", type(ex), ex.args)

        