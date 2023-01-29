# Wrapper for THC-Hydra

Dehydrated is a project that provides a convenient Python3 library interface for the [**THC-Hydra**](https://github.com/vanhauser-thc/thc-hydra) password cracking tool. It abstracts the functionality of THC-Hydra and presents it in a way that is easy for Python developers to use. With Dehydrated, developers can leverage the power of THC-Hydra for password cracking tasks in their own Python applications, without having to delve into the intricacies of the underlying tool. This makes it an ideal solution for those who need to automate password cracking tasks in their workflows.

## Disclaimer
Dehydrated is a software tool for password cracking and should not be used for any illegal activities. The authors and contributors of Dehydrated do not condone or support the use of this software for illegal purposes and cannot be held responsible for any misuse of the software. By using Dehydrated, you acknowledge and agree to use it only for lawful purposes.

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
