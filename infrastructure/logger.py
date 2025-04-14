import logging
import logging.config
from config import DEBUG

logger = logging.getLogger(__name__)

def setup_logger():
    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
        },
        'handlers': {
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'app.log',
                'formatter': 'default',
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
        },
        'root': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'handlers': ['file', 'console'],
        },
    })


def info_log(log_message: str):
    logger.info(log_message)

def error_log(log_message: str):
    logger.error(log_message)
