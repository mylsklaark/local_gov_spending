# OCC Spending

A data pipeline that downloads Oxfordshire County Council's monthly transparency spending data (transactions over £500, published as open Excel sheets), loads it into DuckDB, and uses dbt to model it into analytical layers.

## Project structure

```
occ_spending/
├── data/          # Raw .xlxs downloaded from OCC (gitignored)
├── ingest/        # Python ingestion scripts
│   └── ingest.py  # Downloads .xlxs and loads them into DuckDB
└── transform/     # dbt project
    ├── models/
    │   ├── staging/   # Light cleaning on raw data, one model per source
    │   └── marts/     # Analytical models (by supplier, category, department)
    ├── tests/         # Data quality tests
    └── dbt_project.yml
```

## Setup

1. Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```
   pip install dbt-duckdb
   ```

3. Verify dbt can connect:
   ```
   cd transform
   dbt debug
   ```

## Usage

Run the ingestion script to download .xlxs files and load into DuckDB:
```
python ingest/ingest.py
```

Then run dbt to build the models:
```
cd transform
dbt run
```
