from system.core.controller import *
import time

class Appointments(Controller):
    def __init__(self, action):
        super(Appointments, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('Appointment')
        self.db = self._app.db


    def index(self):

        # check to see if user is logged in and fail fast if not
        if not session.get('id'):
            flash("You must first login to look at that page.", 'fail')
            return redirect('/')
        else:

            all_usr_appmts = self.models['Appointment'].getUsrAppmts(session['id'])
            all_other_appmts = self.models['Appointment'].getOtherAppmts(session['id'])

            # get todays date
            dateStr = time.strftime("%B %d, %Y:")


            return self.load_view('appointments.html', dateStr=dateStr, all_usr_appmts=all_usr_appmts, all_other_appmts=all_other_appmts)


    def newAppmt(self):
        formInfo = {
                "appmt_date": request.form['appmt_date'],
                "appmt_time": request.form['appmt_time'],
                "tasks": request.form['tasks']
                }

        create_status = self.models['Appointment'].createAppmt(formInfo, session['id'])

        if create_status['status'] == True:

            flash("Successfully created new appointment", 'success')
            return redirect('/appointments')

        else:
            for message in create_status['errors']:
                flash(message, 'login_errors')

            return redirect('/appointments')

    def deleteAppmt(self, appmtId):
        self.models['Appointment'].deleteAppmt(appmtId)
        flash("Successfully removed appointment")
        return redirect('/appointments')

    def editAppmt(self, appmtId):
        appmt_info = self.models['Appointment'].appmtInfo(appmtId)
        return self.load_view('edit.html', appmt_info=appmt_info, appmtId=appmtId)

    def updateAppmt(self):
        formInfo = request.form

        update_status = self.models['Appointment'].updateAppmt(formInfo)

        if update_status['status'] == True:

            flash("Successfully upadated appointment", 'success')
            return redirect('/appointments')

        else:
            for message in update_status['errors']:
                flash(message, 'login_errors')

            return redirect('/appointments')
