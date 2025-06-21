from hubspot import HubSpot
from hubspot.conversations.conversations import ActorsApi, ChannelAccountsApi, ChannelsApi, InboxesApi, ThreadsApi


def test_is_discoverable():
    apis = HubSpot().conversations.conversations
    assert isinstance(apis.actors_api, ActorsApi)
    assert isinstance(apis.channel_accounts_api, ChannelAccountsApi)
    assert isinstance(apis.channels_api, ChannelsApi)
    assert isinstance(apis.inboxes_api, InboxesApi)
    assert isinstance(apis.threads_api, ThreadsApi)
