import argparse
from knockpy import knockpy


def scan_subdomains(hostname):
    print('Scanning for subdomains ...')
    results = knockpy.Scanning.start(hostname)
    domains = []
    for subdomain in results:
        domains.append(str(subdomain))

    print('Found ' + str(len(domains)) + ' subdomains ...')
    return domains


def save(output_file, domains):
    file = open(output_file, 'a')
    file.write('\n'.join(domains))
    file.flush()
    file.close()


def sort_subdomain(hostname):
    parts = hostname.split('.')[::-1]
    if parts[-1] == 'www':
        return parts[:-1], 1
    return parts, 0



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Adds a domain and any found subdomains"
    )

    parser.add_argument(
        "--subdomains",
        "-s",
        dest="subdomains",
        default=False,
        action="store_true",
        help="Include subdomains"
    )

    parser.add_argument(
        "--add-host",
        "-a",
        dest="host",
        help="Host to add"
    )

    parser.add_argument(
        "--output",
        "-o",
        dest="output",
        default="data/list",
        help="Output file"
    )

    options = vars(parser.parse_args())
    include_subdomains = options["subdomains"]
    host_to_add = options["host"]
    output_file = options["output"]

    print('Adding \'' + host_to_add + '\' to ' + '\'' + output_file + '\'')

    domains = []

    if include_subdomains:
        domains = scan_subdomains(host_to_add)

    domains.append(host_to_add)
    domains = sorted(domains, key = sort_subdomain)
    save(output_file, domains)
