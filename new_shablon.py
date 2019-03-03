import os
import codecs

path = input()
path_rename = os.path.join(path, "RENAME_FILE")
file_docs = os.path.join(path_rename, "solar01_structure.txt")
last_step = {}  # last step - document

with open(file_docs, encoding='utf8') as f:
    for i in f:
        i = i.replace("\n", "")
        p = i.split("\\")
        if p[len(p) - 2] not in last_step.keys():
            last_step[p[len(p) - 2]] = ["*"]
            b = last_step.get(p[len(p) - 2])
            b.append(p[len(p) - 1])
            last_step[p[len(p) - 2]] = b
        else:
            b = last_step.get(p[len(p) - 2])
            b.append(p[len(p) - 1])
            last_step[p[len(p) - 2]] = b

file = os.path.join(path, "blue.dat")
file_lines = []
direct = []
with codecs.open(file, "r", "utf_16_le") as f:
    file_lines = [str(line.replace('\n', "")) for line in f]

for i in range(file_lines.index("100") - 3):
    direct.append(file_lines[i])

nodes_name = dict(zip(direct[1::6], direct[5::6]))
nodes_num = dict(zip(direct[1::6], direct[3::6]))
nodes_type = dict(zip(direct[1::6], direct[2::6]))
scenars = [i for i in nodes_name if nodes_type[i] == "BMSC"]
process = [i for i in nodes_name if nodes_type[i] == "BMPG"]
steps = [i for i in nodes_name if nodes_type[i] == "BMPC"]

# make a pattern
used = []
with open(os.path.join(path_rename, "new_shablon.txt"), 'w', encoding='utf8') as f:
    f.truncate()
    for i, val in enumerate(scenars):
        f.writelines("\tCreate a scenario\t1\tSCN\t{0}\t\t\t\n".format(nodes_name[val]))
        if nodes_name[val] in last_step.keys():
            used.append(nodes_name[val])
            a = last_step.get(nodes_name[val])
            for k in a:
                if k != "*":
                    f.writelines(
                        " \t\t2\tKWOBJ\t{0}\tsmd_doctype\tZSB_0009\t\n \t\t\t\t\tsmd_state\t0IN_PROGRESS\n \t\t\t\t\tsmd_responsible\tname\n \t\t\t\t\t$FILE_PATH\t{1}\n".format(
                            k, os.path.join(path_rename, k)))
        for j, valj in enumerate(process):
            if i != len(scenars) - 1:
                if val <= valj < scenars[i + 1]:
                    f.writelines("\tCreate process\t2\tPROC\t{0}\t\t\t\n".format(nodes_name[valj]))
                    if nodes_name[valj] in last_step.keys():
                        used.append(nodes_name[valj])
                        a = last_step.get(nodes_name[valj])
                        for k in a:
                            if k != "*":
                                f.writelines(
                                    " \t\t3\tKWOBJ\t{0}\tsmd_doctype\tZSB_0009\t\n \t\t\t\t\tsmd_state\t0IN_PROGRESS\n \t\t\t\t\tsmd_responsible\tname\n \t\t\t\t\t$FILE_PATH\t{1}\n".format(
                                        k, os.path.join(path_rename, k)))
                    for m, valm in enumerate(steps):
                        if j != len(steps) - 1:
                            if valj <= valm < process[j + 1]:
                                f.writelines("\tCreate step\t3\tREF_PROCSTEP\t{0}\t\t\t\n".format(nodes_name[valm]))
                                if nodes_name[valm] in last_step.keys():
                                    used.append(nodes_name[valm])
                                    a = last_step.get(nodes_name[valm])
                                    for k in a:
                                        if k != "*":
                                            f.writelines(
                                                " \t\t4\tKWOBJ\t{0}\tsmd_doctype\tZSB_0009\t\n \t\t\t\t\tsmd_state\t0IN_PROGRESS\n \t\t\t\t\tsmd_responsible\tname\n \t\t\t\t\t$FILE_PATH\t{1}\n".format(
                                                    k, os.path.join(path_rename, k)))
                        else:
                            if valj <= valm:
                                f.writelines("\tCreate step\t3\tREF_PROCSTEP\t{0}\t\t\t\n".format(nodes_name[valm]))
                                if nodes_name[valm] in last_step.keys():
                                    used.append(nodes_name[valm])
                                    a = last_step.get(nodes_name[valm])
                                    for k in a:
                                        if k != "*":
                                            f.writelines(
                                                " \t\t4\tKWOBJ\t{0}\tsmd_doctype\tZSB_0009\t\n \t\t\t\t\tsmd_state\t0IN_PROGRESS\n \t\t\t\t\tsmd_responsible\tname\n \t\t\t\t\t$FILE_PATH\t{1}\n".format(
                                                    k, os.path.join(path_rename, k)))
            else:
                if val <= valj:
                    f.writelines("\tCreate process\t2\tPROC\t{0}\t\t\t\n".format(nodes_name[valj]))
                    if nodes_name[valj] in last_step.keys():
                        used.append(nodes_name[valj])
                        a = last_step.get(nodes_name[valj])
                        for k in a:
                            if k != "*":
                                f.writelines(
                                    " \t\t3\tKWOBJ\t{0}\tsmd_doctype\tZSB_0009\t\n \t\t\t\t\tsmd_state\t0IN_PROGRESS\n \t\t\t\t\tsmd_responsible\tname\n \t\t\t\t\t$FILE_PATH\t{1}\n".format(
                                        k, os.path.join(path_rename, k)))
                    for m, valm in enumerate(steps):
                        if j != len(steps) - 1:
                            if valj <= valm < process[j + 1]:
                                f.writelines("\tCreate step\t3\tREF_PROCSTEP\t{0}\t\t\t\n".format(nodes_name[valm]))
                                if nodes_name[valm] in last_step.keys():
                                    used.append(nodes_name[valm])
                                    a = last_step.get(nodes_name[valm])
                                    for k in a:
                                        if k != "*":
                                            f.writelines(
                                                " \t\t4\tKWOBJ\t{0}\tsmd_doctype\tZSB_0009\t\n \t\t\t\t\tsmd_state\t0IN_PROGRESS\n \t\t\t\t\tsmd_responsible\tname\n \t\t\t\t\t$FILE_PATH\t{1}\n".format(
                                                    k, os.path.join(path_rename, k)))
                        else:
                            if valj <= valm:
                                f.writelines("\tCreate step\t3\tREF_PROCSTEP\t{0}\t\t\t\n".format(nodes_name[valm]))
                                if nodes_name[valm] in last_step.keys():
                                    used.append(nodes_name[valm])
                                    a = last_step.get(nodes_name[valm])
                                    for k in a:
                                        if k != "*":
                                            f.writelines(
                                                " \t\t4\tKWOBJ\t{0}\tsmd_doctype\tZSB_0009\t\n \t\t\t\t\tsmd_state\t0IN_PROGRESS\n \t\t\t\t\tsmd_responsible\tname\n \t\t\t\t\t$FILE_PATH\t{1}\n".format(
                                                    k, os.path.join(path_rename, k)))

    for n in list(set.difference(set(last_step) - set(used))):
        a = last_step.get(n)
        for k in a:
            if k != "*":
                f.writelines(
                    " \t\t1\tKWOBJ\t{0}\tsmd_doctype\tZSB_0009\t\n \t\t\t\t\tsmd_state\t0IN_PROGRESS\n \t\t\t\t\tsmd_responsible\tname\n \t\t\t\t\t$FILE_PATH\t{1}\n".format(
                        k, os.path.join(path_rename, k)))
print("pass")
