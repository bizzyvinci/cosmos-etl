from cosmosetl.utils import MAX_PER_PAGE


def generate_json_rpc(method, params, request_id=1):
    return {
        'jsonrpc': '2.0',
        'method': method,
        'params': params,
        'id': request_id,
    }


def generate_get_block_by_number_json_rpc(block_numbers):
    for idx, block_number in enumerate(block_numbers):
        yield generate_json_rpc(
            method='block',
            params=[str(block_number)],
            request_id=idx
        )


def generate_tx_search_by_height_json_rpc(heights, page=1, per_page=MAX_PER_PAGE):
    for idx, height in enumerate(heights):
        yield generate_json_rpc(
            method='tx_search',
            params=["tx.height=%d" % height, True, str(page), str(per_page), "asc"],
            request_id=idx
        )
