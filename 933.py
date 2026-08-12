class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        valid = []
        for i in self.requests:
            if i >= t-3000:
                valid.append(i)
        self.requests = valid
            return len(self.requests)