import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
import logging
from config import GOOGLE_API_SCOPES
from infrastructure.file_system import write_to_json
from infrastructure.exceptions import AuthException

logger = logging.getLogger(__name__)

async def authenticate_for_google():
    """
    Authenticates with Google Sheets API and returns credentials.
    This method must be called on initiation of the application or before using the google_api_client class.
    It is required to authenticate for google, to access the APIs
    """
    
    SCOPES = [GOOGLE_API_SCOPES]
    creds = None

    try:
        if os.path.exists("google-api-token.json"):
            creds = Credentials.from_authorized_user_file("google-api-token.json", SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                "google-credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)

            write_to_json("google-api-token.json", creds)

    except Exception as ex:
        logger.error(f"Error authenticating for google: {type(ex)}, {ex.args}")
        raise AuthException("Failed to authenticate for google") from ex