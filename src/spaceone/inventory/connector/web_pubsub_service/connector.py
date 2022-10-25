import logging
from spaceone.inventory.libs.connector import AzureConnector

__all__ = ['WebPubSubServiceConnector']
_LOGGER = logging.getLogger(__name__)


class WebPubSubServiceConnector(AzureConnector):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_connect(kwargs.get('secret_data'))

    def list_by_subscription(self):
        self.web_pubsub_service_client.web_pub_sub.list_by_subscription()
