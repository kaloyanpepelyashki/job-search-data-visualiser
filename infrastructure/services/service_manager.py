import logging 
from infrastructure.api import GoogleAPIClient
from application.services import GoogleSheetsService, JobTrackerDataProvider

logger = logging.getLogger(__name__)

class ServiceManager:
    '''
    This class is responsible for managing services. The class initilises services  
    and provides an access point to them to the rest of the application
    '''
    def __init__(self):
        self._low_level_services = {} #Lower level services must be only called/implemented by other (higher level) services
        self._high_level_services = {} #Higher level services can be called by the UI or other levels of the application

    
    def _register_lower_level(self, name: str, service):
        '''
        This method is soley responsible for registering lower level services to the _low_level_services registry
        The method may only be used internally
        '''
        self._low_level_services[name] = service


    def _register_high_level(self, name: str, service):
        '''
        This method is soley responsible for registering higher level services to the _high_level_services registry
        The method may only be used internally
        '''
        self._high_level_services[name] = service

    def _get_low_level_service(self, service_name: str):
        '''
        This method is in charge of getting the low level services by name. The method can and must only be used internally in this class. 
        '''
        return self._low_level_services[service_name]

    def get_service(self, service_name: str):
        try:
            return self._high_level_services[service_name]
        except KeyError:
            logger.error(f"Error getting service. Service '{service_name}' is not registered.")
            raise ValueError(f"Service '{service_name}' is not registered.")
    

    def _set_up_lower_level(self) : 
        try:
            google_api_client = GoogleAPIClient()
            self._register_low_level("google_api_client", google_api_client)
        except Exception as ex:
            logger.error(F"Error setting up lower level services. {type(ex)}, {ex.args}")
            return ex
        
    def _set_up_high_level(self):
        try:
            google_sheets_service = GoogleSheetsService(self._get_low_level_service("google_api_client"))
            self._register_high_level("google_sheets_service", google_sheets_service)

            job_tacker_provider = JobTrackerDataProvider(self.get_service("google_sheets_service"))
            self._register_high_level("job_tracker_data_provider", job_tacker_provider)
        except Exception as ex:
            logger.error(F"Error setting up higher level services. {type(ex)}, {ex.args}")
            return ex

    
    def set_up_services(self):
        self._set_up_lower_level()
        self._set_up_high_level()


service_manager = ServiceManager()
service_manager.set_up_services() 