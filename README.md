## BGCFlow dbt-duckdb implementation
Shamelessly adapted from https://github.com/dbt-labs/jaffle_shop_duckdb

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
source venv/bin/activate
dbt build
dbt docs generate
dbt docs serve
```