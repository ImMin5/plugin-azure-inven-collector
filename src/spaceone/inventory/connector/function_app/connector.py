import logging
from spaceone.inventory.libs.connector import AzureConnector

__all__ = ['FunctionAppConnector']
_LOGGER = logging.getLogger(__name__)


class FunctionAppConnector(AzureConnector):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_connect(kwargs.get('secret_data'))
