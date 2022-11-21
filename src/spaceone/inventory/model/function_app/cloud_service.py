from schematics.types import ModelType, StringType, PolyModelType, FloatType, DateTimeType
from spaceone.inventory.model.function_app.data import FunctionApp
from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, DateTimeDyField
from spaceone.inventory.libs.schema.metadata.dynamic_layout import ItemDynamicLayout
from spaceone.inventory.libs.schema.cloud_service import CloudServiceResource, CloudServiceResponse, CloudServiceMeta

'''
Function App
'''
# TAB - Function App
function_app_info_meta = ItemDynamicLayout.set_fields('Web PubSub Service', fields=[
])


function_app_meta = CloudServiceMeta.set_layouts(
    [function_app_info_meta])


class ComputeResource(CloudServiceResource):
    cloud_service_group = StringType(default='WebPubSubService')


class FunctionAppResource(ComputeResource):
    cloud_service_type = StringType(default='ScaleSet')
    data = ModelType(FunctionApp)
    _metadata = ModelType(CloudServiceMeta, default=function_app_meta, serialized_name='metadata')
    name = StringType()
    account = StringType(serialize_when_none=False)
    instance_type = StringType(serialize_when_none=False)
    instance_size = FloatType(serialize_when_none=False)


class WebPubSubServiceResponse(CloudServiceResponse):
    resource = PolyModelType(FunctionAppResource)