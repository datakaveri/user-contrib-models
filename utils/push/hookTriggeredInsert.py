#!/usr/local/bin/python3
import json
import os
from os import walk
import glob
import shutil
import requests

from collections import OrderedDict
from distutils.dir_util import copy_tree

cert_file = "keys/cert.pem"
key_file = "keys/private-key.pem"

data_models_dir = "data-models"

excluded = ["utils", ".git"]


# Recursively list out classes and properties paths
files = []

for (dirpath, dirnames, filenames) in os.walk(data_models_dir):
    for fl in filenames:
        if (fl.split(".")[-1] == "jsonld"):
            with open(dirpath + "/" + fl, "r") as f:
                files.append(json.load(f))

cert = (cert_file, key_file)
auth_api = "https://auth.iudx.org.in/auth/v1/token"
auth_headers = {"content-type": "application/json"}
payload = { "request" : [ {"id": "datakaveri.org/f7e044eee8122b5c87dce6e7ad64f3266afa41dc/voc.iudx.org.in/*"} ] }
# Obtain token from auth server
token = requests.post(auth_api, data=json.dumps(payload),
                        headers=auth_headers, cert=cert).json()["token"]


url = "https://voc.iudx.org.in/descriptor/"
voc_headers = {"token": token, "content-type": "application/ld+json", "accept": "application/ld+json"}
for fl in files:
    r = requests.post(url+fl["name"], json.dumps(fl), headers=voc_headers, cert=cert)



