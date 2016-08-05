"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'Welcome'

routes['POST']['/register'] = 'Users#register'
routes['POST']['/login'] = 'Users#login'
routes['/logout'] = 'Users#logout'
routes['/appointments'] = 'Appointments#index'
routes['POST']['/newAppmt'] = 'Appointments#newAppmt'
routes['/deleteAppmt/<appmtId>'] = 'Appointments#deleteAppmt'
routes['/edit/<appmtId>'] = 'Appointments#editAppmt'
routes['POST']['/updateAppmt'] = 'Appointments#updateAppmt'
