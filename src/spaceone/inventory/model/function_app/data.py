from schematics import Model
from schematics.types import StringType
from spaceone.inventory.libs.schema.resource import AzureCloudService


class FunctionApp(AzureCloudService):
    id = StringType(serialize_when_none=False)
    name = StringType(serialize_when_none=False)
    location = StringType(serialize_when_none=False)

    def reference(self):
        return {
            "resource_id": self.id,
            "external_link": f"https://portal.azure.com/#@.onmicrosoft.com/resource{self.id}/overview",
        }