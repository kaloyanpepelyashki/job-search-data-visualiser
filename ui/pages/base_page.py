import dearpygui.dearpygui as dpg

class BasePage:
    def __init__(self, tag: str, visible: bool = False):
        self.tag: str = tag,
        self.visible = visible
        self.state = {}
    
    def build(self):
        """
        Builds the UI of the page
        The UI of each page must be built here
        Each page implements the build method itslef (must be implemented by subclasses)
        """
        raise NotImplementedError("Each page must be built")
    
    def show(self):
        dpg.show_item(self.tag)
        self.visible = True
    
    def hide(self):
        dpg.hide_item(self.tag)
        self.visible = False

        