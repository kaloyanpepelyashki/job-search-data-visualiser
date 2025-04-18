import logging
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from infrastructure.file_system import read_from_json


logger = logging.getLogger(__name__)

class GoogleAPIClient:

    def __init__(self):
       self.api_service = None
       try:
        self.creds = read_from_json("google-api-token.json")
        self.api_service = build("sheets", version="v4", credentials=self.creds)
       except Exception as ex:
          logger.error(f"Error initialising class: {type(ex)}, {ex.args}")
    

    def get_cells_in_range(self, sheet_id: str, range: str):
        if not self.api_service:
            raise RuntimeError("GoogleAPIClient is not initialized. OAuth flow might still be pending.")
        
        try:
            sheet = self.api_service.spreadsheets()

            result = (sheet.values()
                     .get(spreadsheetId=sheet_id, range=range)
                     .execute()
                    )
        
            values = result.get("values", [])
        
            if not values:
                logger.info(f"No values were returend for range {range} in sheet")
            else:
                return values
        except HttpError as ex:
            logging.error(f"Error getting cells for range {range} : {type(ex)}, {ex.args}")
            return ex
        except Exception as ex:
            logging.error(f"Error getting cells for range {range} : {type(ex)}, {ex.args}")
            return ex