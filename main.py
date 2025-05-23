import asyncio
import logging
from infrastructure import setup_logger

setup_logger()
logger = logging.getLogger(__name__)
from infrastructure.auth import authenticate_for_google
logger.info("Authenticating for Google...")
asyncio.run(authenticate_for_google())


import dearpygui.dearpygui as dpg
from config import WINDOW_WIDTH, WINDOW_HEIGHT, APP_NAME
from infrastructure.screen import center_viewport

from infrastructure.navigation import page_manager
from ui.theme import create_light_theme
from ui.pages import DashboardPage, ApplicationsPage
from ui.components import NavBar
from infrastructure.runtime import async_manager


def main() :
    try:
        logger.info("Application started")


        dpg.create_context()
        dpg.create_viewport(title=APP_NAME, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, clear_color=(249, 249, 251, 100))
        center_viewport(WINDOW_WIDTH, WINDOW_HEIGHT)

        #The master component tag, defines where the child components (pages) must display (within the master component or the parent component)
        master_component_tag = page_manager.parent_window_tag

        dashboard_page = DashboardPage(master_component_tag, int(WINDOW_WIDTH), int(WINDOW_HEIGHT))
        applications_page = ApplicationsPage(master_component_tag, int(WINDOW_WIDTH), int(WINDOW_HEIGHT))
        global_navbar = NavBar()

        page_manager.register_pages({ dashboard_page.tag: dashboard_page, applications_page.tag: applications_page})
        page_manager.global_navbar = global_navbar

        page_manager.build_layout(WINDOW_WIDTH, WINDOW_HEIGHT)
        page_manager.switch_page(page_manager.pages[dashboard_page.tag])

        async_manager.start_polling()

        #//TODO For later: Write the logic for checking if dark theme is on and create the right theme accordingly
        theme = create_light_theme() 

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("master", True)
        dpg.bind_theme(theme)
        dpg.start_dearpygui()
        dpg.destroy_context()
        logger.info("App is exiting")
    except Exception as ex:
        logger.error(f"Could not start application. {type(ex)}, {ex.args}")

if __name__ == "__main__":
    main()