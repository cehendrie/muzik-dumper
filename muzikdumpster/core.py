"""
core

A process script to read a file of album information and sort by band and release year
"""

import os
import datetime
from operator import attrgetter
from argparse import ArgumentParser
from library import Library


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
    else:
        for root, _, files in os.walk(path):
            if (root == path):  # process only file in path (no sub-dirs)
                for filename in files:
                    if filename.startswith(".") is False:
                        filepath = os.path.join(root, filename)
                        file_paths.append(filepath)  # Add it to the list.
    return file_paths

def print_results(entries):
    print("[Info] printing results...")
    print('\n')
    for entry in entries:
        print(entry.raw)
    print('\n')
    print('[Info] printing results complete')

def archive_results(entries):
    now = datetime.datetime.now()
    filename = "muzik-dumpster-archive-{}{}{}:{}{}{}.txt".format(
        now.year, 
        now.month, 
        now.day, 
        now.hour, 
        now.minute, 
        now.second)
    print("[Info] archiving results to: {}".format(filename))
    f = open(filename, "w+")
    for entry in entries:
        f.write(entry.raw + "\n")
    f.close()
    print('[Info] archiving results complete')

def main():
    """
    The core entry point.
    """
    
    cli = build_argparser()
    args = cli.parse_args()

    files = get_filepaths(args.files)

    library = Library(files)
    entries = library.load()
    entries = sorted(entries, key=attrgetter('artist', 'year'))

    if args.archive is False:
        print_results(entries)
    else:
        archive_results(entries)

if __name__ == '__main__':
    main()
