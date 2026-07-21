class ProjectService:

    def __init__(self):
        self.current_project = None

    def open(self, name):
        self.current_project = name

    def current(self):
        return self.current_project

    def close(self):
        self.current_project = None

    def has_project(self):
        return self.current_project is not None