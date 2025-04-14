from .theme_config import theme_light_background_color, theme_light_text_color
import dearpygui.dearpygui as dpg


def create_light_theme():
    with dpg.theme() as light_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, theme_light_background_color, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Text, theme_light_text_color, category=dpg.mvThemeCat_Core)
        with dpg.theme_component(dpg.mvChildWindow):
            dpg.add_theme_color(dpg.mvThemeCol_ChildBg, theme_light_background_color)
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, theme_light_background_color)
            dpg.add_theme_color(dpg.mvThemeCol_Text, theme_light_text_color)

    return light_theme