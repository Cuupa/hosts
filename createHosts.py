import plugins.sortLists as sortLists
import plugins.combineLists as combineLists
import plugins.removeDuplicates as removeDuplicates
import plugins.updateReadme as updateReadme


def start():
    sortLists.start()
    combineLists.start()
    removeDuplicates.start()
    updateReadme.start()


if __name__ == '__main__':
    start()
