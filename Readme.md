# Tide-query

# Usage
```shell script
pip install tide-query
```

# Example

### First

Now you need install dependent packages before.
```shell script
pip install -r requirement.txt
```
> If you in Chinese Mainland, I highly recommend you use pip mirrors source by following.
```shell script
pip install -r requirement.txt -i https://mirrors.aliyun.com/pypi/simple/
```

### Second

Write your `excel` file. Make its format of content like following:

| 单词 | 音标1 | 音标2 | 结果 |
| --- | --- | --- | ---| 
| Chinese | | | |
| English | | | |
| Japanese | | | |
| ... | | | |

### Third

Change `SOURCE_EXCEL` and `TARGET_EXCEL` from `demo.py`  

> The `SOURCE_EXCEL` is a path of source `excel file`.  
> The `excel file` format like above table and it's you wrote.

> The `TARGET_EXCEL` is also a path of `excel file`.
> But the `excel file` will has been written by `demo.py`.
file `demo.py`:
```python
from typing import List

import pandas as pd

from tide_query import YouDaoQuery, TideQuery as Tq

SOURCE_EXCEL = '/xx/xx.xlsx'  # 源excel路径
TARGET_EXCEL = '/xx/xx.xlsx'  # 目标excel路径 (建议不要与源excel为同一个文件)

if __name__ == "__main__":
    ...
```

### Other config you can see comment of `demo.py` first.

Now, you can running this `demo.py` file.
```shell script
python demo.py
```
