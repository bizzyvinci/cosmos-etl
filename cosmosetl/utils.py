import base64
from datetime import datetime

MAX_PER_PAGE = 100

def str_to_dec(num_string):
    if num_string is None:
        return None
    try:
        return int(num_string)
    except ValueError:
        print("Not a num string %s" % num_string)
        return num_string


def str_to_timestamp(date_string, format="%Y-%m-%dT%H:%M:%S.%f%z"):
    # format is not correct because %f still has 3 more decimals. 
    # Remove or make changes later
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
