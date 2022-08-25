from urllib.parse import urlparse

from web3 import IPCProvider, HTTPProvider

from cosmosetl.providers.ipc import BatchIPCProvider
from cosmosetl.providers.rpc import BatchHTTPProvider

DEFAULT_TIMEOUT = 60


def get_provider_from_uri(uri_string, timeout=DEFAULT_TIMEOUT, batch=False):
    uri = urlparse(uri_string)
    if uri.scheme == 'file':
        if batch:
            return BatchIPCProvider(uri.path, timeout=timeout)
        else:
            return IPCProvider(uri.path, timeout=timeout)
    elif uri.scheme == 'http' or uri.scheme == 'https':
        request_kwargs = {'timeout': timeout}
        if batch:
            return BatchHTTPProvider(uri_string, request_kwargs=request_kwargs)
        else:
            return HTTPProvider(uri_string, request_kwargs=request_kwargs)
    else:
        raise ValueError('Unknown uri scheme {}'.format(uri_string))

