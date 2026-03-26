# WAXS Cellulose

Tools for analyzing wide-angle X-ray scattering (WAXS) data for cellulosic materials.

## Installation

```bash
pip install -e .
```

## Quick example

```python
from waxs_cellulose.pipeline import run_pipeline

result = run_pipeline("data/sample.csv")
print(result.fit_report())
```
