from schematics import Model
from schematics.types import StringType, ModelType, DictType, BooleanType, ListType, IntType, DateTimeType, FloatType, \
    LongType
from spaceone.inventory.libs.schema.resource import AzureCloudService


# ManagedServiceIdentity

# ManagedServiceIdentity - UserAssignedIdentity
class UserAssignedIdentity(Model):
    principal_id = StringType(serialize_when_none=False)
    client_id = StringType(serialize_when_none=False)


class ManagedServiceIdentity(Model):
    type = StringType(choices=['NONE', 'SYSTEM_ASSIGNED', 'SYSTEM_ASSIGNED_USER_ASSIGNED', 'USER_ASSIGNED'])
    user_assigned_identities = DictType(StringType, UserAssignedIdentity, serialize_when_none=False)
    tenant_id = StringType(serialize_when_none=False)
    principal_id = StringType(serialize_when_none=False)


# ExtendedLocation
class ExtendedLocation(Model):
    name = StringType(serialize_when_none=False)
    type = StringType(serialize_when_none=False)


# HostNameSslState
class HostNameSslState(Model):
    name = StringType(serialize_when_none=False)
    ssl_state = StringType(choices=['DISABLED', 'SNI_ENABLED', 'IP_BASED_ENABLED'])
    virtual_ip = StringType(serialize_when_none=False)
    thumbprint = StringType(serialize_when_none=False)
    to_update = BooleanType(serialize_when_none=False)
    host_type = StringType(choices=['REPOSITORY', 'STANDARD'])


# SiteConfig

# SiteConfig - NameValuePair
class NameValuePair(Model):
    name = StringType(serialize_when_none=False)
    value = StringType(serialize_when_none=False)


# SiteConfig - ConnStringInfo
class ConnStringInfo(Model):
    name = StringType(serialize_when_none=False)
    connection_string = StringType(serialize_when_none=False)
    type = StringType(choices=['API_HUB', 'CUSTOM', 'DOC_DB', 'EVENT_HUB', 'MY_SQL', 'NOTIFICATION_HUB', 'POSTGRE_SQL',
                               'REDIS_CACHE', 'SERVICE_BUS', 'SQL_AZURE', 'SQL_SERVER'])


# SiteConfig - HandlerMapping
class HandlerMapping(Model):
    extension = StringType(serialize_when_none=False)
    script_processor = StringType(serialize_when_none=False)
    arguments = StringType(serialize_when_none=False)


# SiteConfig - VirtualApplication

# SiteConfig - VirtualApplication - VirtualDirectory
class VirtualDirectory(Model):
    virtual_path = StringType(serialize_when_none=False)
    physical_path = StringType(serialize_when_none=False)


class VirtualApplication(Model):
    virtual_path = StringType(serialize_when_none=False)
    physical_path = StringType(serialize_when_none=False)
    preload_enabled = BooleanType(serialize_when_none=False)
    virtual_directories = ListType(ModelType(VirtualDirectory))


# SiteConfig - Experiments

# SiteConfig - Experiments - RampUpRule
class RampUpRule(Model):
    action_host_name = StringType(serialize_when_none=False)
    reroute_percentage = FloatType(serialize_when_none=False)
    change_step = FloatType(serialize_when_none=False)
    change_interval_in_minutes = IntType(serialize_when_none=False)
    min_reroute_percentage = FloatType(serialize_when_none=False)
    max_reroute_percentage = FloatType(serialize_when_none=False)
    change_decision_callback_url = StringType(serialize_when_none=False)
    name = StringType(serialize_when_none=False)


class Experiments(Model):
    ramp_up_rules = ListType(ModelType(RampUpRule))


# SiteConfig - SiteLimits
class SiteLimits(Model):
    max_percentage_cpu = FloatType(serialize_when_none=False)
    max_memory_in_mb = LongType(serialize_when_none=False)
    max_disk_size_in_mb = LongType(serialize_when_none=False)


# SiteConfig - AutoHealRules - AutoHealTriggers - RequestsBasedTrigger
class RequestsBasedTrigger(Model):
    count = IntType(serialize_when_none=False)
    time_interval = StringType(serialize_when_none=False)


# SiteConfig - AutoHealRules - AutoHealTriggers - StatusCodesBasedTrigger
class StatusCodesBasedTrigger(Model):
    status = IntType(serialize_when_none=False)
    sub_status = IntType(serialize_when_none=False)
    win32_status = IntType(serialize_when_none=False)
    count = IntType(serialize_when_none=False)
    time_interval = StringType(serialize_when_none=False)
    path = StringType(serialize_when_none=False)


# SiteConfig - AutoHealRules - AutoHealTriggers - SlowRequestsBasedTrigger
class SlowRequestsBasedTrigger(Model):
    time_taken = StringType(serialize_when_none=False)
    path = StringType(serialize_when_none=False)
    count = IntType(serialize_when_none=False)
    time_interval = StringType(serialize_when_none=False)


# SiteConfig - AutoHealRules - AutoHealTriggers - StatusCodesRangeBasedTrigger
class StatusCodesRangeBasedTrigger(Model):
    status_codes = StringType(serialize_when_none=False)
    path = StringType(serialize_when_none=False)
    count = IntType(serialize_when_none=False)
    time_interval = StringType(serialize_when_none=False)


# SiteConfig - AutoHealRules - AutoHealTriggers
class AutoHealTriggers(Model):
    requests = ModelType(RequestsBasedTrigger)
    private_bytes_in_kb = IntType(serialize_when_none=False)
    status_codes = ListType(ModelType(StatusCodesBasedTrigger))
    slow_requests = ModelType(SlowRequestsBasedTrigger)
    slow_requests_with_path = ListType(ModelType(SlowRequestsBasedTrigger))
    status_codes_range = ListType(ModelType(StatusCodesRangeBasedTrigger))


# SiteConfig - AutoHealRules - AutoHealActions - AutoHealCustomAction
class AutoHealCustomAction(Model):
    exe = StringType(serialize_when_none=False)
    parameters = StringType(serialize_when_none=False)
    min_process_execution_time = StringType(serialize_when_none=False)


# SiteConfig - AutoHealRules - AutoHealActions
class AutoHealActions(Model):
    action_type = StringType(choices=['RECYCLE', 'LOG_EVENT', 'CUSTOM_ACTION'])
    custom_action = ModelType(AutoHealCustomAction)


# SiteConfig - AutoHealRules
class AutoHealRules(Model):
    triggers = ModelType(AutoHealTriggers)
    actions = ModelType(AutoHealActions)


# SiteConfig - CorsSettings
class CorsSettings(Model):
    allowed_origins = ListType(StringType)
    support_credentials = BooleanType(serialize_when_none=False)


# SiteConfig - PushSettings
class PushSettings(Model):
    id = StringType(serialize_when_none=False)
    name = StringType(serialize_when_none=False)
    type = StringType(serialize_when_none=False)
    kind = StringType(serialize_when_none=False)
    is_push_enabled = BooleanType(serialize_when_none=False)
    tag_whitelist_json = StringType(serialize_when_none=False)
    tags_requiring_auth = StringType(serialize_when_none=False)
    dynamic_tags_json = StringType(serialize_when_none=False)


# SiteConfig - ApiDefinitionInfo
class ApiDefinitionInfo(Model):
    url = StringType(serialize_when_none=False)


# SiteConfig - ApiManagementConfig
class ApiManagementConfig(Model):
    id = StringType(serialize_when_none=False)


# SiteConfig - IpSecurityRestriction
class IpSecurityRestriction(Model):
    ip_address = StringType(serialize_when_none=False)
    subnet_mask = StringType(serialize_when_none=False)
    vnet_subnet_resource_id = StringType(serialize_when_none=False)
    vnet_traffic_tag = IntType(serialize_when_none=False)
    subnet_traffic_tag = IntType(serialize_when_none=False)
    action = StringType(serialize_when_none=False)
    tag = StringType(choices=['DEFAULT', 'SERVICE_TAG', 'XFF_PROXY'])
    priority = IntType(serialize_when_none=False)
    name = StringType(serialize_when_none=False)
    description = StringType(serialize_when_none=False)
    headers = DictType(StringType, ListType(StringType))


# SiteConfig - AzureStorageInfoValue
class AzureStorageInfoValue(Model):
    type = StringType(serialize_when_none=False)
    account_name = StringType(serialize_when_none=False)
    share_name = StringType(serialize_when_none=False)
    access_key = StringType(serialize_when_none=False)
    mount_path = StringType(serialize_when_none=False)
    state = StringType(serialize_when_none=False)


# SiteConfig - SiteMachineKey
class SiteMachineKey(Model):
    validation = StringType(serialize_when_none=False)
    validation_key = StringType(serialize_when_none=False)
    decryption = StringType(serialize_when_none=False)
    decryption_key = StringType(serialize_when_none=False)


class SiteConfig(Model):
    number_of_workers = IntType(serialize_when_none=False)
    default_documents = ListType(StringType)
    net_framework_version = StringType(serialize_when_none=False)
    php_version = StringType(serialize_when_none=False)
    python_version = StringType(serialize_when_none=False)
    node_version = StringType(serialize_when_none=False)
    power_shell_version = StringType(serialize_when_none=False)
    linux_fx_version = StringType(serialize_when_none=False)
    windows_fx_version = StringType(serialize_when_none=False)
    request_tracing_enabled = BooleanType(serialize_when_none=False)
    request_tracing_expiration_time = DateTimeType(serialize_when_none=False)
    remote_debugging_enabled = BooleanType(serialize_when_none=False)
    remote_debugging_version = StringType(serialize_when_none=False)
    http_logging_enabled = BooleanType(serialize_when_none=False)
    acr_use_managed_identity_creds = BooleanType(serialize_when_none=False)
    acr_user_managed_identity_id = StringType(serialize_when_none=False)
    logs_directory_size_limit = IntType(serialize_when_none=False)
    detailed_error_logging_enabled = BooleanType(serialize_when_none=False)
    publishing_username = StringType(serialize_when_none=False)
    app_settings = ListType(ModelType(NameValuePair))
    connection_strings = ListType(ModelType(ConnStringInfo))
    handler_mappings = ListType(ModelType(HandlerMapping))
    document_root = StringType(serialize_when_none=False)
    scm_type = StringType(choices=['BITBUCKET_GIT', 'BITBUCKET_HG', 'CODE_PLEX_GIT', 'CODE_PLEX_HG', 'DROPBOX',
                                   'EXTERNAL_GIT', 'EXTERNAL_HG', 'GIT_HUB', 'LOCAL_GIT', 'NONE', 'ONE_DRIVE', 'TFS',
                                   'VSO', 'VSTSRM'])
    use32_bit_worker_process = BooleanType(serialize_when_none=False)
    web_sockets_enabled = BooleanType(serialize_when_none=False)
    always_on = BooleanType(serialize_when_none=False)
    java_version = StringType(serialize_when_none=False)
    java_container = StringType(serialize_when_none=False)
    app_command_line = StringType(serialize_when_none=False)
    managed_pipeline_mode = StringType(choices=['CLASSIC', 'INTEGRATED'])
    virtual_applications = ListType(ModelType(VirtualApplication))
    load_balancing = StringType(choices=['LEAST_REQUESTS', 'LEAST_RESPONSE_TIME', 'PER_SITE_ROUND_ROBIN',
                                         'REQUEST_HASH', 'WEIGHTED_ROUND_ROBIN', 'WEIGHTED_TOTAL_TRAFFIC'])
    experiments = ModelType(Experiments)
    limits = ModelType(SiteLimits)
    auto_heal_enabled = BooleanType(serialize_when_none=False)
    auto_heal_rules = ModelType(AutoHealRules)
    tracing_options = StringType(serialize_when_none=False)
    vnet_name = StringType(serialize_when_none=False)
    vnet_route_all_enabled = BooleanType(serialize_when_none=False)
    vnet_private_ports_count = IntType(serialize_when_none=False)
    cors = ModelType(CorsSettings)
    push = ModelType(PushSettings)
    api_management_config = ModelType(ApiManagementConfig)
    auto_swap_slot_name = StringType(serialize_when_none=False)
    local_my_sql_enabled = BooleanType(serialize_when_none=False)
    managed_service_identity_id = IntType(serialize_when_none=False)
    x_managed_service_identity_id = IntType(serialize_when_none=False)
    key_vault_reference_identity = StringType(serialize_when_none=False)
    ip_security_restrictions = ListType(ModelType(IpSecurityRestriction))
    scm_ip_security_restrictions = ListType(ModelType(IpSecurityRestriction))
    scm_ip_security_restrictions_use_main = BooleanType(serialize_when_none=False)
    http20_enabled = BooleanType(serialize_when_none=False)
    min_tls_version = StringType(choices=['ONE0', 'ONE1', 'ONE2'])
    scm_min_tls_version = StringType(choices=['ONE0', 'ONE1', 'ONE2'])
    ftps_state = StringType(choices=['ALL_ALLOWED', 'DISABLED', 'FTPS_ONLY'])
    pre_warmed_instance_count = IntType(serialize_when_none=False)
    function_app_scale_limit = IntType(serialize_when_none=False)
    health_check_path = StringType(serialize_when_none=False)
    functions_runtime_scale_monitoring_enabled = BooleanType(serialize_when_none=False)
    website_time_zone = StringType(serialize_when_none=False)
    minimum_elastic_instance_count = IntType(serialize_when_none=False)
    azure_storage_accounts = DictType(StringType, ModelType(AzureStorageInfoValue))
    public_network_access = StringType(serialize_when_none=False)
    machine_key = ModelType(SiteMachineKey)


# Site - HostingEnvironmentProfile
class HostingEnvironmentProfile(Model):
    id = StringType(serialize_when_none=False)
    name = StringType(serialize_when_none=False)
    type = StringType(serialize_when_none=False)


# Site - CloningInfo
class CloningInfo(Model):
    correlation_id = StringType(serialize_when_none=False)
    overwrite = BooleanType(serialize_when_none=False)
    clone_custom_host_names = BooleanType(serialize_when_none=False)
    clone_source_control = BooleanType(serialize_when_none=False)
    source_web_app_id = StringType(serialize_when_none=False)
    source_web_app_location = StringType(serialize_when_none=False)
    hosting_environment = StringType(serialize_when_none=False)
    app_settings_overrides = DictType(StringType, serialize_when_none=False)
    configure_load_balancing = BooleanType(serialize_when_none=False)
    traffic_manager_profile_id = StringType(serialize_when_none=False)
    traffic_manager_profile_name = StringType(serialize_when_none=False)


class Site(AzureCloudService):
    id = StringType(serialize_when_none=False)
    name = StringType(serialize_when_none=False)
    location = StringType(serialize_when_none=False)
    kind = StringType(serialize_when_none=False)
    identity = ModelType(ManagedServiceIdentity)
    extended_location = ModelType(ExtendedLocation)
    enabled = BooleanType(serialize_when_none=False)
    host_name_ssl_states = ListType(ModelType(HostNameSslState))
    server_farm_id = StringType(serialize_when_none=False)
    reserved = BooleanType(serialize_when_none=False)
    is_xenon = BooleanType(serialize_when_none=False)
    hyper_v = BooleanType(serialize_when_none=False)
    site_config = ModelType(SiteConfig)
    scm_site_also_stopped = BooleanType(serialize_when_none=False)
    hosting_environment_profile = ModelType(HostingEnvironmentProfile)
    client_affinity_enabled = BooleanType(serialize_when_none=False)
    client_cert_enabled = BooleanType(serialize_when_none=False)
    client_cert_mode = StringType(choices=['OPTIONAL', 'OPTIONAL_INTERACTIVE_USER', 'REQUIRED'])
    client_cert_exclusion_paths = StringType(serialize_when_none=False)
    host_names_disabled = BooleanType(serialize_when_none=False)
    custom_domain_verification_id = StringType(serialize_when_none=False)
    container_size = IntType(serialize_when_none=False)
    daily_memory_time_quota = IntType(serialize_when_none=False)
    cloning_info = ModelType(CloningInfo)
    https_only = BooleanType(serialize_when_none=False)
    redundancy_mode = StringType(choices=['ACTIVE_ACTIVE', 'FAILOVER', 'GEO_REDUNDANT', 'MANUAL', 'NONE'])
    storage_account_required = BooleanType(serialize_when_none=False)
    key_vault_reference_identity = StringType(serialize_when_none=False)
    virtual_network_subnet_id = StringType(serialize_when_none=False)

    def reference(self):
        return {
            'resource_id': self.id,
            'external_link': f'https://portal.azure.com/#@.onmicrosoft.com/resource{self.id}/overview',
        }
