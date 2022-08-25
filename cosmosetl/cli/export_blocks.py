from email.policy import default
import click

from blockchainetl_common.logging_utils import logging_basic_config
from cosmosetl.jobs.export_blocks_job import ExportBlocksJob
from cosmosetl.jobs.exporters.blocks_item_exporter import blocks_item_exporter
from cosmosetl.providers.auto import get_provider_from_uri
from cosmosetl.thread_local_proxy import ThreadLocalProxy

logging_basic_config()


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-s', '--start-block', default=0, show_default=True, type=int, help='Start block')
@click.option('-e', '--end-block', required=True, type=int, help='End block')
@click.option('-b', '--batch-size', default=100, show_default=True, type=int, help='The number of blocks to export at a time.')
@click.option('-p', '--provider-uri', required=True, type=str, help='The URI of tendermint RPC')
@click.option('-w', '--max-workers', default=5, show_default=True, type=int, help='The maximum number of workers.')
@click.option('-o', '--output', required=True, type=str, help='Output file for blocks (ending with .csv or .json)')
def export_blocks(start_block, end_block, batch_size, provider_uri, max_workers, output):
    job = ExportBlocksJob(
        start_block=start_block,
        end_block=end_block,
        batch_size=batch_size,
        batch_web3_provider=ThreadLocalProxy(lambda: get_provider_from_uri(provider_uri, batch=True)),
        max_workers=max_workers,
        item_exporter=blocks_item_exporter(output)
    )
    job.run()
