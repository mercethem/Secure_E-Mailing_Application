from hashlib import sha256


def Hashing(input):  # hashleme işlemi sha256 ile
    return sha256(input.encode('utf-8')).hexdigest()
