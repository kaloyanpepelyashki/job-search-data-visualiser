import dearpygui.dearpygui as dpg

#This class must be treated as a signleton, so it should not be instantiated more
class PageManager: 
    def __init__(self):
        self.pages = {}
        self.current_page = None

    def register(self, page):
        if not page.tag in self.pages:
            self.pages[page.tag] = page
            page.build()

    def switch_page(self, from_tag: str, to_tag: str):
        dpg.hide_item(from_tag)
        dpg.show_item(to_tag)
        

#A singleton instance of the PageManager class
page_manager = PageManager()
