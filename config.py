from dotenv import load_dotenv
import os

load_dotenv()
#ALL CONFIGURATIONS GO HERE

#ALL GLOBAL APPLICATION CONFIG ===== >
APP_NAME = "Job Search Data Visualiser"
APP_NAME_SHORT = "JSDV"
VERSION = "0.0.1"
DEBUG = True

#ALL GUI CONFIG ---- >
WINDOW_WIDTH = 2560
WINDOW_HEIGHT = 1600
APP_THEME_IS_DARK = False

#<-- TYPE FACE
DEFAULT_FONT = ("Arial", 12)
#<--
#< ----
#< =====

#API CONFIG ===== >
GOOGLE_API_SCOPES = os.getenv("GOOGLE_API_SCOPES")
GOOGLE_SPREADSHEET_ID = os.getenv("GOOGLE_SPREADSHEET_ID")

#< =====
