from schematics.types import ModelType, StringType, PolyModelType, FloatType, DateTimeType
from spaceone.inventory.model.web_pubsub_service.data import WebPubSubService
from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, DateTimeDyField
from spaceone.inventory.libs.schema.metadata.dynamic_layout import ItemDynamicLayout
from spaceone.inventory.libs.schema.cloud_service import CloudServiceResource, CloudServiceResponse, CloudServiceMeta

'''
Web PubSub Service
'''
# TAB - Web PubSub Service
web_pubsub_service_info_meta = ItemDynamicLayout.set_fields('Web PubSub Service', fields=[
])


web_pubsub_service_meta = CloudServiceMeta.set_layouts(
    [web_pubsub_service_info_meta])


class ApplicationIntegrationResource(CloudServiceResource):
    cloud_service_group = StringType(default='WebPubSubService')


class WebPubSubServiceResource(ApplicationIntegrationResource):
    cloud_service_type = StringType(default='Service')
    data = ModelType(WebPubSubService)
    _metadata = ModelType(CloudServiceMeta, default=web_pubsub_service_meta, serialized_name='metadata')
    name = StringType()
    account = StringType(serialize_when_none=False)
    instance_type = StringType(serialize_when_none=False)
    instance_size = FloatType(serialize_when_none=False)
    launched_at = DateTimeType(serialize_when_none=False)


class WebPubSubServiceResponse(CloudServiceResponse):
    resource = PolyModelType(WebPubSubServiceResource)
