import dearpygui.dearpygui as dpg
from config import WINDOW_WIDTH, WINDOW_HEIGHT
from Application.Utilities import center_viewport

# CURRENT_OVERLAY_SCREEN = ""

# def show_next_screen():
#     global CURRENT_OVERLAY_SCREEN
#     if not CURRENT_OVERLAY_SCREEN: 
#         dpg.show_item("screen1")
#         CURRENT_OVERLAY_SCREEN = "screen1" 
#     if CURRENT_OVERLAY_SCREEN is "screen1":
#         dpg.hide_item("screen1")
#         dpg.show_item("screen2")
#         CURRENT_OVERLAY_SCREEN = "SCREEN 2"
#     if CURRENT_OVERLAY_SCREEN is "SCREEN 2":
#         dpg.hide_item("screen2")
#         dpg.show_item("screen1")
#         CURRENT_OVERLAY_SCREEN = "SCREEN 1"



# with dpg.window(label="Main window", width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
#     dpg.add_text("Hello world, this is main screen")
#     dpg.add_button(label="Next", callback=lambda: show_next_screen())

# with dpg.handler_registry():
#     with dpg.window(label="screen1", tag="screen1", width=600, height=600):
#         dpg.add_text("Screen 1")
#     with dpg.window(label="screen2", tag="screen2", width=600, height=600):
#         dpg.add_text("Screen 2")


def show_next_screen():
    pass

def main() :
    dpg.create_context()
    dpg.create_viewport(title="Test Title", width=WINDOW_WIDTH, height=WINDOW_HEIGHT,)

    with dpg.window(label="Main window", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, no_title_bar=True, no_move=True):
        dpg.add_text("Hello world, this is main screen")
        dpg.add_button(label="Next", callback=lambda: show_next_screen())

    center_viewport(WINDOW_WIDTH, WINDOW_HEIGHT)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


main()