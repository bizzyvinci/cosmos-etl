import re
from cosmosetl.mappers.block_mapper import CosmBlockMapper
from cosmosetl.utils import rpc_response_to_result

def get_block(web3, height=None):
    # height==None would return latest block
    if height is not None and not isinstance(height, str):
        height = str(height)
    response = web3.make_request('block', [height])
    result = rpc_response_to_result(response)
    return CosmBlockMapper().json_dict_to_block(result)


def get_genesis_block(web3):
    response = web3.make_request('block', ['1'])
    if 'error' in response:
        search = re.search('lowest height is (\d+)', response['error']['data'])
        if search is not None:
            genesis_height = search.group(1)
            response = web3.make_request('block', [genesis_height])
    
    result = rpc_response_to_result(response)
    return CosmBlockMapper().json_dict_to_block(result)


def get_latest_block(web3):
    return get_block(web3, None)

