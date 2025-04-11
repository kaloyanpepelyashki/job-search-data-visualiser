from .base_page import BasePage
import dearpygui.dearpygui as dpg

class ApplicationsPage(BasePage):

    def __init__(self, parent_window_tag, width, height):
        super().__init__(tag="applications", visible=False, parent_window_tag=parent_window_tag)
        self.state["width"]= int(width)
        self.state["height"] = int(height)

    def build(self):
        try:
            width = int(self.state.get("width", 600)) 
            height = int(self.state.get("height", 400))
            tag = str(self.tag)

            with dpg.child_window(label="Applications page", tag=tag, parent=self.parent_window_tag, show=self.visible, width=width, height=height, border=False):
                dpg.add_text("This is applications page")
            
            self.is_built = True
        except Exception as ex:
            print(f"Error building page with tag: {self.tag}: ", type(ex), ex.args)

    def update(self):
        pass