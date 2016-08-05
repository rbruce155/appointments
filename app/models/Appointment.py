from system.core.model import Model
import time

class Appointment(Model):
    def __init__(self):
        super(Appointment, self).__init__()

    def createAppmt(self, formInfo, curUsrID):
        errors=[]

        # form information
        appmt_date = formInfo['appmt_date']
        appmt_time = formInfo['appmt_time']
        tasks = formInfo['tasks']

        # form validations
        if not appmt_date:
            errors.append("Date must have a value")
        if not appmt_time:
            errors.append("Time must have a value")
        if not tasks:
            errors.append("Tasks must have a value")
        if appmt_date < time.strftime("%Y-%m-%d"):
            errors.append("You cannot create an appointment for a past date")


        if errors:
            return {"status": False, "errors": errors}

        else:
            query = "INSERT INTO appointment (user_id, tasks, appmt_date, appmt_time) VALUES (:user_id, :tasks, :appmt_date, :appmt_time)"
            data = {'user_id': curUsrID, 'tasks': tasks, 'appmt_date': appmt_date, 'appmt_time': appmt_time }
            self.db.query_db(query,data)

            return {"status": True}


    def getUsrAppmts(self, usrId):
        today = time.strftime("%Y-%m-%d")
        query = "SELECT * FROM appointment WHERE user_id = :usrId and appmt_date = :today ORDER BY appmt_time DESC"
        data = {'usrId': usrId, 'today': today}
        return self.db.query_db(query,data)

    def getOtherAppmts(self, usrId):
        today = time.strftime("%Y-%m-%d")
        query = "SELECT * FROM appointment WHERE user_id = :usrId and appmt_date > :today"
        data = {'usrId': usrId, 'today': today}
        return self.db.query_db(query,data)

    def deleteAppmt(self, appmtId):
        query = "DELETE from appointment WHERE id = :appmtId"
        data = {'appmtId': appmtId}
        return self.db.query_db(query,data)

    def appmtInfo(self, appmtId):
        query = "SELECT * from appointment WHERE id = :appmtId"
        data = {'appmtId': appmtId}
        return self.db.query_db(query,data)

    def updateAppmt(self, formInfo):
        errors=[]
        appmtId = formInfo['appmtId']
        tasks = formInfo['tasks']
        status = formInfo['status']
        appmt_date = formInfo['appmt_date']
        appmt_time = formInfo['appmt_time']

        # form validations
        if not appmt_date:
            errors.append("Date must have a value")
        if not appmt_time:
            errors.append("Time must have a value")
        if not tasks:
            errors.append("Tasks must have a value")
        if appmt_date < time.strftime("%Y-%m-%d"):
            errors.append("You cannot create an appointment for a past date")


        if errors:
            return {"status": False, "errors": errors}

        else:
            query = "UPDATE appointment SET tasks=:tasks, status=:status, appmt_date=:appmt_date, appmt_time=:appmt_time WHERE id = :appmtId"
            data = {'appmtId': appmtId, 'tasks': tasks, 'status': status, 'appmt_date': appmt_date, 'appmt_time': appmt_time }
            self.db.query_db(query,data)

            return {"status": True}
