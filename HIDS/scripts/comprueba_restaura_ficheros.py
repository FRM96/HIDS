import hashlib as hl
import os
import time
import shutil
import json
import funciones_globales as fg

def attack_log(key):
    log = open("C:/primer-entregable/attack.log", "a+")
    log.write("El archivo " + key + " ha sido modificado. Se ha detectado a las " + str(time.localtime().tm_hour) + ":"
              + str(time.localtime().tm_min) + " del " + str(time.localtime().tm_mday) + "/" + str(
        time.localtime().tm_mon) + "/"
              + str(time.localtime().tm_year) + "\n")
    log.close()

def attack_log2(key):
    log = open("C:/primer-entregable/attack.log", "a+")
    log.write("El archivo " + key + " ha sido introducido sin permiso. Se ha detectado a las " + str(time.localtime().tm_hour) + ":"
              + str(time.localtime().tm_min) + " del " + str(time.localtime().tm_mday) + "/" + str(
        time.localtime().tm_mon) + "/"
              + str(time.localtime().tm_year) + "\n")
    log.close()


def compare_hash(path):
    new_hash = fg.hash_files(path)
    with open("C:/primer-entregable/hash_backup.json") as js:
        hash_backup = json.load(js)

    for hb in hash_backup.items():
        key = hb[0]
        if not bool(new_hash) or not bool(hash_backup):
            print("No quedan archivos en los directorios")
            break
        elif key not in new_hash or new_hash[key] != hash_backup[key]:
            print("El archivo " + key + " ha sido modificado o eliminado. Restaurando BBDD")
            #attack_log(key)
        else:
            print("El archivo " + key + " no ha sido modificado")

    for hb in new_hash.items():
        key = hb[0]
        if not bool(new_hash) or not bool(hash_backup):
            print("No quedan archivos en los directorios")
            break
        elif key not in hash_backup:
            print("El archivo" + key + " ha sido introducido sin permiso. Restaurando BBDD")
            #attack_log2(key)

    for hb in hash_backup.items():
        key = hb[0]
        if not bool(new_hash) or not bool(hash_backup):
            print("No quedan archivos en los directorios")
            break
        elif key not in new_hash or new_hash[key] != hash_backup[key]:
            shutil.rmtree(path)
            shutil.copytree("C:/primer-entregable/backup", path)
            break

    for hb in new_hash.items():
        key = hb[0]
        if not bool(new_hash) or not bool(hash_backup):
            print("No quedan archivos en los directorios")
            break
        elif key not in hash_backup:
            shutil.rmtree(path)
            shutil.copytree("C:/primer-entregable/backup", path)
            break

def main():
    compare_hash("C:/primer-entregable/dir_pruebas")

#!/usr/bin/env python3
main()
