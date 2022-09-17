# Cosmos ETL
Cosmos ETL lets you convert cosmos blockchain data into convenient formats like CSV and JSON. This project was inspired by [ethereum etl](https://github.com/blockchain-etl/ethereum-etl).

## Quickstart
Install cosmos-etl pypi package
```bash
> pip install cosmos-etl
```

Export blocks

```bash
> cosmosetl export_blocks -s 2000000 -e 2001000 -p https://tendermint.bd.evmos.org:26657 -o blocks.csv
```

Export transactions and events

```bash
> cosmosetl export_transactions_and_events -s 2000000 -e 2001000 -p https://tendermint.bd.evmos.org:26657 -to transactions.csv -eo events.csv
```

Get block range for date

```bash
> cosmosetl get_block_range_for_date -p https://tendermint.bd.evmos.org:26657 -d 2022-05-12
```

Get block range for timestamps
```bash
> cosmosetl get_block_range_for_timestamps -p https://tendermint.bd.evmos.org:26657 -s 1661708854 -e 1661808854
```
