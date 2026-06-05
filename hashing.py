try:
    from hashlib import sha256
    def hashing_func(password):
        return sha256(password.encode()).hexdigest()
except ImportError:
    print("something wrong with the modules")
