from blockchainetl_common.logging_utils import logging_basic_config
logging_basic_config()

import click

from cosmosetl.cli.export_blocks import export_blocks
from cosmosetl.cli.export_transactions_and_events import export_transactions_and_events
from cosmosetl.cli.get_block_range_for_date import get_block_range_for_date
from cosmosetl.cli.get_block_range_for_timestamps import get_block_range_for_timestamps

@click.group()
@click.version_option(version='0.0.2')
@click.pass_context
def cli(ctx):
    pass


# export
cli.add_command(export_blocks, "export_blocks")
cli.add_command(export_transactions_and_events, "export_transactions_and_events")
cli.add_command(get_block_range_for_date, "get_block_range_for_date")
cli.add_command(get_block_range_for_timestamps, "get_block_range_for_timestamps")
