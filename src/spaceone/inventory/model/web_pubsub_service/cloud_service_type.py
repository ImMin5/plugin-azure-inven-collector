import os
from spaceone.inventory.libs.utils import *
from spaceone.inventory.libs.schema.metadata.dynamic_widget import CardWidget, ChartWidget
from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, ListDyField, \
    EnumDyField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta

current_dir = os.path.abspath(os.path.dirname(__file__))

web_pubsub_service_by_region_conf = os.path.join(current_dir, 'widget/.yaml')
web_pubsub_service_by_subscription_conf = os.path.join(current_dir, 'widget/.yaml')
web_pubsub_service_instance_count_conf = os.path.join(current_dir, 'widget/.yaml')

cst_web_pubsub_service = CloudServiceTypeResource()
cst_web_pubsub_service.name = 'Service'
cst_web_pubsub_service.group = 'WebPubSubService'
cst_web_pubsub_service.service_code = ''
cst_web_pubsub_service.labels = ['Application Integration']
cst_web_pubsub_service.is_major = True
cst_web_pubsub_service.is_primary = True
cst_web_pubsub_service.tags = {
    'spaceone:icon': '',
}

cst_web_pubsub_service._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
    ],
    search=[

    ],
    widget=[

    ]

)


CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_web_pubsub_service}),
]
