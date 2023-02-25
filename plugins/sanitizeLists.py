from os import walk
import os
import collections
import util as util


def start():
    files = collect_files()
    sanitize_list(files)


def sanitize_list(files):
    for file in files:
        lines = []
        original_lines = []
        with open(file) as current_file:
            original_lines = current_file.readlines()
            for line in original_lines:
                lines.append(line.replace('\t', ' '))

        util.write_file(file, lines)


def collect_files():
    files = []
    for (dirpath, dirnames, filenames) in walk('data'):
        for file in filenames:
            path = os.path.join(dirpath, file)
            files.append(path)
        break
    return files


if __name__ == '__main__':
    print('sanitizing files ...')
    start()
    print('done!')
