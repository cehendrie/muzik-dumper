"""
library.py
"""

class FileObject(object):
    """
    A simple file object that cleans up after itself.
    """

    def __init__(self, filename):
        # open a file filename in filepath in read and write mode
        self.file = open(filename, 'r+')

    def __del__(self):
        self.file.close()
        del self.file

class Entry(object):
    """
    A container to hold one music library entry.
    """

    def __init__(self, artist, album, year, raw):

        self.artist = artist
        self.album = album
        self.year = year
        self.raw = raw

    def __str__(self):
        return "Entry [artist: {0}, album: {1}, year: {2}]".format(
            self.artist,
            self.album,
            self.year)


class Library(object):
    """
    A music library loaed from a text file.
    """

    def __init__(self, files):
        self.files = files

    def load(self):
        """
        Parse a list of files representing a music library.
        """

        entries = []

        for filename in self.files:
            print("[Info] loading libary: {0}".format(filename))
            file_object = FileObject(filename)
            lines = file_object.file.readlines()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    entries.append(self._build_entry(line))

        return entries

    def _build_entry(self, line):
        line = line.strip()
        tokens = line.split("|")
        if len(tokens) < 3:
            raise Exception("invalid number of tokens: {0}, line: {1}".format(len(tokens), line))
        entry = Entry(tokens[0].strip(),
                      tokens[1].strip(),
                      tokens[2].strip(),
                      line)
        return entry
        