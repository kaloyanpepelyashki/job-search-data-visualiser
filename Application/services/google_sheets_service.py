import logging
import string

from infrastructure.api import GoogleAPIClient

from infrastructure.exceptions import APIException
from infrastructure.exceptions import DataFetchException, OperationException
from infrastructure.exceptions.authentication_exception import AuthException


logger = logging.getLogger(__name__)

class GoogleSheetsService:

    def __init__(self, google_api_client: GoogleAPIClient):
        logger.info(f"Initilising {self.__class__.__name__}")
        try:
            self.google_api = google_api_client
        except AuthException as ex:
            logger.error(f"Error initilising {self.__class__.__name__}: {type(ex)}, {ex.args}")
            raise ex


    #//TODO Test this method, still not tested
    async def get_range_end_value(self, google_sheet_id: str, sheet_tab: str):
        '''
        Determines the last populated cell's position (row and column) in a specified Google Sheet tab.

        This method fetches all populated cells from the given sheet tab and calculates the 
        last populated row number and column label based on the data structure returned.

        Parameters:
            google_sheet_id (str): The ID of the Google Sheet to target.
            sheet_tab (str): The specific tab (worksheet name) within the sheet to inspect.

        Returns:
            dict or None: A dictionary containing:
                      - 'column_label' (str): The alphabetical label of the last populated column.
                      - 'row_number' (int): The number of the last populated row.
                      Returns None if no populated cells are found.
        '''
        sheet_id: str = google_sheet_id
        alphabet = list(string.ascii_uppercase)

        try:

            populated_cells = await self.google_api.get_cells_in_range(sheet_id=sheet_id, range=sheet_tab)

            if not populated_cells:
                logger.error("Failed to fetch populated cells in _get_range_end_value method")
                return None


            end_value = {'column_label': alphabet[len(populated_cells[0]) + 1], 'row_number': len(populated_cells)}
            return end_value

        except APIException as ex:
            logger.error(f"Error getting all cells: {type(ex)}, {ex.args}")
            raise DataFetchException("Unable to fetch cells at this time") from ex
        except Exception as ex:
            logger.error(f"Failed to get range end value: {type(ex)}, {ex.args}")
            raise OperationException("Failed to complete get range end value operation") from ex

    #//TODO Test this method, still not tested
    def compose_range(self, sheet, range_start_column, range_start_row, range_end_column, range_end_row):
        range = f"{sheet}!{range_start_column}{range_start_row}:{range_end_column}{range_end_row}"

        return range

    #//TODO Test this method, still not tested
    def get_all_cells(self, google_sheet_id: str, range):
        '''
        Retrieves all cell values from a specified range in a Google Sheet.

        Parameters:
            google_sheet_id (str): The ID of the Google Sheet to read from.
            range (str): The cell range to fetch (e.g., "A1:D10").

        Returns:
            list[list[str]] or None: A 2D list containing the values of the cells if present, or None if the range is empty.
        '''
        sheet_id: str = google_sheet_id

        try:
            cells = self.google_api.get_cells_in_range(sheet_id, range)

            if not cells:
                logger.info("No data was fetched from sheet")
            
            return cells

        except APIException as ex:
            logger.error(f"Error getting all cells: {type(ex)}, {ex.args}")
            raise DataFetchException("Unable to fetch cells at this time") from ex

    #//TODO Test this method, still not tested
    def append_row(self, google_sheet_id: str, range: str, values):
        '''
        This method is in charge of appending a row of values in the sheet
        It appends a row, after the last populated row of the sheet
           Parameters:
            values (arr): The values to be appended, by columns
        '''
        sheet_id: str = google_sheet_id

        try:
            self.google_api.append_values_in_range(sheet_id, range, "USER_ENTERED", values=values)
        except APIException as ex:
            logger.error(f"Error appending row {type(ex)}, {ex.args}")
            raise OperationException("Unable to completre append operations") from ex