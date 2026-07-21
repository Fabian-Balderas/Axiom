import json
from pathlib import Path


class MemoryService:
    """
    Persistent memory storage.
    """

    def __init__(self):
        self.memory_file = Path("axiom/memory/memory.json")
        self.memories = {}

        self.load()

    def load(self):
        if self.memory_file.exists():
            with open(self.memory_file, "r") as file:
                self.memories = json.load(file)

    def save(self):
        with open(self.memory_file, "w") as file:
            json.dump(self.memories, file, indent=4)

    def remember(self, key, value):
        self.memories[key] = value
        self.save()

    def recall(self, key):
        return self.memories.get(key)

    def list(self):
        return self.memories

    def forget(self, key):
        if key in self.memories:
            del self.memories[key]
            self.save()
            return True

        return False