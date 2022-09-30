
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #importamos flash para mandar mensajes de validación
import re #importando expresiones regulares
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:

    def __init__(self, data):
        #data = diccionario --> data = {"id":1, "first_name":"Elena", "last_name":"De Troya" etc etc}
        self.id = data['id']
        self.first_name = data['first_name'] 
        self.last_name = data['last_name'] 
        self.email = data['email'] 
        self.created_at = data['created_at'] 
        self.update_at = data['update_at']
        self.password = data['password']

    @classmethod
    def guardar(cls, formulario):
        #formulario={"first_name":"juana", "last_name":"De Arco" etc etc}
        query = "INSERT INTO users(first_name, last_name, email, password) VALUES( %(first_name)s , %(last_name)s, %(email)s, %(password)s )"
        result = connectToMySQL('esquema_usuarios').query_db(query, formulario)
        return result

    @classmethod
    def muestra_usuario(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('esquema_usuarios').query_db(query)
        #tengo un diccionario:
        #[
        # {"id":1,"first_name":"Juana", "last_name":"De Arco" etc etc etc}
        #luego recibo un segundo diccionario:
        # {"id":2,"first_name":"Elena", "last_name":"De Troya" etc etc etc}
        # ]
        #tengo que transformar los diccionarios en instancias de usuarios// recorriendo la lista y transformandolos en instancias de usuarios
        users = []
        for u in results: # en u voy a estar guardando mi diccionario
            user = cls(u) #user = User(u) -> {"id":1,"first_name":"Juana", "last_name":"De Arco" etc etc etc}
            users.append(user)
        return users

    @classmethod
    def borrar(cls, formulario):
        #formulario = {"id":"1"}
        query = "DELETE FROM users WHERE id = %(id)s" #interpolacion
        result = connectToMySQL('esquema_usuarios').query_db(query,formulario)
        return result


    @classmethod
    def mostrar(cls, formulario):
        #formulario= {"id":1}
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuarios').query_db(query,formulario)
        #result=[
        # {"id":1,"first_name":"Elena","last_name":"De Troya" etc etc}]
        diccionario = result[0] #diccionario = {"id":1,"first_name":"Elena","last_name":"De Troya" etc etc}]
        usuario= cls(diccionario) #usuario = User(diccionario)
        return usuario

    @classmethod
    def actualizar(cls, formulario): #recibiendo el formulario nuevo
        #formulario = {"id":1,"first_name":"Elena","last_name":"De Troya" etc etc}
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuarios').query_db(query, formulario)
        return result

    @staticmethod #(no tiene nada que ver con la clase ni la instancia (cls, self))
    def valida_usuario(formulario):
        is_valid = True #Asumimos que todo en el usuario está correcto
        if len(formulario['first_name']) < 3:
            flash('El nombre debe tener al menos 3 caracteres', 'registro')
            is_valid = False

        if len(formulario['last_name']) < 3:
            flash('El apellido debe tener al menos 3 caracteres', 'registro')
            is_valid = False

        if len(formulario['password']) < 6:
            flash('La contraseña debe tener al menos 6 caracteres', 'registro')
            is_valid = False

        #verificamos con expresiones regulares que el correo tenga el formato correcto
        if not EMAIL_REGEX.match(formulario['email']):
            flash('E-mail inválido', 'registro')
            is_valid = False

        #Consultar si ya existe ese correo electronico
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('esquema_usuarios').query_db(query, formulario)
        if len(result) >=1: #Si existe algun registro con ese correo:
            flash('El e-mail ya está registrado', 'registro')
            is_valid = False

        return is_valid