import os
from spaceone.inventory.libs.utils import *
from spaceone.inventory.libs.schema.metadata.dynamic_widget import CardWidget, ChartWidget
from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, ListDyField, \
    EnumDyField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta

current_dir = os.path.abspath(os.path.dirname(__file__))

function_app_by_account_conf = os.path.join(current_dir, 'widget/function_app_by_account.yaml')
function_app_by_region_conf = os.path.join(current_dir, 'widget/function_app_by_region.yaml')
function_app_by_resource_group_conf = os.path.join(current_dir, 'widget/function_app_by_resource_group.yaml')
function_app_total_count_count_conf = os.path.join(current_dir, 'widget/function_app_total_count.yaml')

cst_function_app = CloudServiceTypeResource()
cst_function_app.name = 'Instance'
cst_function_app.group = 'FunctionApp'
cst_function_app.service_code = 'Microsoft.Web/sites'
cst_function_app.labels = ['Compute']
cst_function_app.is_major = True
cst_function_app.is_primary = True
cst_function_app.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/azure/azure-function-app.svg',
}

cst_function_app._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
    ],
    search=[

    ],
    widget=[

    ]

)


CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_function_app}),
]