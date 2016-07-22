"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('Quote')
        self.load_model('Favorite')
        self.db = self._app.db


    def index(self):

        # check to see if user is logged in and fail fast if not
        if not session.get('id'):
            flash("You must first login to look at that page.", 'fail')
            return redirect('/')
        else:

            all_favs = self.models['Favorite'].allFavorites(session['id'])
            all_quotes = self.models['Quote'].allQuotes()

            return self.load_view('quotes.html', all_quotes=all_quotes, all_favs=all_favs)

    def newquote(self):
        formInfo = {
                "author": request.form['author'],
                "quote": request.form['quote']
                }

        create_status = self.models['Quote'].createQuote(formInfo, session['id'])

        if create_status['status'] == True:

            flash("Successfully created new quote", 'success')
            return redirect('/quotes')

        else:
            for message in create_status['errors']:
                flash(message, 'login_errors')

            return redirect('/quotes')

    def getUserQuotes(self, usrId):

        user_quotes = self.models['Quote'].getUsrQuotes(usrId)

        count = len(user_quotes)

        return self.load_view('showuser.html', user_quotes=user_quotes, count=count)
