import dearpygui.dearpygui as dpg

class NavBar:
    
    def render(self, parent_screen_width, parent_screen_hight, nav_callback_one, nav_callback_two):
        nav_bar_left_spacing = parent_screen_width * 0.91

        #//TODO Finish the font-binder and make sure it binds the font properly and fully.
        # with dpg.font_registry():
        #     enlarged_font = dpg.add_font("font/Inter-VariableFont_opsz,wght.ttf", 244)
        # dpg.bind_item_font("dashboard_page_link", enlarged_font)
        

        with dpg.group(tag="navbar", horizontal=True):
            dpg.add_spacer(width=nav_bar_left_spacing)
            dpg.add_button(tag="dashboard_page_link", label="Dashboard", callback=nav_callback_one)
            dpg.add_button(label="Applications", callback=nav_callback_two)
        
