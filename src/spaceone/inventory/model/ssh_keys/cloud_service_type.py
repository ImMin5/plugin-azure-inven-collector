
import os
from spaceone.inventory.libs.utils import *
from spaceone.inventory.libs.schema.metadata.dynamic_widget import CardWidget, ChartWidget
from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, ListDyField, \
    EnumDyField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta
from spaceone.inventory.conf.cloud_service_conf import ASSET_URL


current_dir = os.path.abspath(os.path.dirname(__file__))


cst_ssh_keys = CloudServiceTypeResource()

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_ssh_keys}),
]