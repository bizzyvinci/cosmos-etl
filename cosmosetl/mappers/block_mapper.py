from cosmosetl.domain.block import CosmBlock
from cosmosetl.utils import str_to_dec

class CosmBlockMapper:
    def json_dict_to_block(self, json_dict):
        block = CosmBlock()
        block.height = str_to_dec(json_dict['block']['header'].get('height'))
        block.hash = json_dict['block_id'].get('hash')
        block.last_block_hash = json_dict['block']['header'].get('last_block_id', {}).get('hash')
        block.data_hash = json_dict['block']['header'].get('data_hash')
        block.proposer = json_dict['block']['header'].get('proposer_address')
        block.num_txs = len(json_dict['block']['data'].get('txs', []))
        block.timestamp = json_dict['block']['header'].get('time')
        return block
    
    def block_to_dict(self, block):
        return {
            'type': 'block',
            'height': block.height,
            'hash': block.hash,
            'last_block_hash': block.last_block_hash,
            'data_hash': block.data_hash,
            'proposer': block.proposer,
            'num_txs': block.num_txs,
            'timestamp': block.timestamp,
        }