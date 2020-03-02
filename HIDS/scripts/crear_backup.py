import funciones_globales as fg
import json 
import hashlib as hl
import shutil


def create_backup(path):
    shutil.copytree(path,"C:/primer-entregable/backup")
    hashDict = fg.hash_files(path)
    jsonDump = json.dumps(hashDict)
    f = open("C:/primer-entregable/hash_backup.json", "w")
    f.write(jsonDump)
    f.close()

def config():
    sha = fg.sha_search()
    items = fg.hash_files("C:/primer-entregable/dir_pruebas/").items()
    with open("C:/primer-entregable/config.txt", mode='r+') as text:
        a = text.read()
        for k in items:
            if k[1] not in a:
                text.write("\n" + "----------" + sha + "----------" + "\n" + str(k) + "\n")
    text.close()


def main():
    config()
    create_backup("C:/primer-entregable/dir_pruebas")

#!/usr/bin/env python3
main()
