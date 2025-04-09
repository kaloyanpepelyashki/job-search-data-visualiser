import dearpygui.dearpygui as dpg
from config import WINDOW_WIDTH, WINDOW_HEIGHT, APP_NAME, APP_NAME_SHORT
from infrastructure.screen import center_viewport
from infrastructure import setup_logger
from infrastructure.navigation import page_manager
from ui.pages import DashboardPage, ApplicationsPage
from ui.components import NavBar

def main() :
    setup_logger()
    dpg.create_context()
    dpg.create_viewport(title=APP_NAME, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, clear_color=(249, 249, 251, 100))
    center_viewport(WINDOW_WIDTH, WINDOW_HEIGHT)

    with dpg.window(tag="primary"):
        pass

    dashboard_page = DashboardPage(int(WINDOW_WIDTH), int(WINDOW_HEIGHT))
    applications_page = ApplicationsPage(int(WINDOW_WIDTH), int(WINDOW_HEIGHT))
    global_navbar = NavBar()

    page_manager.register_pages({ dashboard_page.tag: dashboard_page, applications_page.tag: applications_page})
    page_manager.global_navbar = global_navbar

    page_manager.build_layout(WINDOW_WIDTH, WINDOW_HEIGHT)
    page_manager.switch_page(page_manager.pages[dashboard_page.tag])

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("primary", True)
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()