from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM dojos WHERE id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, {'id':data})

    @classmethod
    def select(cls, data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, {'id':data})

    @classmethod
    def select_last(cls):
        query = 'select * FROM dojos ORDER BY id DESC LIMIT 1;'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query)
    
    @classmethod
    def update(cls, data):
        query = 'UPDATE dojos SET name = %(first_name)s, updated_at = NOW() WHERE id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db( query , {'id':data} )
        dojos = cls( results[0] )
        for dojo in results:
            ninja_data = {
                'id' : dojo['id'],
                'first_name' : dojo['first_name'],
                'last_name' : dojo['last_name'],
                'age' : dojo['age'],
                'created_at' : dojo['created_at'],
                'updated_at' : dojo['updated_at'],
                'dojo_id' : dojo['dojo_id']
            }
            dojos.ninjas.append(ninja.Ninja(ninja_data))
        return dojos