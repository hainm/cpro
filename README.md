juprog
======
Circle progress for Jupyter notebook

Basic Example
=============

```python

from time import sleep
from juprog import CircleProgress

for x in range(CircleProgress(sequence)):
    # fake long process
    sleep(0.2)

Use [progress-circle](https://github.com/iammary/progress-circle) for displaying progress. 
