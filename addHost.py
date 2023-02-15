import argparse
import subprocess
import sys

sublist3r_path = "C:\Python311\Lib\site-packages\sublist3r.py"
cmd = "-d{host}"

def scan_subdomains(hostname):
    subprocess.call([sys.executable, sublist3r_path, cmd.format(host=hostname), "-o", "temp", "-b", "-v"])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Adds a domain and any found subdomains"
    )

    parser.add_argument(
        "--subdomains",
        "-s",
        dest="subdomains",
        default=False,
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

    if include_subdomains:
        print("include subdomains")
        scan_subdomains(host_to_add)
