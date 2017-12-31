from argparse import ArgumentParser

import os

from library import Library
from result import Result


class MuzikDumpster(object):

    def run(self):
        cli = self._build_argparser()
        args = cli.parse_args()

        dir_path, files = self._get_filepaths(args.files)

        if len(files) == 0:
            print('[Info] no files to process. Exiting...')
            exit(0)

        print("[Info] processing {} files".format(len(files)))

        library = Library(files)
        entries = library.process_files()

        result = Result(entries)

        if args.debug is False:
            result.archive(dir_path, args.media_type)
        else:
            result.print()

    def _build_argparser(self):
        """
        Build a command line parser.
        """
        argparser = ArgumentParser()
        argparser.add_argument(
            '-f',
            '--files',
            required=True,
            help='a music collection file or directory of music collection files')
        argparser.add_argument(
            '-m',
            '--media-type',
            required=False,
            default='unknown_type',
            help='type of file(s) being processed')
        argparser.add_argument(
            '-d',
            '--debug',
            action='store_true',
            help='dump results to standard out')
        return argparser

    def _get_filepaths(self, path):
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


if __name__ == '__main__':
    muzik_dumpster = MuzikDumpster()
    muzik_dumpster.run()
