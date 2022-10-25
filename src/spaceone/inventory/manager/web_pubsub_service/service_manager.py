import time
import logging
from spaceone.inventory.libs.manager import AzureManager
from spaceone.inventory.libs.schema.base import ReferenceModel
from spaceone.core.utils import *
from spaceone.inventory.model.web_pubsub_service.cloud_service_type import CLOUD_SERVICE_TYPES
from spaceone.inventory.connector.web_pubsub_service.connector import WebPubSubServiceConnector
_LOGGER = logging.getLogger(__name__)


class WebPubSubServiceManager(AzureManager):
    connector_name = 'WebPubSubServiceConnector'
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
                CloudServiceResponse (list) : list of azure web pubsub service data resource information
                ErrorResourceResponse (list) : list of error resource information


        """

        _LOGGER.debug(f'** Web PubSub Service START **')
        start_time = time.time()
        subscription_info = params['subscription_info']
        container_instances_responses = []
        error_responses = []

        web_pubsub_service_conn: WebPubSubServiceConnector = self.locator.get_connector(self.connector_name, **params)
        web_pubsub_services = web_pubsub_service_conn.list_by_subscription()

        for web_pubsub_service in web_pubsub_services:
            web_pubsub_service_id = ''
            try:
                web_pubsub_service_dict = self.convert_nested_dictionary(web_pubsub_service)
                # import pprint
                # pprint.pprint(web_pubsub_service_dict)
            except Exception as e:
                _LOGGER.error(f'[list_instances] {web_pubsub_service_id} {e}', exc_info=True)
                error_response = self.generate_resource_error_response(e, 'Service', 'WebPubSubService',
                                                                       web_pubsub_service_id)
                error_responses.append(error_response)

        _LOGGER.debug(f'** Web PubSub Service Finished {time.time() - start_time} Seconds **')
        return container_instances_responses, error_responses
