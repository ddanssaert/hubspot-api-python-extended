import hubspot.conversations.conversations as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def actors_api(self) -> api_client.ActorsApi:
        return self._configure_api_client(api_client, "ActorsApi")

    @property
    def channel_accounts_api(self) -> api_client.ChannelAccountsApi:
        return self._configure_api_client(api_client, "ChannelAccountsApi")

    @property
    def channels_api(self) -> api_client.ChannelsApi:
        return self._configure_api_client(api_client, "ChannelsApi")

    @property
    def inboxes_api(self) -> api_client.InboxesApi:
        return self._configure_api_client(api_client, "InboxesApi")

    @property
    def threads_api(self) -> api_client.ThreadsApi:
        return self._configure_api_client(api_client, "ThreadsApi")
