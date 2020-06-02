from operator import attrgetter
from fileobj import FileObj


class Album(object):
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


class Albums(object):
    """
    A music library loaded from a text file.
    """

    def __init__(self, files):
        self.files = files

    def build_collection(self):
        """
        Process the list of files

        :return: an array of sorted albums
        """
        albums = []

        for filename in self.files:

            print("[Info] loading library: {0}".format(filename))

            file_object = FileObj(filename, 'r+')
            lines = file_object.file.readlines()

            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    albums.append(self._build_album(line))

        albums = sorted(albums, key=attrgetter('artist', 'year'))

        return self._extract_raw(albums)

    def _build_album(self, line):
        line = line.strip()
        tokens = line.split("|")
        if len(tokens) < 3:
            raise Exception("invalid number of tokens: {0}, line: {1}".format(len(tokens), line))
        album = Album(tokens[0].strip(),
                      tokens[1].strip(),
                      tokens[2].strip(),
                      line)
        return album

    def _extract_raw(self, albums):
        raw = []
        for album in albums:
            raw.append(album.raw)
        return raw
