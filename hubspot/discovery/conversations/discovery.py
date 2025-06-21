from ..discovery_base import DiscoveryBase

class Discovery(DiscoveryBase):
    @property
    def visitor_identification(self):
        from .visitor_identification.discovery import Discovery as VisitorIdentificationDiscovery
        return VisitorIdentificationDiscovery(self.config)

    @property
    def conversations(self):
        from .conversations.discovery import Discovery as ConversationsDiscovery
        return ConversationsDiscovery(self.config)

    @property
    def custom_channels(self):
        from .custom_channels.discovery import Discovery as CustomChannelsDiscovery
        return CustomChannelsDiscovery(self.config)
