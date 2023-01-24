import subprocess
import sys


def start():
    subprocess.call([sys.executable, 'sortLists.py'])
    subprocess.call([sys.executable, 'combineLists.py'])


if __name__ == '__main__':
    start()
