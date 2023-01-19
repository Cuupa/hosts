from os import walk
import os.path

hostfile = 'hosts'

files = []
for (dirpath, dirnames, filenames) in walk('data'):
    for file in filenames:
        path = os.path.join(dirpath, file)
        files.append(path)
    break

number_of_entries = 0

for file in files:
    with open(file) as current_file:
        for line in current_file:
            if '#' in line:
                continue
            if line.strip():
                number_of_entries += 1

host = open(hostfile, 'w')
host.write('# Title: Currated List by Cuupa\n')
host.write('# Number of entries: ' + str(number_of_entries) + '\n')

for file in files:
    host.write('\n')
    with open(file) as current_file:
        for line in current_file:
            host.write(line.rstrip())
            host.write('\n')
host.close()
