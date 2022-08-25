import click

from blockchainetl_common.logging_utils import logging_basic_config
from cosmosetl.jobs.export_transactions_job import ExportTransactionsJob
from cosmosetl.jobs.exporters.transactions_and_events_item_exporter import transactions_and_events_item_exporter
from cosmosetl.providers.auto import get_provider_from_uri
from cosmosetl.thread_local_proxy import ThreadLocalProxy

logging_basic_config()


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-s', '--start-block', default=0, show_default=True, type=int, help='Start block')
@click.option('-e', '--end-block', required=True, type=int, help='End block')
@click.option('-b', '--batch-size', default=100, show_default=True, type=int, help='The number of blocks to export at a time.')
@click.option('-p', '--provider-uri', required=True, type=str, help='The URI of tendermint RPC')
@click.option('-w', '--max-workers', default=5, show_default=True, type=int, help='The maximum number of workers.')
@click.option('-to', '--transactions-output', default=None, show_default=True, type=str, help='Output file for transactions (ending with .csv or .json)')
@click.option('-eo', '--events-output', default=None, show_default=True, type=str, help='Output file for events (ending with .csv or .json)')
def export_transactions_and_events(start_block, end_block, batch_size, provider_uri, max_workers, transactions_output, events_output):
    job = ExportTransactionsJob(
        start_block=start_block,
        end_block=end_block,
        batch_size=batch_size,
        batch_web3_provider=ThreadLocalProxy(lambda: get_provider_from_uri(provider_uri, batch=True)),
        max_workers=max_workers,
        item_exporter=transactions_and_events_item_exporter(transactions_output, events_output),
        export_transactions=transactions_output is not None,
        export_events=events_output is not None
    )
    job.run()
