import argparse
import os
import sys
import util as util


def add_host(host_to_add, output_file, include_subdomains):
    print('Adding \'' + host_to_add + '\' to ' + '\'' + output_file + '\'')
    domains = []
    if include_subdomains:
        domains = util.scan_subdomains(host_to_add)
    domains.append('0.0.0.0 ' + host_to_add)
    domains = sorted(domains, key=util.sort_subdomain)
    util.append_file(output_file, domains)


def remove_host(host_to_remove, output_file, include_subdomains):
    print('Remove \'' + host_to_remove + '\' from ' + '\'' + output_file + '\'')

    content = []
    for line in util.read_file(output_file):
        if include_subdomains and host_to_remove in line:
            continue
        elif not include_subdomains and line.strip() and not line.startswith('#'):
            hostname = line.split('0.0.0.0 ')[1].strip()
            print('\'' + hostname + '\'')
            if host_to_remove == hostname:
                continue

        content.append(line)
    util.write_file(output_file, content)


def main():
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
        dest="add-host",
        help="Host to add"
    )

    parser.add_argument(
        "--remove-host",
        "-r",
        dest="remove-host",
        help="Host to remove"
    )

    parser.add_argument(
        "--output",
        "-o",
        dest="output",
        default="data/list",
        help="Output file"
    )

    parser.add_argument(
        "--list",
        "-l",
        dest="list",
        help="List of hosts to be added"
    )

    options = vars(parser.parse_args())
    include_subdomains = options["subdomains"]
    host_to_add = options["add-host"]
    host_to_remove = options["remove-host"]
    output_file = options["output"]


    if host_to_add:
        add_host(host_to_add, output_file, include_subdomains)

    elif host_to_remove:
        remove_host(host_to_remove, output_file, include_subdomains)


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print("\nInterrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
