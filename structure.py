import codecs
import os

# file = r"D:\...\BLUEPRINT\blue.dat"
path = input()
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

for i, val in enumerate(scenars):
    print("\tCreate a scenario\t1\tSCN\t{0}\t\t\t\n".format(nodes_name[val]))
    for j, valj in enumerate(process):
        if i != len(scenars) - 1:
            if val <= valj < scenars[i + 1]:
                print("\tCreate process\t2\tPROC\t{0}\t\t\t\n".format(nodes_name[valj]))
                for m, valm in enumerate(steps):
                    if j != len(steps) - 1:
                        if valj <= valm < process[j + 1]:
                            print("\tCreate step\t3\tREF_PROCSTEP\t{0}\t\t\t\n".format(nodes_name[valm]))
                    else:
                        if valj <= valm:
                            print("\tCreate step\t3\tREF_PROCSTEP\t{0}\t\t\t\n".format(nodes_name[valm]))
        else:
            if val <= valj:
                print("\tCreate process\t2\tPROC\t{0}\t\t\t\n".format(nodes_name[valj]))
                for m, valm in enumerate(steps):
                    if j != len(steps) - 1:
                        if valj <= valm < process[j + 1]:
                            print("\tCreate step\t3\tREF_PROCSTEP\t{0}\t\t\t\n".format(nodes_name[valm]))
                    else:
                        if valj <= valm:
                            print("\tCreate step\t3\tREF_PROCSTEP\t{0}\t\t\t\n".format(nodes_name[valm]))

print("pass")
