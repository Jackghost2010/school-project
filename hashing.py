import hashlib

def hashing_func(password):

    return hashlib.sha256(password.encode()).hexdigest()