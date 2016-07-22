"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Favorite(Model):
    def __init__(self):
        super(Favorite, self).__init__()

    # todo: change querry to send back quote id so i can remove from fav list
    # returns 3 latest reviews with book title and user name
    def allFavorites(self, curUsrID):
        query = "SELECT u.alias 'poster_alias', u.id 'poster_id', q.author 'quote_author', q.quote 'quote', f.id 'fav_id' from favorite f join user u, quote q WHERE u.id = f.user_id and f.quote_id = q.id and u.id = :curUsrID"
        data = {"curUsrID": curUsrID}
        return self.db.query_db(query,data)
