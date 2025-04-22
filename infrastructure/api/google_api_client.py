import logging
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from infrastructure.file_system import read_from_json
from infrastructure.exceptions import APIException, AuthException


logger = logging.getLogger(__name__)

class GoogleAPIClient:
    #Note: The class can contain implementations for calling more than one google APIs if needed
    '''
    This class provides an access point for talking to the Google APIs (all APIs, not limited to one)
    The class contains methods for reading or appending values to/from google sheets
    The class must be implemented by a higher level service class. 
    Must not be called directly in application logic
    '''

    def __init__(self):
       #Google Sheets API service (only accesses the sheets API)
       self.sheet_api_service = None
       try:
        self.creds = read_from_json("google-api-token.json")

        if not self.creds:
            raise AuthException("Failed to fetch auth token, failed to authenticate")

        self.sheet_api_service = build("sheets", version="v4", credentials=self.creds)
       except Exception as ex:
          logger.error(f"Error initialising class: {type(ex)}, {ex.args}")
    

    def get_cells_in_range(self, sheet_id: str, range: str):
        '''
        Retrieves the values from a specified range in a Google Sheet using the Sheets API.

        Parameters:
            sheet_id (str): The ID of the Google Sheet.
            range (str): The A1 notation of the range to retrieve data from.

        Raises:
            RuntimeError: If the API client is not initialized.
            APIException: If the retrieval operation fails due to an API or unexpected error.

        Returns:
            list: A list of rows, where each row is a list of cell values. Returns an empty list if no values are found.
        '''
        if not self.sheet_api_service:
            raise RuntimeError("GoogleAPIClient is not initialized. OAuth flow might still be pending.")
        
        try:
            sheet = self.sheet_api_service.spreadsheets()

            result = (sheet.values()
                     .get(spreadsheetId=sheet_id, range=range)
                     .execute()
                    )
        
            values = result.get("values", [])
        
            if not values:
                logger.info(f"No values were returend for range {range} in sheet")
                return values
            else:
                return values
        except HttpError as ex:
            logging.debug(f"Error getting cells for range {range} : {type(ex)}, {ex.args}")
            raise APIException("Failed to fetch cells for requested range from requested sheet") from ex
        except Exception as ex:
            logging.debug(f"Error getting cells for range {range} : {type(ex)}, {ex.args}")
            raise APIException("Failed to fetch cells for requested range from requested sheet") from ex
    
    
    def append_values_in_range(self, sheet_id: str, range: str, value_input_option: str, values):
        '''
        Appends a list of values to a specified range in a Google Sheet using the Sheets API.

        Parameters:
            sheet_id (str): The ID of the Google Sheet.
            range (str): The A1 notation of the range to append data to. Example: A:D (Assumes the first sheet is targeted) Sheet1!A:H or Sheet1!A:D or Sheet4!A1:F3
            value_input_option (str): How the input data should be interpreted (e.g., 'RAW' or 'USER_ENTERED').
            values (list): The data to append, structured as a list of lists.

        Raises:
            RuntimeError: If the API client is not initialized.
            APIException: If the append operation fails due to an API or unexpected error.

        Returns:
            dict: The response from the Sheets API containing metadata about the update.
        '''

            
        if not self.sheet_api_service:
            raise RuntimeError("GoogleAPIClient is not initialized. OAuth flow might still be pending.")

        try:
            sheet = self.sheet_api_service.spreadsheets()

            result = (sheet.values()
                    .append(
                        spreadsheetId= sheet_id,
                        range=range,
                        valueInputOption=value_input_option,
                        body={"values": values}
                    )
            ).execute()


            logger.info(f"{(result.get('updates').get('updatedCells'))} cells appended.")

            return result
    
        except HttpError as ex:
            logging.debug(f"Error appending values for range {range} : {type(ex)}, {ex.args}")
            raise APIException("Failed to append values for requested range to requested sheet") from ex
        except Exception as ex:
            logging.debug(f"Error appending values for range {range} : {type(ex)}, {ex.args}")
            raise APIException("Failed to append values for requested range to requested sheet") from ex