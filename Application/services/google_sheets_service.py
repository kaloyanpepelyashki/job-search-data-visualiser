import logging
from config import GOOGLE_SPREADSHEET_ID
from infrastructure.api import GoogleAPIClient

from infrastructure.exceptions import APIException
from infrastructure.exceptions import DataFetchException


logger = logging.get_logger(__name__)
class GoogleSheetsService:

    def __init__(self, google_api_client: GoogleAPIClient):
        self.google_api = google_api_client


    def get_all_cells(self):
        sheet_id: str = GOOGLE_SPREADSHEET_ID

        try:
            #//TODO Implement the rest of the logic for getting cell values and returnting them
            #//TODO The logic must have a dynamic way of fetching cells (dynamic way of defining the range, as cells will continue to grow, as new data is added)
            cells = self.google_api.get_cells_in_range(sheet_id, "A3:T30")
        except APIException as ex:
            logger.error(f"Error getting all cells: {type(ex)}, {ex.args}")
            raise DataFetchException("Unable to fetch tasks at this time") from ex