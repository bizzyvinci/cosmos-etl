# Cosmos ETL
Cosmos ETL lets you convert cosmos blockchain data into convenient formats like CSV and JSON. This project was inspired by [ethereum etl](https://github.com/blockchain-etl/ethereum-etl).

## Quickstart
Export blocks
`python3 -m cosmosetl export_blocks -s 2000000 -e 2001000 -p https://tendermint.bd.evmos.org:26657 -o blocks.csv`

Export transactions and events
`python3 -m cosmosetl export_transactions_and_events -s 2000000 -e 2001000 -p https://tendermint.bd.evmos.org:26657 -to transactions.csv -eo events.csv`
