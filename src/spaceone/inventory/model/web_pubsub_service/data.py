from schematics import Model
from schematics.types import ModelType, ListType, StringType, IntType, BooleanType, DateTimeType
from spaceone.inventory.libs.schema.resource import AzureCloudService


# SkuResource
class SkuResource(Model):
    name = StringType(serialize_when_none=False)
    tier = StringType(serialize_when_none=False)
    size = StringType(serialize_when_none=False)
    family = StringType(serialize_when_none=False)
    capacity = IntType(serialize_when_none=False)


# ManagedIdentity

# ManagedIdentity - UserAssignedIdentityProperty
class UserAssignedIdentityProperty(Model):
    principal_id = StringType(serialize_when_none=False)
    client_id = StringType(serialize_when_none=False)


class ManagedIdentity(Model):
    type = StringType(serialize_when_none=False)
    user_assigned_identities = ModelType(UserAssignedIdentityProperty)
    principal_id = StringType(serialize_when_none=False)
    tenant_id = StringType(serialize_when_none=False)


# SystemData
class SystemData(Model):
    created_by = StringType(serialize_when_none=False)
    created_by_type = StringType(serialize_when_none=False)
    created_at = DateTimeType(serialize_when_none=False)
    last_modified_by = StringType(serialize_when_none=False)
    last_modified_by_type = StringType(serialize_when_none=False)
    last_modified_at = DateTimeType(serialize_when_none=False)


# PrivateEndpointConnection

# PrivateEndpointConnection - PrivateEndpoint
class PrivateEndpoint(Model):
    id = StringType(serialize_when_none=False)


# PrivateEndpointConnection - PrivateLinkServiceConnectionState
class PrivateLinkServiceConnectionState:
    status = StringType(choices=('Approved', 'Disconnected', 'Pending', 'Rejected'))
    description = StringType(serialize_when_none=False)
    actions_required = StringType(serialize_when_none=False)


class PrivateEndpointConnection(Model):
    id = StringType(serialize_when_none=False)
    name = StringType(serialize_when_none=False)
    type = StringType(serialize_when_none=False)
    system_data = ModelType(SystemData, serialize_when_none=False)
    provisioning_state = StringType(choices=('Canceled', 'Creating', 'Deleting', 'Failed', 'Moving', 'Running',
                                             'Succeeded', 'Unknown', 'Updating'))
    private_endpoint = ModelType(PrivateEndpoint)
    group_ids = ListType(StringType, serialize_when_none=False)
    private_link_service_connection_state = ModelType(PrivateEndpoint)


# SharedPrivateLinkResource
class SharedPrivateLinkResource(Model):
    id = StringType(serialize_when_none=False)
    name = StringType(serialize_when_none=False)
    type = StringType(serialize_when_none=False)
    system_data = ModelType(SystemData)
    group_id = StringType(serialize_when_none=False)
    private_link_resource_id = StringType(serialize_when_none=False)
    provisioning_state = StringType(choices=('Canceled', 'Creating', 'Deleting', 'Failed', 'Moving', 'Running',
                                             'Succeeded', 'Unknown', 'Updating'))
    request_message = StringType(serialize_when_none=False)
    status = StringType(choices=('Approved', 'Disconnected', 'Pending', 'Rejected'))


# WebPubSubTlsSettings
class WebPubSubTlsSettings(Model):
    client_cert_enabled = BooleanType(default=True)


# LiveTraceConfiguration

# LiveTraceConfiguration - LiveTraceCategory
class LiveTraceCategory(Model):
    name = StringType(serialize_when_none=False)
    enabled = StringType(serialize_when_none=False)


class LiveTraceConfiguration(Model):
    enabled = StringType(serialize_when_none=False)
    categories = ListType(ModelType(LiveTraceCategory))


# ResourceLogConfiguration

# ResourceLogConfiguration - ResourceLogCategory
class ResourceLogCategory(Model):
    name = StringType(serialize_when_none=False)
    enabled = StringType(serialize_when_none=False)


class ResourceLogConfiguration(Model):
    categories = ListType(ModelType(ResourceLogCategory))


# WebPubSubNetworkACLs

# WebPubSubNetworkACLs - NetworkACL
class NetworkACL(Model):
    allow = ListType(StringType, serialize_when_none=False)
    deny = ListType(StringType, serialize_when_none=False)


# WebPubSubNetworkACLs - PrivateEndpointACL
class PrivateEndpointACL(Model):
    allow = ListType(StringType)
    deny = ListType(StringType)
    name = StringType()


class WebPubSubNetworkACLs(Model):
    default_action = StringType(serialize_when_none=False)
    public_network = ModelType(NetworkACL)
    private_endpoints = ListType(ModelType(PrivateEndpointACL))


class WebPubSubService(AzureCloudService):  # Main Class
    id = StringType(serialize_when_none=False)
    name = StringType(serialize_when_none=False)
    location = StringType(serialize_when_none=False)
    sku = ModelType(SkuResource, serialize_when_none=False)
    identity = ModelType(ManagedIdentity, serialize_when_none=False)
    system_data = ModelType(SystemData, serialize_when_none=False)
    provisioning_state = StringType(choices=('Canceled', 'Creating', 'Deleting', 'Failed', 'Moving', 'Running',
                                             'Succeeded', 'Unknown', 'Updating'))
    external_ip = StringType(serialize_when_none=False)
    host_name = StringType(serialize_when_none=False)
    public_port = IntType(serialize_when_none=False)
    server_port = IntType(serialize_when_none=False)
    version = StringType(serialize_when_none=False)
    private_endpoint_connections = ListType(ModelType(PrivateEndpointConnection))
    shared_private_link_resources = ListType(ModelType(SharedPrivateLinkResource))
    tls = ModelType(WebPubSubTlsSettings)
    host_name_prefix = StringType(serialize_when_none=False)
    live_trace_configuration = ModelType(LiveTraceConfiguration)
    resource_log_configuration = ModelType(ResourceLogConfiguration)
    public_network_access = StringType(default='Enabled')
    disable_local_auth = BooleanType(default=False)
    disable_aad_auth = BooleanType(default=False)

    def reference(self):
        return {
            "resource_id": self.id,
            "external_link": f"https://portal.azure.com/#@.onmicrosoft.com/resource{self.id}/overview",
        }
