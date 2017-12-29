import datetime

import os

from fileobj import FileObj


class Result(object):
    """
    Output a list of results.
    """

    def __init__(self, entries):
        self.entries = entries

    def print(self):
        """
        Print results to the console.
        """
        print('[Info] printing result entries...\n')

        for entry in self.entries:
            print(entry.raw)

        print('\n')
        print('[Info] printing result entries complete')

    def archive(self, location, archive_type):
        """
        Store the results in a text file.
        """
        print('[Info] archive results...')

        now = datetime.datetime.now()
        filename = "muzik-dumpster-archive-{}-{}{}{}:{}{}{}.txt".format(
            archive_type,
            now.year,
            now.month,
            now.day,
            now.hour,
            now.minute,
            now.second)

        archive_location = os.path.join(location, filename)

        print("[Info] archiving results to: {}".format(archive_location))

        f = FileObj(archive_location, 'w+')
        for entry in self.entries:
            f.file.write(entry.raw + "\n")
        # f.close()

        print('[Info] archiving results complete')
