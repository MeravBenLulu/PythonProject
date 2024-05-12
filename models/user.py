from PythonProject.app import mongo

class User:
    def create_user(self, user_data):
        users = mongo.db.users
        user_id = users.insert_one(user_data).inserted_id
        return user_id

    def get_user(self, user_id):
        users = mongo.db.users
        user = users.find_one({'_id': user_id})
        return user
