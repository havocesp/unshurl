# UNSHURL

- Author: Daniel J. Umpierrez
- License: UNLICENSE

## Description

Just another short to long URL converter application.

## Install

```bash
> pip3 install git+https://github.com/havocesp/unshurl
```

## Usage

```python
from unshurl.core import unshurl, shurl

# URL to short or un-short
url = 'https://github.com/havocesp/unshurl'
# URL short
url = shurl(url)
print(url)
# URL un-short
url = unshurl(url)
print(url)
```

## Changelog

### v0.1.1

- Added URL short feature.

### v0.1.0

- Initial version
