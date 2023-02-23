from knockpy import knockpy


def sort_subdomain(hostname):
    parts = hostname.split('.')[::-1]
    if parts[-1] == 'www':
        return parts[:-1], 1
    return parts, 0


def read_file(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def write_file(file, content):
    f = open(file, 'w')
    f.write(''.join(content))
    f.flush()
    f.close()


def append_file(file, content):
    f = open(file, 'a')
    f.write('\n'.join(content))
    f.write('\n')
    f.flush()
    f.close()

def scan_subdomains(hostname):
    try:
        print('Scanning for subdomains ...')
        results = knockpy.Scanning.start(hostname)
        domains = []
        for subdomain in results:
            domains.append(str('0.0.0.0 ' + subdomain))

        print('Found ' + str(len(domains)) + ' subdomains ...')
        return domains
    except ImportError:
        return []
