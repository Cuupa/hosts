
from os import walk
import os


def collect_files():
    files = []
    for (dirpath, dirnames, filenames) in walk('data'):
        for file in filenames:
            path = os.path.join(dirpath, file)
            files.append(path)
        break
    return files

def tld(name):
    var = name.split('.')[-2]
    if ' ' in var:
        var = var.split(' ')[1]
    print(var)
    return var

def start():
    files = collect_files()
    for file in files:
        buffer = ""
        sorted_content = []
        with open(file) as current_file:
            for line in current_file:
                if line.isspace() or line.startswith('#'):
                    buffer += line
                
                else:
                    sorted_content.append(line)
        
        buffer += ''.join(sorted(sorted_content, key=tld))
        f = open(file, 'w')
        f.write(buffer)
        f.close()


if __name__ == '__main__':
    start()
