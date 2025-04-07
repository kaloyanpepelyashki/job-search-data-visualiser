from .base_page import BasePage
import dearpygui.dearpygui as dpg

class DashboardPage(BasePage):
    def __init__(self, width, height):
        super().__init__(tag="dashboard_page", visible=True)
        self.state["width"]= int(width)
        self.state["height"] = int(height)
    
    def build(self):
        width = self.state.get("width", 600)
        height = self.state.get("height", 400)
        with dpg.window(label="Dashboard", tag=self.tag, show=self.visible, width=200, height=200):
            dpg.add_text("📊 Dashboard Overview page")
            dpg.add_button(label="Refresh Chart", callback=self.update)
            self.state["plot"] = dpg.add_plot(label="Sample Plot", height=200, width=400)
            self.state["x_axis"] = dpg.add_plot_axis(dpg.mvXAxis, label="X Axis", parent=self.state["plot"])
            self.state["y_axis"] = dpg.add_plot_axis(dpg.mvYAxis, label="Y Axis", parent=self.state["plot"])
            dpg.add_line_series([0, 1, 2], [0, 1, 4], label="Line", parent=self.state["y_axis"])
