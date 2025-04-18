import logging
from .base_page import BasePage
import dearpygui.dearpygui as dpg

class DashboardPage(BasePage):
    def __init__(self, parent_window_tag, width, height):
        super().__init__(tag="dashboard", visible=False, parent_window_tag=parent_window_tag)
        self.state["width"]= int(width)
        self.state["height"] = int(height)
        self.state["char-left"] = [0, 1, 12, 22]
        self.state["char-right"] = [0, 3, 15, 25]
    
    def build(self):
        try:
            self.logger.info("Building dashboard page")
            with dpg.child_window(label="Dashboard", tag=self.tag, parent=self.parent_window_tag, show=self.visible, autosize_x=True, autosize_y=True, border=False):
                dpg.add_text("📊 Dashboard Overview page")
                dpg.add_button(label="Refresh Chart", callback=self.update)
                self.state["plot"] = dpg.add_plot(label="Sample Plot", height=200, width=400)
                self.state["x_axis"] = dpg.add_plot_axis(dpg.mvXAxis, label="X Axis", parent=self.state["plot"])
                self.state["y_axis"] = dpg.add_plot_axis(dpg.mvYAxis, label="Y Axis", parent=self.state["plot"])

                self.state["line_series"] = dpg.add_line_series(
                    self.state["char-left"],
                    self.state["char-right"],
                    label="Line",
                    parent=self.state["y_axis"]
                )
            
            self.is_built = True
        except Exception as ex:
            self.logger.error(f"Error building page with tag {self.tag}: {type(ex)}, {ex.args}")

    def update(self):
        try:
            self.state['char-left'] = [0, 11, 22, 34, 22, 11, 0]
            self.state['char-right'] = [0, 13, 25, 35,]

            dpg.set_value(self.state["line_series"], [self.state["char-left"], self.state["char-right"]])
        except Exception as ex:
            self.logger.error(f"Error updating state of page with tag {self.tag}: {type(ex)}, {ex.args}")
