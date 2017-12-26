"""
core

A process script to read a file of album information and sort by band and release year
"""

from argparse import ArgumentParser

import os
from operator import attrgetter

from muzikdumpster.library import Library
from muzikdumpster.result import Result


def build_argparser():
    """
    Build a command line parser.
    """
    argparser = ArgumentParser()
    argparser.add_argument(
        '-f',
        '--files',
        required=True,
        help='a music file or directory of music files')
    argparser.add_argument(
        '-a',
        '--archive',
        action='store_true',
        help='create file of results')
    argparser.add_argument(
        '-t',
        '--archive-type',
        required=False,
        default='unknown_type',
        help='type of file(s) being processed')
    return argparser


def get_filepaths(path):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []
    if os.path.isfile(path):
        file_paths.append(path)
        dir_path = os.path.dirname(path)
    else:
        for root, _, files in os.walk(path):
            if root == path:  # process only file in path (no sub-dirs)
                for filename in files:
                    if filename.startswith(".") is False:
                        filepath = os.path.join(root, filename)
                        file_paths.append(filepath)  # Add it to the list.
        dir_path = path
    return dir_path, file_paths


def main():
    """
    The core entry point.
    """

    cli = build_argparser()
    args = cli.parse_args()

    dir_path, files = get_filepaths(args.files)

    if len(files) == 0:
        print('[Info] no files to process. Exiting...')
        exit(0)

    print("[Info] processing {} files".format(len(files)))

    library = Library(files)
    entries = library.load()
    entries = sorted(entries, key=attrgetter('artist', 'year'))

    result = Result(entries)
    if args.archive is False:
        result.print()
    else:
        result.archive(dir_path, args.archive_type)


if __name__ == '__main__':
    main()
