from hubspot import HubSpot
from hubspot.conversations.custom_channels import ChannelAccountStagingTokensApi, ChannelAccountsApi, ChannelsApi, MessagesApi


def test_is_discoverable():
    apis = HubSpot().conversations.custom_channels
    assert isinstance(apis.channel_account_staging_tokens_api, ChannelAccountStagingTokensApi)
    assert isinstance(apis.channel_accounts_api, ChannelAccountsApi)
    assert isinstance(apis.channels_api, ChannelsApi)
    assert isinstance(apis.messages_api, MessagesApi)
