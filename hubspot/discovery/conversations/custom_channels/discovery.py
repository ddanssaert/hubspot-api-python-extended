import hubspot.conversations.custom_channels as api_client
from ...discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):
    @property
    def channel_account_staging_tokens_api(self) -> api_client.ChannelAccountStagingTokensApi:
        return self._configure_api_client(api_client, "ChannelAccountStagingTokensApi")

    @property
    def channel_accounts_api(self) -> api_client.ChannelAccountsApi:
        return self._configure_api_client(api_client, "ChannelAccountsApi")

    @property
    def channels_api(self) -> api_client.ChannelsApi:
        return self._configure_api_client(api_client, "ChannelsApi")

    @property
    def messages_api(self) -> api_client.MessagesApi:
        return self._configure_api_client(api_client, "MessagesApi")
