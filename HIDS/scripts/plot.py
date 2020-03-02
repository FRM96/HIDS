#!/usr/bin/env python3
import hashlib as hl
import os
import time
import shutil
import json
import random
import string
import matplotlib.pyplot as plt
import numpy as np

def generate_graphics(d):
    dict_x = list(d.keys())
    dates = []
    days = []
    for st in dict_x:
        i = st.find(':')
        j = st.find("-")
        hour = (st[i-2:i+3])
        k = st.find("/")
        dates.append(st[j+1:j+11])
        days.append(st[j+1:k])
    x = list(map(int,days))
    y = list(map(float,d.values()))
    plt.plot(x, y,marker='o')
    plt.xticks(np.arange(min(x),max(x)+1,1),dates,size=6.5)
    plt.yticks(np.arange(0,1.1,0.1))
    plt.title("Evolución de los ataques realizados")
    plt.xlabel("Fecha")
    plt.ylabel("Tasa de archivos modificados")
    plt.show()
    plt.savefig('C:/primer-entregable/attack_graph.png')


def data_dict():
    aux_keys = []
    values = []
    dict_graph = {}
    with open("C:/primer-entregable/attack.log") as text:
        for line in text.readlines():
            line = line.strip()
            i = line.find("{")
            j = line.find("}")
            k = line.find(">")
            z = line.find("<")
            if "{" in line:
                aux_keys.append(line[i+1:j])
            else:
                values.append(line[k+2:z-1])
        keys = list(dict.fromkeys(aux_keys))
    for i in range(len(keys)):
        dict_graph[keys[i]] = values[i]
    return dict_graph

def main():
    generate_graphics(data_dict())

main()
