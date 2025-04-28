import asyncio
import queue
import threading
import logging
import dearpygui.dearpygui as dpg

logger = logging.getLogger(__name__)

class AsyncManager :
    '''
    This class is in charge of handling async tasks
    '''

    def __init__(self):
        try:
            self.loop = asyncio.new_event_loop()
            self.queue = queue.Queue()
            self.thread = threading.Thread(target=self._start_loop, daemon=True)
            self.thread.start()
        except Exception as ex:
            logger.error(f"Error initialising async manager: {type(ex)}, {ex.args}")
        else:
            logger.info("Async initialised successfully")
    

    def _start_loop(self):
        """
        Starts the asyncio event loop in a dedicated thread.

        This method sets the current thread's event loop to the one created during initialization 
        and runs it indefinitely. It is intended to be run in a background thread so that async 
        tasks can be handled separately from the main thread.
        """
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()


    def run_async_task(self, coroutine, callback=None):
        """
        Submits a coroutine to be executed asynchronously on the background event loop, without interupting the execution of the main loop.

        Args:
            coroutine (Coroutine): The coroutine to be executed.
            callback (Callable, optional): A function to be called with the result of the coroutine 
                                        once it finishes. If the coroutine raises an exception, 
                                        the exception is passed to the callback instead.

        This method wraps the coroutine execution to catch exceptions and places the result or 
        exception into a thread-safe queue for later handling. The execution is thread-safe and 
        submitted to the internal asyncio loop.
        """
        async def wrapper():
            try:
                result = await coroutine
                self.queue.put((result, callback))
            except Exception as ex:
                logger.error(f"Error running async task: {type(ex)} {ex.args}")
                self.queue.put((ex, callback))
        
        asyncio.run_coroutine_threadsafe(wrapper(), self.loop)


    def check_queue(self):
        """
        Checks the result queue for completed tasks and invokes their associated callbacks.

        This method processes all items currently in the queue. For each item, it unpacks the result 
        and the callback function, and if a callback is present, it calls it with the result or exception.

        Intended to be called regularly (e.g., every frame or on a timer) to ensure that async task 
        results are handled in the main thread context.
        """
        while not self.queue.empty():
            result, callback = self.queue.get()
            if callback:
                callback(result)


    def start_polling(self, interval_frames= 1):
        """
        Starts polling the result queue at a regular interval defined by GUI frame updates.

        Args:
            interval_frames (int): Number of frames to wait between each polling action.

        This method integrates with DearPyGui's frame system to repeatedly call check_queue(). 
        It ensures that any async results are delivered to the main thread via callbacks without 
        blocking or needing a separate polling thread.
        """
        def _poll():
            self.check_queue()
            dpg.set_frame_callback(interval_frames, _poll)
        
        dpg.set_frame_callback(1, _poll)




async_manager = AsyncManager()