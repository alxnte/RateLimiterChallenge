import time
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self, interval_ms, limit):
        self.interval_ms = interval_ms
        self.limit = limit
        self.client_requests = defaultdict(deque) 
        # Using a deque to leverage O(1) TC for edits and FIFO


    def is_allowed(self, client_ip, request_timestamp):
        current_time = time.time() * 1000  # Converting to ms

        # Removing stale entries
        while self.client_requests[client_ip] and self.client_requests[client_ip][0] <= current_time - self.interval_ms:
            self.client_requests[client_ip].popleft()

        if len(self.client_requests[client_ip]) < self.limit:
            self.client_requests[client_ip].append(request_timestamp)
            return True

        return False