# -*- coding:utf-8 -*-
import argparse
import sys
from typing import Iterable as Iter

import requests

Int = int


def unshurl(url, raw=False):
    return_code = 0
    try:
        session = requests.Session()
        resp = session.head(url, allow_redirects=True)
        if resp.ok:
            print(resp.url if raw else f' * {url} -> {resp.url}')
        else:
            return_code = 1
            resp.raise_for_status()
    except (requests.ConnectionError, requests.ConnectTimeout):
        return_code = 1
        print(f' * {url} -> FAIL')
    except (requests.exceptions.InvalidURL, requests.exceptions.MissingSchema):
        return_code = 2
    return return_code


def shurl(url, raw=False):
    return_code = 0
    try:
        session = requests.Session()
        url = f'https://is.gd/create.php?format=simple&url={url}'
        resp = session.get(url, allow_redirects=True)
        if resp.ok:
            print(resp.text if raw else f' * {url} -> {resp.text}')
        else:
            return_code = 1
            resp.raise_for_status()
    except (requests.ConnectionError, requests.ConnectTimeout):
        return_code = 1
        print(f' * {url} -> FAIL')
    except (requests.exceptions.InvalidURL, requests.exceptions.MissingSchema):
        return_code = 2
    return return_code


def main(urls: Iter[str], raw=False, short_url=False) -> Int:
    """Main work is here.

    :param short_url: if set, supplied URL will be shorted.
    :param Iter urls: an iterable containing all URLs to be checked.
    :param bool raw: if set, just the un-shorted URL will be shown.
    """

    return_code = 0

    for url in urls:
        if short_url:
            shurl(url, raw)
        else:
            unshurl(url, raw)
    return return_code


def run():
    parser = argparse.ArgumentParser(description='URL shortener or un-shortener.')
    parser.add_argument('url', nargs='+', metavar='URL', help='URL to short or un-short.')
    parser.add_argument(
        '-s',
        '--short',
        default=False,
        action='store_true',
        help='Short the supplied URL instead of un-short (default).'
    )
    parser.add_argument('-r', '--raw', action='store_true', help='Only output long URL.')
    args = parser.parse_args()
    # so connections are recycled
    sys.exit(main(args.url, raw=args.raw))
