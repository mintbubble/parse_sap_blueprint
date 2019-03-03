import os
import codecs
import shutil
import re

path = input()
path_rename = os.path.join(path, "RENAME_FILE")
file_docs = os.path.join(path_rename, "solar01_structure.txt")
last_step = {}  # last step - document
z = 30  # how much cut off the name!

# make the dictionary the last step - the document from "solar01_structure.txt"
with open(file_docs, encoding='utf8') as f:
    for i in f:
        i = i.replace("\n", "")
        p = i.split("\\")
        x = p[len(p) - 2][:z].strip()
        y = p[len(p) - 1].strip()
        if x == "Организационные единицы" or x == "Основные данные" or x == "Бизнес-процессы" or x == "Бизнес-сценарии":
            x = p[len(p) - 3][:z].strip()
        if x not in last_step.keys():
            last_step[x] = ["*"]
            b = last_step.get(x)
            b.append(y)
            last_step[x] = b
        else:
            b = last_step.get(x)
            b.append(y)
            last_step[x] = b

file = os.path.join(path, "blue.dat")
file_lines = []
direct = []
with codecs.open(file, "r", "utf_16_le") as f:
    file_lines = [str(line.replace('\n', "")) for line in f]

# structure processing (up to the first line with code 100 - file)
for i in range(file_lines.index("100") - 3):
    direct.append(file_lines[i].strip())

nodes_name = dict(zip(direct[1::6], direct[5::6]))
nodes_num = dict(zip(direct[1::6], direct[3::6]))
nodes_type = dict(zip(direct[1::6], direct[2::6]))
scenars = [i for i in nodes_name if nodes_type[i] == "BMSC"]
process = [i for i in nodes_name if nodes_type[i] == "BMPG"]
steps = [i for i in nodes_name if nodes_type[i] == "BMPC"]

# kill special characters in nodes_name ["\\","/",":","*","?","\"","<",">","|"]
match = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]
for n in nodes_name:
    for i in match:
        nodes_name[n] = nodes_name[n].replace(i, "")

# we cut the name to the length set at the beginning
for n in nodes_name:
    if len(nodes_name[n]) > z:
        nodes_name[n] = nodes_name[n][:z].strip()

# delete downloaded and unused documents
name = ["\(не исп", "\(не акт", "\(пер"]
for key in last_step.keys():
    b = last_step.get(key)
    c = []
    for doc in b:
        for nam in name:
            search = re.search(nam, doc.lower())
            if search:
                c.append(doc)
    for item in c:
        b.remove(item)
    last_step[key] = b

# decomposed into folders
used = []

for i, val in enumerate(scenars):
    path_scenario = os.path.join(path_rename, nodes_name[val])
    if not os.path.exists(path_scenario):
        os.makedirs(path_scenario)
    if nodes_name[val] in last_step.keys():
        used.append(nodes_name[val])
        a = last_step.get(nodes_name[val])
        for k in a:
            if k != "*":
                shutil.copyfile(os.path.join(path_rename, k), os.path.join(path_scenario, k))
    for j, valj in enumerate(process):
        if i != len(scenars) - 1:
            if val <= valj < scenars[i + 1]:
                path_process = os.path.join(path_scenario, nodes_name[valj])
                if not os.path.exists(path_process):
                    os.makedirs(path_process)
                if nodes_name[valj] in last_step.keys():
                    used.append(nodes_name[valj])
                    a = last_step.get(nodes_name[valj])
                    for k in a:
                        if k != "*":
                            shutil.copyfile(os.path.join(path_rename, k), os.path.join(path_process, k))
                for m, valm in enumerate(steps):
                    if j != len(steps) - 1:
                        if valj <= valm < process[j + 1]:
                            path_step = os.path.join(path_process, nodes_name[valm])
                            if not os.path.exists(path_step):
                                os.makedirs(path_step)
                            if nodes_name[valm] in last_step.keys():
                                used.append(nodes_name[valm])
                                a = last_step.get(nodes_name[valm])
                                for k in a:
                                    if k != "*":
                                        shutil.copyfile(os.path.join(path_rename, k), os.path.join(path_step, k))
                    else:
                        if valj <= valm:
                            path_step = os.path.join(path_process, nodes_name[valm])
                            if not os.path.exists(path_step):
                                os.makedirs(path_step)
                            if nodes_name[valm] in last_step.keys():
                                used.append(nodes_name[valm])
                                a = last_step.get(nodes_name[valm])
                                for k in a:
                                    if k != "*":
                                        shutil.copyfile(os.path.join(path_rename, k), os.path.join(path_step, k))
        else:
            if val <= valj:
                path_process = os.path.join(path_scenario, nodes_name[valj])
                if not os.path.exists(path_process):
                    os.makedirs(path_process)
                if nodes_name[valj] in last_step.keys():
                    used.append(nodes_name[valj])
                    a = last_step.get(nodes_name[valj])
                    for k in a:
                        if k != "*":
                            shutil.copyfile(os.path.join(path_rename, k), os.path.join(path_process, k))
                for m, valm in enumerate(steps):
                    if j != len(steps) - 1:
                        if valj <= valm < process[j + 1]:
                            path_step = os.path.join(path_process, nodes_name[valm])
                            if not os.path.exists(path_step):
                                os.makedirs(path_step)
                            if nodes_name[valm] in last_step.keys():
                                used.append(nodes_name[valm])
                                a = last_step.get(nodes_name[valm])
                                for k in a:
                                    if k != "*":
                                        shutil.copyfile(os.path.join(path_rename, k), os.path.join(path_step, k))
                    else:
                        if valj <= valm:
                            path_step = os.path.join(path_process, nodes_name[valm])
                            if not os.path.exists(path_step):
                                os.makedirs(path_step)
                            if nodes_name[valm] in last_step.keys():
                                used.append(nodes_name[valm])
                                a = last_step.get(nodes_name[valm])
                                for k in a:
                                    if k != "*":
                                        shutil.copyfile(os.path.join(path_rename, k), os.path.join(path_step, k))

for n in list(set.difference(set(last_step) - set(used))):
    path_empty = os.path.join(path_rename, "ЕАСУП. Шаблон")
    if not os.path.exists(path_empty):
        os.makedirs(path_empty)
    a = last_step.get(n)
    for k in a:
        if k != "*":
            shutil.copyfile(os.path.join(path_rename, k), os.path.join(path_empty, k))
print("pass")
