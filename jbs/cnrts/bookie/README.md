### Requirements:
Create the file below with your coinbase credentials:
```bookie/cb.py
COIN_BASE_CRED = {
   "name": "coinbase key name",
   "privateKey": "coinbase private key",
}
```

### Installation:
```bash
python -mvenv .venv
. .venv/bin/activate
pip install -e .
```

### Run:
```bash
. .venv/bin/activate
python bookle/cli.py --help
```

### Tests:
```bash
. .venv/bin/activate
pip install -e ".[test]"
pytest bookie
```
