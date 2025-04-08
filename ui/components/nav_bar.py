import dearpygui.dearpygui as dpg


class NavBar:
    
    def render(self, nav_callback_one, nav_callback_two):
        with dpg.group(tag="navbar", horizontal=True):
            dpg.add_spacer(width=50)
            dpg.add_button(label="Dashboard", callback=nav_callback_one)
            dpg.add_button(label="Applications", callback=nav_callback_two)
            