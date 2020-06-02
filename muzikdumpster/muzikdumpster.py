import os

from argparse import ArgumentParser

from albums import Albums
from archive import Archive


def arg_parser():
    argparser = ArgumentParser()
    argparser.add_argument('-f', '--files', required=True, help='a music collection file or directory of music collection files')
    argparser.add_argument('-a', '--archive', action='store_true', help='store music collection as a file')
    args = argparser.parse_args()
    return args

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
    args = arg_parser()
    dir_path, files = get_filepaths(args.files)
    if len(files) == 0:
        print("no file to process")
        exit(0)
    albums = Albums(files)
    collection = albums.build_collection()
    for album in collection:
        print(album)
    if args.archive == True:
        arc = Archive(collection, dir_path)
        arc.generate()

if __name__ == '__main__':
    main()
