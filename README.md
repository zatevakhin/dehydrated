# Wrapper for THC-Hydra

Dehydrated it's a project which wraps the [**thc-hydra**](https://github.com/vanhauser-thc/thc-hydra) as a Python3 library.

## Usage

```python

from dehydrated.modules import HttpHeadShot, HttpHeadBurst
from dehydrated import run_hydra

# To check only one login/password pair #Shot
hs = HttpHeadShot(
        target="httpbin.org",
        service_port=80,
        login="demo",
        password="demo",
        path="/basic-auth/demo/demo"
    )

print(run_hydra(hs))
# [{'port': '80',
#   'module': 'http-head',
#   'host': 'httpbin.org',
#   'login': 'demo',
#   'passwd': 'demo'}]

# To check logins/passwords lists #Burst
hb = HttpHeadBurst(
        target="httpbin.org",
        service_port=80,
        logins=["admin", "root", "demo"],
        passwords=["1234", "toor","demo"],
        path="/basic-auth/demo/toor"
    )

print(run_hydra(hb))
# [{'port': '80',
#   'module': 'http-head',
#   'host': 'httpbin.org',
#   'login': 'demo',
#   'passwd': 'toor'}]

```
