"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def register(self, formInfo):
        errors = []

        # form information
        name = formInfo['name']
        alias = formInfo['alias']
        email = formInfo['email']
        password = formInfo['password']
        conf_password = formInfo['conf_password']
        dob = formInfo['dob']

        if not name:
            errors.append('Name cannot be blank')
        elif len(name) < 2:
            errors.append('Name must be longer than 2 characters')
        if not alias :
            errors.append("Alias cannot be blank")
        elif len(alias) < 2:
            errors.append('Alias must be longer than 2 characters')
        if not email:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(email):
            errors.append('Email must be in email format')
        if not password:
            errors.append('Password cannot be blank')
        elif len(password) < 8:
            errors.append('Password must be longer than 8 characters')
        if not password == conf_password:
            errors.append('Passwords must match')

        if errors:
            return {"status": False, "errors": errors}
        else:
            # generate password hash to be stored using bcrypt
            ps_hash = self.bcrypt.generate_password_hash(password)

            register_query = "INSERT INTO user (name, alias, email, password, dob, created_at) VALUES (:name, :alias, :email, :password, :dob, NOW())"
            register_data = {'name': name, 'alias': alias, 'email': email, 'password': ps_hash, 'dob': dob}

            newUserId = self.db.query_db(register_query,register_data)

            get_new_user_query = "SELECT * FROM user WHERE id = :id"
            get_new_user_data = {'id': newUserId}

            newUser = self.db.query_db(get_new_user_query,get_new_user_data)

            return {"status": True, "newUser": newUser[0]}


    def login(self, formInfo):

        errors = []

        email = formInfo['email']
        password = formInfo['password']

        if not email:
            errors.append('Email must be provided')
        elif not EMAIL_REGEX.match(email):
            errors.append('Please enter a valid email format')
        if not password:
            errors.append('A password must be entered')

        if errors:
            return {"status": False, "errors": errors}
        else:

            get_user_query = "SELECT * FROM user WHERE email = :email LIMIT 1"
            get_user_data = {'email': email}

            user = self.db.query_db(get_user_query,get_user_data)

            if user:
                if self.bcrypt.check_password_hash(user[0]['password'], password):
                    return {"status": True, "userMatch": user[0]}
                else:
                    errors.append('Incorrect password')
                    return {"status": False, "errors": errors}
            else:
                errors.append('No user found under email: ' + email)
                return {"status": False, "errors": errors}
