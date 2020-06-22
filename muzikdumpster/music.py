from operator import itemgetter


class Music(object):
    """
    A music collection of albums loaded from one or more text files.
    """
    def __init__(self, files):
        self.files = files

    def generate(self):
        """
        Process each line of each file and build a new sorted list of music.

        Each file contains a list of music where each line represents a physical album with the following format:
        artist | album | year | format

        :return: a list of music sorted by artist and year
        """
        if len(self.files) == 0:
            raise Exception('no files to process')
        music = []
        for filename in self.files:
            music.extend(self._process_file(filename))
        return self._extract_raw(sorted(music, key=lambda tup: (tup[0], tup[2])))

    def _process_file(self, filename):
        print(f"[debug] processing file, filename: {filename}")
        with open(filename, 'r+') as f:
            lines = f.readlines()
        artists = []
        for line in lines:
            line = line.strip()
            if len(line) > 0:
                artists.append(self._store_artist(line))
        return artists

    def _store_artist(self, line):
        line = line.strip()
        tokens = line.split("|")
        if len(tokens) < 3:
            raise Exception(f"invalid number of tokens: {len(tokens)}, line: {line}")
        return (tokens[0].strip(), tokens[2].strip(), line)

    def _extract_raw(self, artists):
        raw = []
        for artist in artists:
            raw.append(artist[2])
        return raw
