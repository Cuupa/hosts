from os import walk
import os.path
from datetime import datetime

hostfile = 'hosts'
hostfile_minified = 'hosts_minified'
hostfile_compressed = 'hosts_compressed'


def start():
    files = collect_files()
    global number_of_entries
    number_of_entries = count_entries(files)
    write(hostfile, files)
    write_minified(hostfile_minified, files)
    write_compressed(hostfile_compressed, files)


def collect_files():
    files = []
    for (dirpath, dirnames, filenames) in walk('data'):
        for file in filenames:
            path = os.path.join(dirpath, file)
            files.append(path)
        break
    return files


def write_compressed(hostfile, files):
    host = open(hostfile, 'w')
    lines_compressed = []
    for file in files:
        with open(file) as current_file:
            for line in current_file:
                if '#' in line or line.isspace():
                    continue

                sanitized_line = line.replace('\n', '')
                try:
                    sanitized_line = sanitized_line.split('0.0.0.0 ')[1]
                    lines_compressed.append(sanitized_line)
                except:
                    print("Failed to process " + sanitized_line)

                if len(lines_compressed) == 9:
                    host.write('0.0.0.0 ')
                    host.write(' '.join(lines_compressed).rstrip())
                    host.write('\n')
                    host.flush()
                    lines_compressed = []
    host.write('0.0.0.0 ')
    host.write(' '.join(lines_compressed).rstrip())
    host.write('\n')
    host.flush()
    host.close()

def write_minified(hostfile, files):
    host = open(hostfile, 'w')
    for file in files:
        with open(file) as current_file:
            for line in current_file:
                if '#' in line or line.isspace():
                    continue
                host.write(line.rstrip())
                host.write('\n')
    host.flush()
    host.close()


def write(hostfile, files):
    host = open(hostfile, 'w')
    host.write('# Title: Currated List by Cuupa\n')
    host.write('# Number of entries: ' + str(number_of_entries) + '\n')
    host.write('# Last updated: ' +
               datetime.now().strftime('%Y-%m-%d %H:%M:%S' + '\n'))

    for file in files:
        host.write('\n')
        with open(file) as current_file:
            for line in current_file:
                host.write(line.rstrip())
                host.write('\n')
    host.flush()
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
    print('combining lists ...')
    start()
    print('done!')
