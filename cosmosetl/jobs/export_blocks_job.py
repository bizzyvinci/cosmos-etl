import json
from blockchainetl_common.jobs.base_job import BaseJob
from blockchainetl_common.executors.batch_work_executor import BatchWorkExecutor
from cosmosetl.mappers.block_mapper import CosmBlockMapper
from cosmosetl.json_rpc_requests import generate_get_block_by_number_json_rpc
from cosmosetl.utils import validate_range, rpc_response_batch_to_results

class ExportBlocksJob(BaseJob):
    def __init__(self, start_block, end_block, batch_size, batch_web3_provider,
                max_workers, item_exporter):
        validate_range(start_block, end_block)
        self.start_block = start_block
        self.end_block = end_block

        self.batch_web3_provider = batch_web3_provider

        self.batch_work_executor = BatchWorkExecutor(batch_size, max_workers)
        self.item_exporter = item_exporter
        self.block_mapper = CosmBlockMapper()
        
    def _start(self):
        self.item_exporter.open()
    
    def _export(self):
        self.batch_work_executor.execute(
            range(self.start_block, self.end_block + 1),
            self._export_batch,
            total_items=self.end_block - self.start_block + 1
        )
    
    def _export_batch(self, block_number_batch):
        blocks_rpc = list(generate_get_block_by_number_json_rpc(block_number_batch))
        response = self.batch_web3_provider.make_batch_request(json.dumps(blocks_rpc))
        results = rpc_response_batch_to_results(response)
        blocks = [self.block_mapper.json_dict_to_block(result) for result in results]

        for block in blocks:
            self._export_block(block)

    def _export_block(self, block):
        self.item_exporter.export_item(self.block_mapper.block_to_dict(block))

    def _end(self):
        self.batch_work_executor.shutdown()
        self.item_exporter.close()
