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

    def list_slots(self, resource_group_name, name):
        return self.function_app_client.web_apps.list_slots(resource_group_name=resource_group_name, name=name)

    def get_configuration(self, resource_group_name, name):
        return self.function_app_client.web_apps.get_configuration(resource_group_name=resource_group_name, name=name)

    def list_metadata(self, resource_group_name, name):
        return self.function_app_client.web_apps.list_metadata(resource_group_name=resource_group_name, name=name)
