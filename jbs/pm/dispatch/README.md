### Requirements:
- source installable package `dispatch` [included with submission]
 - `dispatch-1.0.0.tar.gz`
 - `dispatch-tests.tar.gz`
- decorate functions with generic or adts [assuming 0 or more args]
  - `valid_usage.py`
- can't decorate duplicated signatures [name+args+return]
 - `assert_uni_sig.py`
- only single decorator `register` is accesible [_mangiling didn't work_]
 - `assert_prv_cls.py`
 - `assert_prv_var.py`

### Installation:
```bash
python -mvenv .venv
. .venv/bin/activate
python -mpip install dispatch-1.0.0.tar.gz
```

### Tests:
```bash
tar xvfz dispatch-tests.tar.gz
python valid_usage.py
python assert_uni_sig.py
python assert_prv_cls.py.py
python assert_prv_var.py.py
```
