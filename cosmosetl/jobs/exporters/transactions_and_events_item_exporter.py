from blockchainetl_common.jobs.exporters.composite_item_exporter import CompositeItemExporter

TRANSACTION_FIELDS_TO_EXPORT = [
    'hash',
    'height',
    'index',
    'code',
    'gas_used',
    'gas_wanted',
    'num_events',
    'root_hash',
    'tx',
    'data',
    'raw_data',
    'raw_log',
]

EVENT_FIELDS_TO_EXPORT = [
    '_type',
    'attributes',
    'tx_hash'
]


def transactions_and_events_item_exporter(transactions_output=None, events_output=None):
    return CompositeItemExporter(
        filename_mapping={
            'transaction': transactions_output,
            'event': events_output
        },
        field_mapping={
            'transaction': TRANSACTION_FIELDS_TO_EXPORT,
            'event': EVENT_FIELDS_TO_EXPORT
        }
    )