
from flask_app.config.mysqlconnection import connectToMySQL

class User:

    def __init__(self, data):
        #data = diccionario --> data = {"id":1, "first_name":"Elena", "last_name":"De Troya" etc etc}
        self.id = data['id']
        self.first_name = data['first_name'] 
        self.last_name = data['last_name'] 
        self.email = data['email'] 
        self.created_at = data['created_at'] 
        self.update_at = data['update_at'] 

    @classmethod
    def guardar(cls, formulario):
        #formulario={"first_name":"juana", "last_name":"De Arco" etc etc}
        query = "INSERT INTO users(first_name, last_name, email) VALUES( %(first_name)s , %(last_name)s, %(email)s )"
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



