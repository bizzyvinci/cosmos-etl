from web3 import HTTPProvider
from web3._utils.request import make_post_request


# Mostly copied from web3.py/providers/rpc.py. Supports batch requests.
# Will be removed once batch feature is added to web3.py https://github.com/ethereum/web3.py/issues/832
class BatchHTTPProvider(HTTPProvider):

    def make_batch_request(self, text):
        self.logger.debug("Making request HTTP. URI: %s, Request: %s",
                          self.endpoint_uri, text)
        request_data = text.encode('utf-8')
        raw_response = make_post_request(
            self.endpoint_uri,
            request_data,
            **self.get_request_kwargs()
        )
        response = self.decode_rpc_response(raw_response)
        self.logger.debug("Getting response HTTP. URI: %s, "
                          "Request: %s, Response: %s",
                          self.endpoint_uri, text, response)
        return response
