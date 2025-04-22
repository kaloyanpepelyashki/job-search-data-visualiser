import logging

from config import GOOGLE_SPREADSHEET_ID
from infrastructure.exceptions.google_sheets_exceptions import DataFetchException, OperationException
from .google_sheets_service import GoogleSheetsService

logger = logging.getLogger(__name__)

class JobTrackerDataProvider:

    def __init__(self, google_sheets_service: GoogleSheetsService):
        self.google_sheets_service = google_sheets_service


    #//TODO Test if this method works properly
    def get_all_job_applications(self):
        '''
        In charge of fetching all job applications from the sheet specified in the environment of the app
        '''
        try:
            sheet_last_value = self.google_sheets_service.get_range_end_value()

            if sheet_last_value is None:
                logger.error("Failed to determince last value for range. sheet_last_value is None")
                raise OperationException("Failed to compose range")

            range = self.google_sheets_service.compose_range("Sheet1", "B", "4", sheet_last_value['column_label'], sheet_last_value['row_number'])

            data = self.google_sheets_service.get_all_cells(GOOGLE_SPREADSHEET_ID, range)

            if not data:
                logger.info("No job application data found")

            return data
        
        #//TODO Implement the exception cases
        except Exception as ex:
            logger.error(f"Error getting all job applications {type(ex)}, {ex.args}")

            pass
        except DataFetchException as ex:
            pass
        except OperationException as ex:
            pass