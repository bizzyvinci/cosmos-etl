from blockchainetl_common.logging_utils import logging_basic_config
logging_basic_config()

import click

from cosmosetl.cli.export_blocks import export_blocks
from cosmosetl.cli.export_transactions_and_events import export_transactions_and_events

@click.group()
@click.version_option(version='0.0.1')
@click.pass_context
def cli(ctx):
    pass


# export
cli.add_command(export_blocks, "export_blocks")
cli.add_command(export_transactions_and_events, "export_transactions_and_events")
