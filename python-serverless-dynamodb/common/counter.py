import uuid

class Counter:
    count: int = 0
    name: str = str(uuid.uuid4())


    def identify(self):
        return {
            "count": self.count,
            "name": self.name
        }


    def increment(self):
        self.count += 1
