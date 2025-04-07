import dearpygui.dearpygui as dpg
from config import WINDOW_WIDTH, WINDOW_HEIGHT, APP_NAME, APP_NAME_SHORT
from infrastructure.screen import center_viewport
from infrastructure import setup_logger
from ui.pages import DashboardPage

def show_next_screen():
    pass

def main() :
    setup_logger()
    dpg.create_context()
    dpg.create_viewport(title=APP_NAME, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, clear_color=(249, 249, 251, 100))
    center_viewport(WINDOW_WIDTH, WINDOW_HEIGHT)


    dashboard_page = DashboardPage(WINDOW_WIDTH, WINDOW_HEIGHT)
    dashboard_page.build()


    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


 



if __name__ == "__main__":
    main()