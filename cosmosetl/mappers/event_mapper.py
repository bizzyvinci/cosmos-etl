import json
from cosmosetl.domain.event import CosmEvent
from cosmosetl.utils import b64decode

class CosmEventMapper:
    def json_dict_to_event(self, json_dict, tx_hash=None):
        event = CosmEvent()
        event._type = json_dict.get("type")
        attributes = json.dumps([
            {'key': b64decode(attr.get('key')), 'value': b64decode(attr.get('value'))}
            for attr in json_dict.get("attributes", [])
        ])
        event.attributes = attributes if attributes else None
        event.tx_hash = tx_hash
        return event
        
    def event_to_dict(self, event):
        return {
            "type": "event",
            "_type": event._type,
            "attributes": event.attributes,
            "tx_hash": event.tx_hash
        }
