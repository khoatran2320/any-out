# login request handling Harry
# sign abdel

from flask import current_app as app

from app import mongo
from Models.User import User

import hashlib


class AuthenticationService():

    def __init__(self):
        return

    def getUser(self, email):
        if not User.objects(email=email):
            return False

        return User.objects.get(email=email)

    def save(self, user):
        if self.getUser(user.email):
            return False
        else:
            user.password = self.hashPassword(user.password)
            user.save()
            return True

    """
     Takes a password and returns a hashed version of it
    """

    def hashPassword(self, password):
        salt = "tyuhjhjklnm"
        saltedPassword = password + salt
        hasher = hashlib.sha256(saltedPassword.encode())
        hashedPassword = hasher.hexdigest()
        return hashedPassword
