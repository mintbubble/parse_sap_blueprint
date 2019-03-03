import os

path = input()
path_rename = os.path.join(path, "RENAME_FILE")
file = os.path.join(path_rename, "solar01_structure.txt")
scenario = {}  # scenario - business process
bus_step = {}  # business process - step
last_step = {}  # last step - document

with open(file, encoding='utf8') as f:
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
        if "Бизнес-сценарии" in i:
            a = len(p)
            m = int(p.index("Бизнес-сценарии")) + 2
            if int(len(p)) > int(p.index("Бизнес-сценарии")) + 2:
                if p[p.index("Бизнес-сценарии") + 1] not in scenario.keys():
                    scenario[p[p.index("Бизнес-сценарии") + 1]] = ["*"]
                if "Бизнес-процессы" in i:
                    if int(len(p)) > int(p.index("Бизнес-процессы")) + 2:

                        x = p.index("Бизнес-процессы") + 1
                        z = p[p.index("Бизнес-процессы") + 1]
                        y = scenario.get(p[p.index("Бизнес-сценарии") + 1])

                        if p[p.index("Бизнес-процессы") + 1] not in y:
                            y.append(p[p.index("Бизнес-процессы") + 1])
                            scenario[p[p.index("Бизнес-сценарии") + 1]] = y
                        if int(len(p)) > int((p.index(
                                "Бизнес-процессы") + 3)):  # if the list is longer than bp + name bp + document, then there is a step (bp + 2 - step)
                            if p[p.index("Бизнес-процессы") + 1] not in bus_step.keys():
                                bus_step[p[p.index("Бизнес-процессы") + 1]] = ["*"]
                            c = bus_step.get(p[p.index("Бизнес-процессы") + 1])
                            if p[p.index("Бизнес-процессы") + 2] not in c:
                                c.append(p[p.index("Бизнес-процессы") + 2])
                                bus_step[p[p.index("Бизнес-процессы") + 1]] = c
                    else:
                        bus_step["Бизнес-процессы"] = ["*"]
            else:
                if "Бизнес-сценарии" not in scenario.keys():
                    scenario["Бизнес-сценарии"] = ["*"]
        else:
            if p[0] not in scenario.keys():
                scenario[p[0]] = ["*"]

# make a pattern
with open(os.path.join(path_rename, "shablon.txt"), 'w', encoding='utf8') as f:
    f.truncate()
    for scen in scenario.keys():
        if scen == "":
            f.writelines("\tCreate a scenario\t1\tSCN\t{0}\t\t\t\n".format("NoName"))
        else:
            f.writelines("\tCreate a scenario\t1\tSCN\t{0}\t\t\t\n".format(scen))
        if scen in last_step.keys():
            a = last_step.get(scen)
            for i in a:
                if i != "*":
                    f.writelines(
                        "\t \t2\tKWOBJ\t{0}\tsmd_doctype\tZSB_0009\t\n\t\t\t\t\tsmd_state\t0IN_PROGRESS\n\t\t\t\t\t$FILE_PATH\t{1}\n".format(
                            i, os.path.join(path_rename, i)))
        for bp in scenario.get(scen):
            if bp != "*":
                f.writelines("\tCreate process\t2\tPROC\t{0}\t\t\t\n".format(bp))
            if bp in last_step.keys():
                a = last_step.get(bp)
                for i in a:
                    if i != "*":
                        f.writelines(
                            "\t \t3\tKWOBJ\t{0}\tsmd_doctype\tZSB_0009\t\n\t\t\t\t\tsmd_state\t0IN_PROGRESS\n\t\t\t\t\t$FILE_PATH\t{1}\n".format(
                                i, os.path.join(path_rename, i)))
            if bp in bus_step.keys():

                for step in bus_step.get(bp):
                    if step != "*":
                        f.writelines("\tCreate step\t3\tREF_PROCSTEP\t{0}\t\t\t\n".format(step))
                        if step in last_step.keys():
                            a = last_step.get(step)
                            for i in a:
                                if i != "*":
                                    f.writelines(
                                        "\t \t4\tKWOBJ\t{0}\tsmd_doctype\tZSB_0009\t\n\t\t\t\t\tsmd_state\t0IN_PROGRESS\n\t\t\t\t\t$FILE_PATH\t{1}\n".format(
                                            i, os.path.join(path_rename, i)))

print("pass")
