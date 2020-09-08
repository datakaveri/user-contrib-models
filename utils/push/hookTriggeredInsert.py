#!/usr/local/bin/python3
import json
import os
from os import walk
import glob
import shutil
import requests

from collections import OrderedDict
from distutils.dir_util import copy_tree


data_models_dir = "data-models"

excluded = ["utils", ".git"]


# Recursively list out classes and properties paths
files = []

for (dirpath, dirnames, filenames) in os.walk(data_models_dir):
    for fl in filenames:
        if (fl.split(".")[-1] == "jsonld"):
            with open(dirpath + "/" + fl, "r") as f:
                files.append(json.load(f))

token = ""
with open("../config/vocserver.json", "r") as f:
    token = json.load(f)["vocserver.jkspasswd"]

url = "https://voc.iudx.org.in/descriptor/"
voc_headers = {"token": token, "content-type": "application/ld+json", "accept": "application/ld+json"}
for fl in files:
    r = requests.post(url+fl["name"], json.dumps(fl), headers=voc_headers)



