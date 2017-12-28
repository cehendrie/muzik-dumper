class FileObj(object):

    def __init__(self, filepath, attribute):
        self.file = open(filepath, attribute)

    def __del__(self):
        self.file.close()
        del self.file
