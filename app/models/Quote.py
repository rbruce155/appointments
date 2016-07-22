"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Quote(Model):
    def __init__(self):
        super(Quote, self).__init__()


    def allQuotes(self):
        # TOdo: this query needs to change so that i can get user id for favorites functionality
        query = "SELECT * FROM quote q JOIN user u WHERE q.user_id = u.id ORDER BY q.created_at DESC"
        return self.db.query_db(query)


    def createQuote(self, formInfo, curUsrID):
        errors=[]

        # form information
        author = formInfo['author']
        quote = formInfo['quote']

        # check if author is new or existing
        if len(author) < 3:
            errors.append("Author must be at least 3 characters")
        if len(quote) < 10:
            errors.append("Quote must be longer than 10 characters")

        if errors:
            return {"status": False, "errors": errors}

        else:
            query = "INSERT INTO quote (user_id, quote, author, created_at) VALUES (:user_id, :quote, :author, NOW())"
            data = {'user_id': curUsrID, 'quote': quote, 'author': author }
            self.db.query_db(query,data)

            return {"status": True}

    def getUsrQuotes(self, usrId):
        query = "SELECT u.name 'user_name', q.author 'quote_author', q.quote 'quote' from quote q JOIN user u where q.user_id = u.id and u.id = :usrId"
        data = {'usrId': usrId}
        return self.db.query_db(query,data)
