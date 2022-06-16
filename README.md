# Jobs

Simple tools for python concurrency and parallelism.

## Install

Pip install this repo.

## Usage

```python
import numpy as np
from jobs import MultiprocessJobs

jobs = MultiprocessJobs()

for _ in range(100):
    jobs.add(np.square, np.random.rand(100, 100))

results = jobs.execute()
```