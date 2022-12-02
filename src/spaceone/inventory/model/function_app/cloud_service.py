from schematics.types import ModelType, StringType, PolyModelType, FloatType, DateTimeType
from spaceone.inventory.model.function_app.data import FunctionApp
from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, EnumDyField, ListDyField, DateTimeDyField\
    , MoreField
from spaceone.inventory.libs.schema.metadata.dynamic_layout import ItemDynamicLayout, TableDynamicLayout
from spaceone.inventory.libs.schema.cloud_service import CloudServiceResource, CloudServiceResponse, CloudServiceMeta

'''
Function App
'''

# TAB - Function App
function_app_info_meta = ItemDynamicLayout.set_fields('Function App', fields=[
    TextDyField.data_source('Name', 'name'),
    EnumDyField.data_source('Instance State', 'data.state', default_state={
        'safe': ['Running', 'Succeeded'],
        'warning': ['Pending'],
        'alert': ['Stopped', 'Failed'],
        'disable': []}),
    TextDyField.data_source('Resource ID', 'data.id'),
    TextDyField.data_source('Resource Group', 'data.resource_group'),
    TextDyField.data_source('Subscription', 'data.subscription_name'),
    TextDyField.data_source('Subscription ID', 'account'),
    TextDyField.data_source('Region', 'data.location'),
    TextDyField.data_source('URL', 'data.default_host_name'),
    TextDyField.data_source('Operating System', 'data.os_system_display'),
    TextDyField.data_source('App Service Plan', 'data.app_service_plan_display'),
    TextDyField.data_source('Functions count', 'data.functions_count_display'),
    TextDyField.data_source('Daily memory time quota', 'data.daily_memory_time_quota'),
    TextDyField.data_source('Https only', 'data.https_only'),
])

# TAB - Functions
functions_info_meta = TableDynamicLayout.set_fields('Functions', root_path='data.functions', fields=[
    TextDyField.data_source('Name', 'name_display'),
    TextDyField.data_source('Trigger', 'config_display.request_type'),
    TextDyField.data_source('Status', 'status_display'),
    TextDyField.data_source('Auth level', 'config_display.authLevel'),
    TextDyField.data_source('Language', 'language'),
    ListDyField.data_source('Request methods', 'config_display.request_methods', options={'delimiter': ', '}),
    MoreField.data_source('Details', 'details_show', options={
        'sub_key': 'details',
        'layout': {
            'name': 'Definition',
            'type': 'popup',
            'options': {
                'layout': {
                    'type': 'raw'
                }
            }
        }
    })
])

# TAB - Deployment slots
deployment_slots_info_meta = TableDynamicLayout.set_fields('Deployments slots', root_path='data.deployment_slots', fields=[
    TextDyField.data_source('Name', 'name'),
    EnumDyField.data_source('Status', 'state', default_state={
        'safe': ['Running', 'Succeeded'],
        'warning': ['Pending'],
        'alert': ['Stopped', 'Failed'],
        'disable': []}),
    TextDyField.data_source('App service plan', 'app_service_plan_display'),
    TextDyField.data_source('Os system', 'os_system_display'),
    ListDyField.data_source('host_names', 'host_names', options={'delimiter': '<br>'}),
    TextDyField.data_source('Region', 'location')
])

# TAB - Configuration
configuration_info_meta =


function_app_meta = CloudServiceMeta.set_layouts(
    [function_app_info_meta])


class ComputeResource(CloudServiceResource):
    cloud_service_group = StringType(default='FunctionApp')


class FunctionAppResource(ComputeResource):
    cloud_service_type = StringType(default='Instance')
    data = ModelType(FunctionApp)
    _metadata = ModelType(CloudServiceMeta, default=function_app_meta, serialized_name='metadata')
    name = StringType()
    account = StringType(serialize_when_none=False)
    instance_type = StringType(serialize_when_none=False)
    instance_size = FloatType(serialize_when_none=False)


class FunctionAppResponse(CloudServiceResponse):
    resource = PolyModelType(FunctionAppResource)