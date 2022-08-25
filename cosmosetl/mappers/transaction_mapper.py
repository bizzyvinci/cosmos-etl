from asyncio import events
import json
from cosmosetl.domain.transaction import CosmTransaction
from cosmosetl.mappers.event_mapper import CosmEventMapper
from cosmosetl.utils import str_to_dec, b64decode

class CosmTransactionMapper:
    def __init__(self):
        self.event_mapper = CosmEventMapper()

    def json_dict_to_transaction(self, json_dict):
        transaction = CosmTransaction()
        transaction.hash = json_dict.get("hash")
        transaction.height = str_to_dec(json_dict.get("height"))
        transaction.index = json_dict.get("index")
        transaction.code = json_dict.get("tx_result", {}).get("code")
        transaction.gas_used = json_dict.get("tx_result", {}).get("gas_used")
        transaction.gas_wanted = json_dict.get("tx_result", {}).get("gas_wanted")
        transaction.num_events = len(json_dict.get("tx_result", {}).get("events", []))
        transaction.root_hash = json_dict.get("proof", {}).get("root_hash")
        transaction.tx = json_dict.get("tx")
        # simple b64decoding doesn't work for data
        # transaction.data = b64decode(json_dict.get("tx_result", {}).get("data"))
        transaction.raw_data = json_dict.get("tx_result", {}).get("data")
        transaction.raw_log = json_dict.get("tx_result", {}).get("log")
        transaction.events = [
            self.event_mapper.json_dict_to_event(evt, tx_hash=transaction.hash)
            for evt in json_dict.get('tx_result', {}).get('events', [])
        ]
        return transaction
        
    def transaction_to_dict(self, transaction):
        return {
            "type": "transaction",
            "hash": transaction.hash,
            "height": transaction.height,
            "index": transaction.index,
            "code": transaction.code,
            "gas_used": transaction.gas_used,
            "gas_wanted": transaction.gas_wanted,
            "num_events": transaction.num_events,
            "root_hash": transaction.root_hash,
            "tx": transaction.tx,
            "data": transaction.data,
            "raw_data": transaction.raw_data,
            "raw_log": transaction.raw_log,
        }
