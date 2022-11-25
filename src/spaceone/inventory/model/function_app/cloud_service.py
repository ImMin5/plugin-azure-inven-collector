from schematics.types import ModelType, StringType, PolyModelType, FloatType, DateTimeType
from spaceone.inventory.model.function_app.data import FunctionApp
from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, EnumDyField, DateTimeDyField
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
    TextDyField.data_source('App Service Plan', 'data.app_service_plan_display')
])

# TAB - Functions
functions_info_meta = TableDynamicLayout.set_fields('Functions', root_path='data.functions', fields=[

])


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