import time
import logging
from spaceone.inventory.libs.manager import AzureManager
from spaceone.inventory.libs.schema.base import ReferenceModel
from spaceone.core.utils import *
from spaceone.inventory.model.function_app.cloud_service_type import CLOUD_SERVICE_TYPES
from spaceone.inventory.connector.function_app.connector import FunctionAppConnector

from spaceone.inventory.model.function_app.data import *
from spaceone.inventory.model.function_app.cloud_service import *

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
                function_app_id = function_app_dict['id']
                resource_group_name = self.get_resource_group_from_id(function_app_id)

                # list
                functions = function_app_conn.list_functions(resource_group_name, name=function_app_dict['name'])
                functions_data = [self.convert_nested_dictionary(function) for function in functions]

                for f in functions_data:
                    import pprint
                    pprint.pprint(f)

                # Update data info of Function App
                function_app_dict.update({
                    'resource_group': resource_group_name,
                    'subscription_id': subscription_info['subscription_id'],
                    'subscription_name': subscription_info['subscription_name'],
                    'azure_monitor': {'resource_id': function_app_id},
                    'os_system_display': self._get_os_system_from_kind(function_app_dict.get('kind', None)),
                    'app_service_plan_display': self._get_app_service_plan_from_server_farm_id(
                        function_app_dict.get('server_farm_id', None)),
                    'functions': functions_data
                })

                function_app_data = FunctionApp(function_app_dict, strict=False)

                import pprint
                pprint.pprint(function_app_dict)
                # Update resource info of Function App
                function_app_resource = FunctionAppResource({
                    'name': function_app_data.name,
                    'account': function_app_dict['subscription_id'],
                    'data': function_app_data,
                    'tags': function_app_dict.get('tags', {}),
                    'region_code': function_app_data.location,
                    'reference': ReferenceModel(function_app_data.reference())
                })
                self.set_region_code(function_app_data.location)
                function_app_responses.append(FunctionAppResponse({'resource': function_app_resource}))
            except Exception as e:
                _LOGGER.error(f'[list_instances] {function_app_id} {e}', exc_info=True)
                error_response = self.generate_resource_error_response(e, 'Instance', 'FunctionApp', function_app_id)
                error_responses.append(error_response)

        _LOGGER.debug(f'** Function App Service Finished {time.time() - start_time} Seconds **')
        return function_app_responses, error_responses

    @staticmethod
    def _get_os_system_from_kind(kind):
        if kind is not None:
            return kind.split(',')[1]

    @staticmethod
    def _get_app_service_plan_from_server_farm_id(server_farm_id):
        if server_farm_id is not None:
            return server_farm_id.split('/')[-1]
