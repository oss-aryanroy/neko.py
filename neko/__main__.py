import sys
from typing import Tuple
import aiohttp
import argparse
import platform
import pkg_resources

import neko

def show_version() -> None:
    entries = []

    entries.append('- Python v{0.major}.{0.minor}.{0.micro}-{0.releaselevel}'.format(sys.version_info))
    version_info = neko.version
    entries.append('- neko.py v{0.major}.{0.minor}.{0.micro}-{0.release}'.format(version_info))
    if version_info.release != 'final':
        pkg = pkg_resources.get_distribution('neko.py')
        if pkg:
            entries.append(f'    - neko.py pkg_resources: v{pkg.version}')

    entries.append(f'- aiohttp v{aiohttp.__version__}')
    uname = platform.uname()
    entries.append('- system info: {0.system} {0.release} {0.version}'.format(uname))
    print('\n'.join(entries))


def parse_args() -> Tuple[argparse.ArgumentParser, argparse.Namespace]:
    parser = argparse.ArgumentParser(prog='neko', description='Tools for helping with neko.py')
    parser.add_argument('-v', '--version', action='store_true', help='shows the library version')
    return parser, parser.parse_args()

def main():
    _, args = parse_args()
    if args.version:
        show_version()

if __name__ == '__main__':
    main()
