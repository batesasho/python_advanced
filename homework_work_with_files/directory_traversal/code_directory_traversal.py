import os
from os.path import join

files_dic = {}

for root, dir, files in os.walk("."):
    for file in files:
        file_ext = "." + file.split(".")[1]
        file_name = file.split(".")[0]
        files_dic.setdefault(file_ext, [])
        files_dic[file_ext].append(file_name)

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
with open(join(desktop, 'report.txt'), "w") as file:
    for ext, name in sorted(files_dic.items(), key = lambda x: (x[0])):
        print(ext, sep = '\n', file = file)
        [print(names, file = file, sep = '\n') for names in sorted(name)]
