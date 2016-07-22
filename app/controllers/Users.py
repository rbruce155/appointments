"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('User')
        self.db = self._app.db

        """

        This is an example of a controller method that will load a view for the client

        """

    def register(self):

        formInfo = {
            "name" : request.form['name'],
            "alias" : request.form['alias'],
            "email" : request.form['email'],
            "password" : request.form['password'],
            "conf_password" : request.form['conf_password'],
            "dob": request.form['dob']
        }

        register_status = self.models['User'].register(formInfo)

        if register_status['status'] == True:
            session['id'] = register_status['newUser']['id']
            session['alias'] = register_status['newUser']['alias']

            flash("Successfully registered!", 'success')
            return redirect('/quotes')

        else:
            for message in register_status['errors']:
                flash(message, 'regis_errors')

            return redirect('/')

    def login(self):

        formInfo = {
            "email" : request.form['email'],
            "password" : request.form['password']
        }

        login_status = self.models['User'].login(formInfo)

        if login_status['status'] == True:

            session['id'] = login_status['userMatch']['id']
            session['alias'] = login_status['userMatch']['alias']

            flash("Successfully loged in!", 'success')
            return redirect('/quotes')

        else:
            for message in login_status['errors']:
                flash(message, 'login_errors')

            return redirect('/')

    def logout(self):
        session.clear()
        return redirect('/')
