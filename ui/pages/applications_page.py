from .base_page import BasePage
import dearpygui.dearpygui as dpg

class ApplicationsPage(BasePage):

    def __init__(self, width, height):
        super().__init__(tag="applications", visible=False)
        self.state["width"]= int(width)
        self.state["height"] = int(height)

    def build(self):
        width = int(self.state.get("width", 600)) 
        height = int(self.state.get("height", 400))
        tag = str(self.tag)

        with dpg.window(label="Applications page", tag=tag, show=self.visible, width=width, height=height, no_title_bar=True):
            dpg.add_text("This is applications page")

    def update(self):
        pass