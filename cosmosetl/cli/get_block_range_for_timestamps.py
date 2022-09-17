import click
from datetime import datetime

from blockchainetl_common.file_utils import smart_open
from blockchainetl_common.logging_utils import logging_basic_config
from cosmosetl.providers.auto import get_provider_from_uri
from cosmosetl.service.cosm_service import CosmService

logging_basic_config()


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-p', '--provider-uri', required=True, type=str, help='The URI of tendermint RPC')
@click.option('-s', '--start-timestamp', required=True, type=int, help='Start unix timestamp, in seconds.')
@click.option('-e', '--end-timestamp', required=True, type=int, help='End unix timestamp, in seconds.')
@click.option('-o', '--output', default='-', show_default=True, type=str, help='The output file. If not specified stdout is used.')
def get_block_range_for_timestamps(provider_uri, start_timestamp, end_timestamp, output):
    """Outputs start and end blocks for given date."""
    provider = get_provider_from_uri(provider_uri)
    cosm_service = CosmService(provider)

    start_block, end_block = cosm_service.get_block_range_for_timestamps(start_timestamp, end_timestamp)

    with smart_open(output, 'w') as output_file:
        output_file.write('{},{}\n'.format(start_block, end_block))
