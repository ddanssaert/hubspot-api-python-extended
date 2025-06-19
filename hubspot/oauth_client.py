import functools
from typing import Callable

from .client import Client
from hubspot.discovery.discovery_base import metadata


# Function to refresh OAuth tokens
def _refresh_tokens(config):
    hubspot_client = Client()

    # Perform tokens refresh using HubSpot OAuth API
    tokens = hubspot_client.oauth.tokens_api.create(
        grant_type="refresh_token",
        client_id=config['client_id'],
        client_secret=config['client_secret'],
        refresh_token=config['refresh_token']
    )

    return tokens


# Decorator to automatically refresh tokens on unauthorized exceptions
def _custom_call_api_decorator(config, api_client, call_api):
    @functools.wraps(call_api)
    def wrapper(*args, **kwargs):
        try:
            return call_api(*args, **kwargs)
        except Exception as e:
            if type(e).__name__ == 'UnauthorizedException' and e.status == 401:
                # Refresh token and retry
                new_tokens = _refresh_tokens(config)
                config['access_token'] = new_tokens.access_token
                api_client.configuration.access_token = new_tokens.access_token
                if 'access_token_setter_callback' in config:
                    config['access_token_setter_callback'](new_tokens)
                return call_api(*args, **kwargs)
            else:
                raise

    return wrapper


# Factory function to create API client with auto token refresh
def _autotokensrefresh_api_factory(api_client_package, api_name, config):
    configuration = api_client_package.Configuration()
    for key in config:
        if key == "api_key":
            configuration.api_key["developer_hapikey"] = config["api_key"]
        elif key == "retry":
            configuration.retries = config["retry"]
        else:
            setattr(configuration, key, config[key])

    api_client = api_client_package.ApiClient(configuration=configuration)
    package_version = metadata.version("hubspot-api-client")
    api_client.user_agent = "hubspot-api-client-python; {0}".format(package_version)

    # Set API call to use custom decorator for automatic token refresh
    api_client.call_api = _custom_call_api_decorator(config, api_client, api_client.call_api)

    return getattr(api_client_package, api_name)(api_client=api_client)


class OAuthClient(Client):
    """
    OAuthClient extends Client to include automatic token management
    functionality for managing OAuth access tokens with refresh capability.

    Attributes:
        client_id (str): The client ID for OAuth.
        client_secret (str): The client secret for OAuth.
        access_token (str): The access token used for API requests.
        refresh_token (str): The refresh token to obtain a new access token.
        access_token_setter_callback (Callable[[dict], None], optional):
            A callback function that takes new token data as input. Useful for updating the tokens in a database.
    """

    def __init__(self,
                 client_id: str,
                 client_secret: str,
                 access_token: str,
                 refresh_token: str,
                 access_token_setter_callback: Callable[[dict], None] = None,
                 *args,
                 **kwargs
                 ):
        super().__init__(
            *args,
            **kwargs,
            client_id=client_id,
            client_secret=client_secret,
            access_token=access_token,
            refresh_token=refresh_token,
            access_token_setter_callback=access_token_setter_callback,
            api_factory=_autotokensrefresh_api_factory,  # !
        )
