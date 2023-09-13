import logging

from spaceone.inventory.libs.connector import AzureConnector
from spaceone.inventory.error.custom import *

__all__ = ['SSHKeysConnector']
_LOGGER = logging.getLogger(__name__)


class SSHKeysConnector(AzureConnector):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_connect(kwargs.get('secret_data'))

    def list_keys(self):
        return self.compute_client.ssh_public_keys.list_by_subscription()
