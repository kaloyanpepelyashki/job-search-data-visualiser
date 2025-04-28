import logging

from config import GOOGLE_SPREADSHEET_ID
from infrastructure.exceptions.google_sheets_exceptions import DataFetchException, OperationException
from .google_sheets_service import GoogleSheetsService

logger = logging.getLogger(__name__)

class JobTrackerDataProvider:

    def __init__(self, google_sheets_service: GoogleSheetsService):
        logger.info(f"Initilising {self.__class__.__name__}")
        try:
            self.google_sheets_service = google_sheets_service
        except Exception as ex:
            logger.error(f"Error initilising {self.__class__.__name__}: {type(ex)}, {ex.args}")
            raise ex

    async def get_all_job_applications(self, sheet_id: str = GOOGLE_SPREADSHEET_ID):
        '''
        In charge of fetching all job applications from the sheet specified in the environment of the app
        '''
        try:
            sheet_last_value = await self.google_sheets_service.get_range_end_value(sheet_id, "Sheet1")

            if sheet_last_value is None:
                logger.error("Failed to determine last value for range. sheet_last_value is None")
                raise OperationException("Failed to compose range")

            range = self.google_sheets_service.compose_range("Sheet1", "B", "4", sheet_last_value['column_label'], sheet_last_value['row_number'])

            data = await self.google_sheets_service.get_all_cells(GOOGLE_SPREADSHEET_ID, range)

            if not data:
                logger.info("No job application data found")

            return data
        
        except Exception as ex:
            logger.error(f"Error getting all job applications {type(ex)}, {ex.args}")
            return ex

        except DataFetchException as ex:
            logger.error(f"Error getting all job applications {type(ex)}, {ex.args}")
            return ex
        except OperationException as ex:
            logger.error(f"Error getting all job applications {type(ex)}, {ex.args}")
            return ex
