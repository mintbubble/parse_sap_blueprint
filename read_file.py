import os
import codecs
import shutil

name_file = {}
id_file = {}
path = input()
file = os.path.join(path, "blue.dat")  # blue.dat file from input path

obj_file = [sChild for sChild in os.listdir(path)]

with codecs.open(file, "r", "utf_16_le") as f:
    file_lines = [str(line.replace('\n', "")) for line in f]

result = list(set(obj_file) & set(file_lines))

# dictionary of file names and their nodes
for n in result:
    name_file[n] = file_lines[file_lines.index(n) + 5].strip()
    id_file[n] = file_lines[file_lines.index(n) - 3]

# kill special characters ["\\","/",":","*","?","\"","<",">","|"]
match = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]
for n in result:
    for i in match:
        name_file[n] = name_file[n].replace(i, "")

# create a folder RENAME_FILE
path_rename = os.path.join(path, "RENAME_FILE")
if not os.path.exists(path_rename):
    os.makedirs(path_rename)

# copy and rename files
for n in result:
    shutil.copyfile(os.path.join(path, n), os.path.join(path_rename, str(name_file[n] + "." + n.split('.')[1])))

# file with structure
format = '0000000000'
with open(os.path.join(path_rename, "solar01_structure.txt"), 'w', encoding='utf8') as f:
    f.truncate()
    for n in result:
        p = []
        path_solar = ""
        used_type = []
        for i in reversed(range(1, int(id_file[n]) + 1)):
            node = format[:-len(str(i))] + str(i)
            if node in file_lines:
                if int(file_lines[file_lines.index(node) + 2]) <= int(file_lines[file_lines.index(id_file[n]) + 2]) and \
                        file_lines[file_lines.index(node) + 2] not in used_type:
                    p.append(file_lines[file_lines.index(node) + 4])
                    used_type.append(file_lines[file_lines.index(node) + 2])
        path_solar = "\\".join(reversed(p))
        f.writelines(path_solar + "\\" + name_file[n] + "." + n.split('.')[1] + "\n")

print("pass")
