class ProjectCache:

    def __init__(self):

        self.files = {}

        self.symbols = {}

        self.summaries = {}

    def clear(self):

        self.files.clear()

        self.symbols.clear()

        self.summaries.clear()


project_cache = ProjectCache()