import hashlib as hl
import os
import time
import shutil
import json
import random
import funciones_globales as fg
import string

def randomString(s):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(s))

def attack_log(key):
    log = open("C:/primer-entregable/attack.log", "a+")
    log.write("["+ key + "] ha sido modificado. {" + str(time.localtime().tm_hour) + ":"
              + str(time.localtime().tm_min) + "-" + str(time.localtime().tm_mday) + "/" + str(
        time.localtime().tm_mon) + "/"
              + str(time.localtime().tm_year) + "}\n")
    log.close()

def count_log(x):
    log = open("C:/primer-entregable/attack.log", "a+")
    log.write("----------> "+x+" <----------"+"\n")


def random_attack(path):
    files = fg.scan_dir(path)
    random_bool = bool(random.getrandbits(1))
    random_list = random.sample(range(len(files)), random.randint(0, len(files)))
    for x in random_list:
        os.remove(files[x])
    if random_bool:
        dir = random.choice(fg.random_dir(path))
        print("Se han creado archivos aleatorios")
        for _ in range(random.randint(1, 10)):
            n = random.randint(1, 16)
            fd = open(dir+"/"+randomString(n)+".txt", 'w')
            fd.write(randomString(300))
            fd.close()

def random_edit(path):
    files = []
    count = 0
    new_hash = fg.hash_files(path)
    with open("C:/primer-entregable/hash_backup.json") as js:
        hash_backup = json.load(js)
    for x in new_hash.keys():
        if new_hash[x] == hash_backup[x]:
            files.append(x)
    if len(files) == 0:
        print(len(files))
        print("Todos los archivos han sido modificados")
    else:
        random_len = random.randint(6,15)
        if len(files) > random_len:
            random_dir = random.sample(files,random_len)
        else:
            random_dir = random.sample(files,len(files))
        for x in random_dir:
            print("el archivo "+x+" ha sido modificado")
            attack_log(x)
            open(x,'a').write(randomString(700))
    new_hash = fg.hash_files(path)
    for x in hash_backup.values():
        if x not in new_hash.values():
            count = count + 1
    print("Se han editado "+str(count)+" Elementos. Quedan "+ str(len(new_hash.values()) - count)+". La tasa de modificación es de "+str(count/(len(hash_backup.values()))))
    count_log(str(count/len(hash_backup.values())))

def main():
    random_edit("C:/primer-entregable/dir_pruebas/")

#!/usr/bin/env python3
main()
