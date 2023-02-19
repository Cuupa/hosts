from os import walk
import os
import collections
import util as util


def start():
    files = collect_files()
    remove_duplicates(files)


def remove_duplicates(files):
    for file in files:
        lines = []
        original_lines = []
        with open(file) as current_file:
            original_lines = current_file.readlines()
            lines = list(dict.fromkeys(original_lines))

        util.write_file(file, lines)

        if len(lines) == len(original_lines):
            print('No duplicates in ' + str(file))
        else:
            print('Found duplicates in ' + str(file))
            removed = [item for item, count in collections.Counter(
                original_lines).items() if count > 1]
            print(''.join(removed))


def collect_files():
    files = []
    for (dirpath, dirnames, filenames) in walk('data'):
        for file in filenames:
            path = os.path.join(dirpath, file)
            files.append(path)
        break
    return files


if __name__ == '__main__':
    print('removing duplicates ...')
    start()
    print('done!')
