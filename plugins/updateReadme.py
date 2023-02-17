import os.path


def start():
    last_updated, number_of_entries = get_metadata()
    update_readme(last_updated, number_of_entries)


def update_readme(last_updated, number_of_entries):
    readme_template = ''.join(read_file('/../README_template.md'))
    content = readme_template.replace(
        '{last_updated}\n', last_updated
    ).replace(
        '{number_of_entries}\n', number_of_entries
    )
    write_file('/../README.md', content)


def get_metadata():
    lines = read_file('/../hosts')
    metadata = list(filter(lambda it: '#' in it, lines))

    last_updated_metadata = list(filter(
        lambda it: '# Last updated: ' in it, metadata))
    last_updated = get_data(last_updated_metadata)
    
    number_of_entries_medatada = list(filter(
        lambda it: '# Number of entries: ' in it, metadata))
    number_of_entries = get_data(number_of_entries_medatada)
    return last_updated, number_of_entries


def write_file(file, content):
    file = open(os.path.dirname(__file__) + file, 'w')
    file.write(content)
    file.close()


def read_file(file):
    file = open(os.path.dirname(__file__) + file, 'r')
    lines = file.readlines()
    file.close()
    return lines


def get_data(line):
    return ''.join(line).split(': ')[1]


if __name__ == '__main__':
    start()
