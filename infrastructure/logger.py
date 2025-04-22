import logging
import logging.config
from config import DEBUG

def setup_logger():
    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '>LOG at [%(asctime)s]: %(levelname)s in %(module)s: %(message)s',
            },
            'error' : {
                'format': '>ERROR at [%(asctime)s]: %(levelname)s in %(module)s: %(message)s'
            },
            'debug' : {
                'format' : '>(DEBUG) [%(asctime)s]: %(levelname)s in %(module)s: %(message)s'
            }
        },
        'handlers': {
            'console_info': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': 'INFO',
            },
            'console_error': {
                'class': 'logging.StreamHandler',
                'formatter': 'error',
                'level': 'ERROR',
            },
            'console_debug': {
                'class': 'logging.StreamHandler',
                'formatter': 'debug',
                'level': 'DEBUG',
            },
            'file_info': {
                'class': 'logging.FileHandler',
                'filename': 'app.log',
                'formatter': 'default',
                'level': "INFO"
            },
            'file_error': {
                'class': 'logging.FileHandler',
                'filename': 'app.log',
                'formatter': 'error',
                'level': "ERROR"
            },
            'file_debug': {
                'class': 'logging.FileHandler',
                'filename': 'app.log',
                'formatter': 'debug',
                'level': 'DEBUG',
            },
        },
        'root': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'handlers': ['file_info', 'file_error', 'file_debug', 'console_info', 'console_error', 'console_debug'],
        },
    })
