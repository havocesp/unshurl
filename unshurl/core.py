# -*- coding:utf-8 -*-
import argparse
import sys
from typing import Iterable as Iter, SupportsInt as  Int

import requests


def main(urls) -> Int:
    """Main work is here.

    :param Iter urls: an iterable containing all URLs to be checked.
    :return: system return code
    """
    return_code = 0

    for url in urls:
        try:
            session = requests.Session()
            resp = session.head(url, allow_redirects=True)
            if resp.ok:
                print(f' * {url} -> {resp.url}')
            else:
                return_code = 1
                resp.raise_for_status()
        except (requests.ConnectionError, requests.ConnectTimeout):
            return_code = 1
            print(f' * {url} -> FAIL')
    return return_code


def run():
    parser = argparse.ArgumentParser(description='Short to long URL converter.')
    parser.add_argument('url', nargs='+', metavar='URL', help='URL to un-short.')
    args = parser.parse_args()
    # so connections are recycled
    sys.exit(main(args.url))
