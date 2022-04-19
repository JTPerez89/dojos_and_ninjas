from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name,  age, created_at, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM ninjas WHERE id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, {'id':data})

    @classmethod
    def select(cls, data):
        query = 'SELECT * FROM ninjas WHERE id = %(id)s'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, {'id':data})

    @classmethod
    def select_last(cls):
        query = 'select * FROM ninjas ORDER BY id DESC LIMIT 1;'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query)
    
    @classmethod
    def update(cls, data):
        query = 'UPDATE ninjas SET name = %(first_name)s, updated_at = NOW() WHERE id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)