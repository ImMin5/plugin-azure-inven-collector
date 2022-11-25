import logging
from spaceone.inventory.libs.connector import AzureConnector

__all__ = ['FunctionAppConnector']
_LOGGER = logging.getLogger(__name__)


class FunctionAppConnector(AzureConnector):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_connect(kwargs.get('secret_data'))

    def list(self):
        return self.function_app_client.web_apps.list()

    def list_functions(self, resource_group_name, name):
        return self.function_app_client.web_apps.list_functions(resource_group_name=resource_group_name, name=name)
