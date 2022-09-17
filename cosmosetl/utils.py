import base64
import itertools
import re
from datetime import datetime
from cosmosetl.utils import rpc_response_to_result
from cosmosetl.mappers.block_mapper import CosmBlockMapper


MAX_PER_PAGE = 100

def str_to_dec(num_string):
    if num_string is None:
        return None
    try:
        return int(num_string)
    except ValueError:
        print("Not a num string %s" % num_string)
        return num_string


def block_time_to_timestamp(time):
    """Convert block time to timestamp
    param time: str e.g block.time
    """
    # Had to use re.match because
    # 1. The precision is in nanoseconds so we pick 6 digits and leave 3 out
    # 2. But the genesis block time precision is seconds
    # Added timezone Z because all the sample network have seen are in Z timezone

    time = re.match('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.?\d{0,6}', time)
    time = time.group(0)
    format = "%Y-%m-%dT%H:%M:%S%z" if len(time) == 19 else "%Y-%m-%dT%H:%M:%S.%f%z"
    return str_to_timestamp(time+'Z', format)


def str_to_timestamp(date_string, format="%Y-%m-%dT%H:%M:%S.%f%z"):
    if date_string is None:
        return None
    try:
        return datetime.strptime(date_string, format).timestamp()
    except ValueError:
        print("Date string (%s) or format (%s) is incorrect" % (date_string, format))
        return date_string


def b64decode(input_string, encoding='utf-8'):
    if input_string is None:
        return None
    try:
        return base64.b64decode(input_string).decode(encoding)
    except Exception:
        print("b64 decoding failed %s" % input_string)
        return input_string


def validate_range(range_start_incl, range_end_incl):
    if range_start_incl < 0 or range_end_incl < 0:
        raise ValueError('range_start and range_end must be greater or equal to 0')

    if range_end_incl < range_start_incl:
        raise ValueError('range_end must be greater or equal to range_start')


def rpc_response_to_result(response):
    result = response.get('result')
    if result is None:
        error_message = 'result is None in response {}.'.format(response)
        # Make better error messages
        raise ValueError(error_message)
    return result


def rpc_response_batch_to_results(response):
    # Sometimes response is dict instead of list
    if isinstance(response, dict):
        yield rpc_response_to_result(response)
    else:
        for response_item in response:
            yield rpc_response_to_result(response_item)


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


def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)
