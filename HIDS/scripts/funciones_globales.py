#!/usr/bin/env python3
import hashlib as hl
import os
import time
import shutil
import json

def sha_search():
    with open("C:/primer-entregable/config.txt", mode='r') as text:
        for line in text:
            if "algoritmo" in line:
                s = line.split()
                sha = s[-1]
    return sha

def create_hash(path):
    with open(path, mode='rb') as message:
        sha = sha_search()
        if sha == "SHA256":
            h = hl.sha256(message.read()).hexdigest()
        elif sha == "SHA224":
            h = hl.sha224(message.read()).hexdigest()
        elif sha == "SHA384":
            h = hl.sha384(message.read()).hexdigest()
        else:
            h = hl.sha512(message.read()).hexdigest()
    return h


def scan_dir(path):
    files = []
    list_file = os.listdir(path)
    for entry in list_file:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            files = files + scan_dir(full_path)
        elif entry.startswith('.'):
            continue
        else:
            files.append(full_path)
    return files

def random_dir(path):
    dir = []
    for (dirpath, _, _) in os.walk(path):
        dir.append(dirpath)
    return dir

def hash_files(path):
    dirs = scan_dir(path)
    hashdict = {}
    for d in dirs:
        hashdict[d] = create_hash(str(d))
    return hashdict


