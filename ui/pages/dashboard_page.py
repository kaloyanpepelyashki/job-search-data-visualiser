import logging
import dearpygui.dearpygui as dpg
from .base_page import BasePage
from infrastructure.runtime import async_manager


class DashboardPage(BasePage):
    def __init__(self, parent_window_tag, width, height):
        super().__init__(tag="dashboard", visible=False, parent_window_tag=parent_window_tag)
        self.state["width"]= int(width)
        self.state["height"] = int(height)
        self.state["char-left"] = [0, 1, 12, 22]
        self.state["char-right"] = [0, 3, 15, 25]
    
    def build(self):
        """
        Constructs the dashboard UI components using the DearPyGui widgets..
        It sets `is_built` to True once construction is successful. Indicating that the page (UI) has already been built once

        Exceptions are logged if any errors occur during UI construction.
        """
        try:
            self.logger.info(f"Building {self.__class__.__name__} UI")
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

                dpg.add_text("", tag="error_text")
            
            self._fetch_data()
            self.is_built = True
        except Exception as ex:
            self.logger.error(f"Error building page with tag {self.tag}: {type(ex)}, {ex.args}")


    def _fetch_data(self):
        try:
            async def _fetch():
                try:
                    self.logger.info("Fetching data")
                    job_tracker_data_provider = self.service_manager.get_service("job_tracker_data_provider")
                    data = await job_tracker_data_provider.get_all_job_applications()
                    
                    return data
                except Exception as ex:
                    self.logger.error(f"Error fetching data: {type(ex)}, {ex.args}")
                    raise ex

            def on_complete(data):
                if isinstance(data, Exception):
                    dpg.set_value("error_text", "Error fetching")
                else:
                    print("Data after fetch of data", data)
                    dpg.set_value("error_text", data)
                
            async_manager.run_async_task(_fetch(), callback=on_complete)

        except Exception as ex:
            self.logger.error(f"Error fetching data {type(ex)}, {ex.args}")


    def update(self):
        try:
            self.state['char-left'] = [0, 11, 22, 34, 22, 11, 0]
            self.state['char-right'] = [0, 13, 25, 35,]

            dpg.set_value(self.state["line_series"], [self.state["char-left"], self.state["char-right"]])
        except Exception as ex:
            self.logger.error(f"Error updating state of page with tag {self.tag}: {type(ex)}, {ex.args}")
