import time
import logging
from spaceone.inventory.libs.manager import AzureManager
from spaceone.inventory.libs.schema.base import ReferenceModel
from spaceone.core.utils import *
from spaceone.inventory.model.web_pubsub_service.cloud_service_type import CLOUD_SERVICE_TYPES
from spaceone.inventory.connector.function_app.connector import FunctionAppConnector

from spaceone.inventory.model.function_app.data import *

_LOGGER = logging.getLogger(__name__)


class FunctionAppManager(AzureManager):
    connector_name = 'FunctionAppConnector'
    cloud_service_types = CLOUD_SERVICE_TYPES

    def collect_cloud_service(self, params):
        """
            Args:
                params (dict):
                    - 'options' : 'dict'
                    - 'schema' : 'str'
                    - 'secret_data' : 'dict'
                    - 'filter' : 'dict'
                    - 'zones' : 'list'
                    - 'subscription_info' :  'dict'

            Response:
                CloudServiceResponse (list) : list of azure function app data resource information
                ErrorResourceResponse (list) : list of error resource information


        """

        _LOGGER.debug(f'** Function App START **')
        start_time = time.time()
        subscription_info = params['subscription_info']
        function_app_responses = []
        error_responses = []

        function_app_conn: FunctionAppConnector = self.locator.get_connector(self.connector_name, **params)
        function_apps = function_app_conn.list()

        for function_app in function_apps:
            function_app_id = ''
            try:
                function_app_dict = self.convert_nested_dictionary(function_app)
                import pprint
                pprint.pprint(function_app_dict)

                function_app_data = FunctionApp()
            except Exception as e:
                print(e)

        _LOGGER.debug(f'** Function App Service Finished {time.time() - start_time} Seconds **')
        return function_app_responses, error_responses
