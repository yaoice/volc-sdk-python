#  -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../../")
from volcengine.example.veen import ak, sk
from volcengine.veen.service import VeenService

if __name__ == "__main__":
    svc = VeenService()
    svc.set_ak(ak)
    svc.set_sk(sk)

    body = {
        "instance_identities": [
            "veen26301302623093022820",
            "veen25200031222138400005",
            "veen38855042004824221584",
        ],
        "ignore_running": True,
    }

    resp = svc.offline_instances(body)
    print(resp)
