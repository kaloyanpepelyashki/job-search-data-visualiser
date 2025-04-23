import asyncio
import queue
import threading
import logging

logger = logging.getLogger(__name__)

class AsyncManager :
    '''
    This class is in charge of handling async tasks
    '''

    def __init__(self):
        try:
            self.loop = asyncio.new_event_loop()
            self.queue = queue.Queue()
            self.thread = threading.Thread(target=self._start_loop, deamon=True)
            self.thread.start()
        except Exception as ex:
            logger.error(f"Error initialising async manager: {type(ex)}, {ex.args}")
        else:
            logger.info("Async initialised successfully")
    

    def _start_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()


    def run_async_task(self, coroutine, callback=None):

        async def wrapper():
            try:
                result = await coroutine
                self.queue.put((result, callback))
            except Exception as ex:
                logger.error("Error running async task: {type(ex)} {ex.args}")
                self.queue.put((ex, callback))
        
        asyncio.run_coroutine_threadsafe(wrapper(), self.loop)


    def check_queue(self):
        while self.queue.not_empty():
            result, callback = self.queue.get()
            if callback:
                callback(result)




async_manager = AsyncManager()