from .base_page import BasePage
import dearpygui.dearpygui as dpg

class DashboardPage(BasePage):
    def __init__(self, width, height):
        super().__init__(tag="dashboard_page", visible=False)
        self.state["width"]= int(width)
        self.state["height"] = int(height)
        self.state["char-left"] = [0, 1, 12, 22]
        self.state["char-right"] = [0, 3, 15, 25]
    
    def build(self):
        print("Dashboard tag:", self.tag)
        width = int(self.state.get("width", 600))
        height = int(self.state.get("height", 400))

        with dpg.window(label="Dashboard", tag=str(self.tag), show=self.visible, width=width, height=height):
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


    def update(self):
        self.state['char-left'] = [0, 11, 22, 34, 22, 11, 0]
        self.state['char-right'] = [0, 13, 25, 35,]

        dpg.set_value(self.state["line_series"], [self.state["char-left"], self.state["char-right"]])
