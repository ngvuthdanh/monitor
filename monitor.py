import random

def listen_traffic():
    if random.random() < 0.2:
        return "192.168.666.200", "POST /login"
    else:
        return "192.168.1.100", "GET /"
