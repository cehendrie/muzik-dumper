import datetime
import os

from fileobj import FileObj


class Archive(object):
    def __init__(self, albums, location):
        self.albums = albums
        self.location = location

    def generate(self):
        archive_location = os.path.join(self.location, "muzik-dumpster-archive-{:%Y-%m-%d_%H:%M:%S}.txt".format(datetime.datetime.now()))
        f = FileObj(archive_location, 'w+')
        for album in self.albums:
            f.file.write(album + "\n")
