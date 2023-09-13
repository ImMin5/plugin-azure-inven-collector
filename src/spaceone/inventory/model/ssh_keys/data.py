from schematics import Model
from schematics.types import ModelType, ListType, StringType, IntType, BooleanType, FloatType, DateTimeType
from spaceone.inventory.libs.schema.resource import AzureCloudService, AzureTags


class SQLServer(AzureCloudService):
    name = StringType()
    id = StringType()
    kind = StringType(serialize_when_none=False)
    location = StringType()
    type = StringType()

    def reference(self):
        return {
            "resource_id": self.id,
            "external_link": f"https://portal.azure.com/#@.onmicrosoft.com/resource{self.id}/overview",
        }