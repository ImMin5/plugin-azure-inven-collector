import time
import logging
from spaceone.inventory.libs.manager import AzureManager
from spaceone.inventory.libs.schema.base import ReferenceModel
from spaceone.core.utils import *
from spaceone.inventory.model.web_pubsub_service.cloud_service_type import CLOUD_SERVICE_TYPES

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
        container_instances_responses = []
        error_responses = []

        _LOGGER.debug(f'** Function App Service Finished {time.time() - start_time} Seconds **')
        return container_instances_responses, error_responses