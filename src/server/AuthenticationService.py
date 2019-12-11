from flask import current_app as app
from app import mongo


import hashlib


def hashPassword(password):
    salt = "tyuhjhjklnm"
    saltedPassword = password + salt
    hasher = hashlib.sha256(saltedPassword.encode())
    hashedPassword = hasher.hexdigest()
    return hashedPassword
