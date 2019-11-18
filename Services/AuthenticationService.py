# login request handling Harry
# sign abdel

from flask import current_app as app
from functools import wraps
from app import mongo
from Models.User import User

import hashlib


class AuthenticationService():

    def __init__(self):
        return

    def login_required(self, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            authenticated = True
            if(not authenticated):
                return "Please login first"
            else:
                return f(*args, **kwargs)  # PASSING TO NEXT
        return decorated_function

    """ 
    Return the user
    """

    def getUser(self, email):
        if not User.objects(email=email):
            return False
        # use objects.get to retreive one result
        return User.objects.get(email=email)

    def save(self, user):
        if self.getUser(user.email):
            return False
        else:
            user.password = self.saltPassword(user.password)
            user.save()
            return True

    """
     Takes a password and returns a hashed version of it
    """

    def saltPassword(self, password):

        yummyYummySalty = "dHw33Th"
        db_password = password+yummyYummySalty
        hasher = hashlib.sha256(db_password.encode())
        hashLevelOne = hasher.hexdigest()
        supaHasher = hashlib.sha256(hashLevelOne.encode())
        hashLevelTwo = supaHasher.hexdigest()

        return hashLevelTwo
