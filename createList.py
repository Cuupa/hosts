from os import walk
import os.path

hostfile = 'hosts'
hostfile_compressed = 'hosts_compressed'


def start():
    files = collect_files()
    global number_of_entries
    number_of_entries = count_entries(files)
    write(hostfile, files)
    write(hostfile_compressed, files, True)


def collect_files():
    files = []
    for (dirpath, dirnames, filenames) in walk('data'):
        for file in filenames:
            path = os.path.join(dirpath, file)
            files.append(path)
        break
    return files


def write(hostfile, files, compressed=False):
    host = open(hostfile, 'w')

    if not compressed:
        host.write('# Title: Currated List by Cuupa\n')
        host.write('# Number of entries: ' + str(number_of_entries) + '\n')

    for file in files:
        if not compressed:
            host.write('\n')
        with open(file) as current_file:
            for line in current_file:
                if compressed:
                    if '#' in line or line.isspace():
                        continue
                host.write(line.rstrip())
                host.write('\n')
    host.close()


def count_entries(files):
    noe = 0
    for file in files:
        with open(file) as current_file:
            for line in current_file:
                if '#' in line:
                    continue
                if line.strip():
                    noe += 1
    return noe


if __name__ == '__main__':
    start()
