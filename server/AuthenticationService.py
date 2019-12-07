# login request handling Harry
# sign abdel

from flask import current_app as app
from app import mongo


import hashlib



def hashPassword(self, password):
    salt = "tyuhjhjklnm"
    saltedPassword = password + salt
    hasher = hashlib.sha256(saltedPassword.encode())
    hashedPassword = hasher.hexdigest()
    return hashedPassword
