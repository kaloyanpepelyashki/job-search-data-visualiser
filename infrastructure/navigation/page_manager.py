import dearpygui.dearpygui as dpg
import logging
#This class must be treated as a signleton, so it should not be instantiated more
class PageManager: 
    def __init__(self):
        #The logger. Used to log general or error application logs
        self.logger = logging.getLogger(__name__)
        
        self.pages = {}
        self.global_navbar = None
        self.current_page = None
        self.parent_window_tag = "master_content_area"


    def register_pages(self, pages: dict):
        '''
        Rgisters pages in the PageManager registry.
        All pages must be registered first 
        '''
        for key, value in pages.items():
            self.pages[str(key)] = value


    def switch_page(self, page):
        if self.current_page:
            self.current_page.hide()

        #Checks if the page has been previously built
        if not page.is_built:
            #If page hasn't been built, it builds it
            page.build()
        
        page.show()
        self.current_page = page


    def build_layout(self, width, height):
        """
        Builds the baster screen's layout
        Initiates the master screen (master window) and builds all the necessary components for that. 
        """
        try:
            with dpg.window(label="master", tag="master", width=width, height=height, autosize=False, no_scrollbar=True, no_move=True, no_close=True, no_title_bar=True):
                if self.global_navbar:
                    self._build_navbar(width, height)
                self.content_area_id = dpg.add_child_window(tag=self.parent_window_tag, width=-1, height=-1, border=False)
        except Exception as ex:
            self.logger.error(f"Error building layout: {type(ex)}, {ex.args}")


    def _build_navbar(self, window_width, window_height):
        try:
            first_callback = lambda: self.switch_page(self.pages["dashboard"]) 
            second_callback = lambda: self.switch_page(self.pages["applications"])

            self.global_navbar.render(window_width, window_height, first_callback, second_callback)
        except Exception as ex:
            self.logger.error(f"Error building navigation bar: {type(ex)}, {ex.args}")


        

#A singleton instance of the PageManager class
page_manager = PageManager()
