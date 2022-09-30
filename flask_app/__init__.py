#pipenv install flask pymysql
#importar flask
from flask import Flask

#inicializar app

app = Flask(__name__)

#declarar llave secreta
app.secret_key = "Esta es mi llave secreta"
