import ctypes
import dearpygui.dearpygui as dpg

def get_screen_resolution():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def center_viewport(width, height):
    screen_width, screen_height = get_screen_resolution()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    dpg.set_viewport_pos([x, y])