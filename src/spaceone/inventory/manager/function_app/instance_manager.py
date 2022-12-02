import json
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

        # https://learn.microsoft.com/en-us/rest/api/appservice/web-apps/list-application-settings#code-try-0
        # https://learn.microsoft.com/en-us/rest/api/appservice/web-apps/list-configurations#code-try-0
        # https://learn.microsoft.com/en-us/rest/api/appservice/web-apps/list-slots#code-try-0

        for function_app in function_apps:
            function_app_id = ''
            try:
                function_app_dict = self.convert_nested_dictionary(function_app)
                function_app_id = function_app_dict['id']
                resource_group_name = self.get_resource_group_from_id(function_app_id)

                # Functions in Function App
                functions = function_app_conn.list_functions(resource_group_name, name=function_app_dict['name'])
                functions_dict = [self.convert_nested_dictionary(function) for function in functions]


                for function_dict in functions_dict:
                    import pprint
                    pprint.pprint(function_dict)
                    function_dict.update({
                        'name_display': self._get_function_name_from_id(function_dict['id']),
                        'status_display': self._convert_status_from_is_disabled(function_dict['is_disabled']),
                        'config_display': self._make_config_dict_display(function_dict['config'])
                    })

                # Deployment slot in Function App
                deployment_slots = function_app_conn.list_slots(resource_group_name, name=function_app_dict['name'])

                deployment_slots_dict = [self.convert_nested_dictionary(deployment_slot)
                                         for deployment_slot in deployment_slots]

                for deployment_slot_dict in deployment_slots_dict:
                    deployment_slot_dict.update({
                        'os_system_display': self._get_os_system_from_kind(deployment_slot_dict.get('kind', None)),
                        'app_service_plan_display': self._get_app_service_plan_from_server_farm_id(
                            deployment_slot_dict.get('server_farm_id', None))
                    })

                # Update data info of Function App
                function_app_dict.update({
                    'resource_group': resource_group_name,
                    'subscription_id': subscription_info['subscription_id'],
                    'subscription_name': subscription_info['subscription_name'],
                    'azure_monitor': {'resource_id': function_app_id},
                    'os_system_display': self._get_os_system_from_kind(function_app_dict.get('kind', None)),
                    'app_service_plan_display': self._get_app_service_plan_from_server_farm_id(
                        function_app_dict.get('server_farm_id', None)),
                    'functions': functions_dict,
                    'functions_count_display': len(functions_dict),
                    'deployment_slots': deployment_slots_dict
                })

                function_app_data = FunctionApp(function_app_dict, strict=False)

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

    @staticmethod
    def _get_function_name_from_id(function_id):
        return function_id.split('/')[-1]

    @staticmethod  # need code review
    def _convert_status_from_is_disabled(is_disabled):
        return 'Disabled' if is_disabled else 'Enabled'

    @staticmethod
    def _make_config_dict_display(config):
        config_display_dict = {}
        config_bindings = config.get('bindings')
        config_display_dict.update({
            'name': config_bindings[0].get('name', None),
            'authLevel': config_bindings[0].get('authLevel', None),
            'request_type': config_bindings[0].get('type', None),
            'request_method': config_bindings[0].get('methods', []),
            'details': json.dumps(config)  # need refactoring
        })
        if len(config_bindings) > 1:
            config_display_dict.update({
                'response_type': config_bindings[1].get('type', None)
            })
        return config_display_dict
