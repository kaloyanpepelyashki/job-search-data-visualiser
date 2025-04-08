import dearpygui.dearpygui as dpg

#This class must be treated as a signleton, so it should not be instantiated more
class PageManager: 
    def __init__(self):
        self.pages = {}
        self.global_navbar = None
        self.current_page = None

    def register_pages(self, pages: dict):
        self.pages = pages

        print("Registered pages: ", self.pages.keys())

    def switch_page(self, page):
        self.current_page = page
        dpg.delete_item(self.content_area_id, children_only=True)
        with dpg.group(parent=self.content_area_id):
            page.build()
        page.visible = True

    def build_layout(self, width, height):
        with dpg.window(label="master window", tag="master_window", width=width, height=height, autosize=False, no_scrollbar=True):
            if self.global_navbar:
                self._build_navbar()
            self.content_area_id = dpg.add_child_window(width=-1, height=-1)
    
    def _build_navbar(self):
        try:
            print(self.pages)
            first_callback = lambda: self.switch_page(self.pages["dashboard_page"]) 
            second_callback = lambda: self.switch_page(self.pages["applications_page"])

            self.global_navbar.render(first_callback, second_callback)
        except():
            print("Error building navigation bar")


        

#A singleton instance of the PageManager class
page_manager = PageManager()
