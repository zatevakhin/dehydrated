from dehydrated import run_hydra

from dehydrated.modules import HttpsHead, Ssh


r_https_head = HttpsHead(
    target="httpbin.org",
    # service_port=80,
    logins=["demo"],
    passwords=["demo"],
    path="/basic-auth/demo/demo",
)


# print(run_hydra(r_https_head))
print(run_hydra(r_https_head))
