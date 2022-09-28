#MVC modelo vista controlador
#config -> mydatabaseconnection
#controllers -> server.py
#models -> clase de usuarios
#static -> css javascript img
#templates -> html
#__init__ -> para inicializar la aplicacion

#importacion de flask_app
from flask_app import app

#importacion de controladores(rutas de la aplicacion)
from flask_app.controllers import users_controller

#ejecutacion de la app

if __name__ =="__main__":
    app.run(debug=True)



