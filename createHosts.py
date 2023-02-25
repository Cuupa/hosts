import plugins.sortLists as sortLists
import plugins.combineLists as combineLists
import plugins.removeDuplicates as removeDuplicates
import plugins.updateReadme as updateReadme
import plugins.sanitizeLists as sanitizeLists

def start():
    sortLists.start()
    sanitizeLists.start()
    combineLists.start()
    removeDuplicates.start()
    updateReadme.start()


if __name__ == '__main__':
    start()
