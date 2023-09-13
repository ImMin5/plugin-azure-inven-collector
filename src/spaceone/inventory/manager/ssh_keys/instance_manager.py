import datetime
import time
import logging

from spaceone.inventory.connector.ssh_keys import SSHKeysConnector
from spaceone.inventory.libs.manager import AzureManager
from spaceone.inventory.model.ssh_keys.cloud_service import *
from spaceone.inventory.model.ssh_keys.cloud_service_type import CLOUD_SERVICE_TYPES
from spaceone.inventory.model.ssh_keys.data import *

_LOGGER = logging.getLogger(__name__)


class SSHKeysManager(AzureManager):
    connector_name = 'SSHKeysConnector'
    cloud_service_types = CLOUD_SERVICE_TYPES

    def collect_cloud_service(self, params):
        """
            Args:
                 params (dict): {
                    'options': 'dict',
                    'schema': 'str'
                    'secret_data': 'dict',
                    'filter': 'dict'
                }
            Response:
                CloudServiceResponse (list) : list of azure ssh keys data resource information
                ErrorResourceResponse (list) : list of error resource information
        """
        _LOGGER.debug('** SSH Keys START **')
        start_time = time.time()
        subscription_info = params['subscription_info']

        ssh_keys_conn: SSHKeysConnector = self.locator.get_connector(self.connector_name, **params)

        ssh_keys_responses = []
        error_responses = []



        try:
            subscription_id = subscription_info['subscription_id']
            ssh_key_list = ssh_keys_conn.list_keys()
            for ssh_key in ssh_key_list:
                print(ssh_key)

        except Exception as e:
            print(f'[ERROR: {e}]')


        _LOGGER.debug(f'** Application Gateway Finished {time.time() - start_time} Seconds **')
        return ssh_keys_responses, error_responses
