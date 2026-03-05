from collections import defaultdict

requests = defaultdict(int)

def check_rate_limit(ip):

    requests[ip] += 1

    if requests[ip] > 100:
        return False

    return True
