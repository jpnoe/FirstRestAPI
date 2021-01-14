from flask import jsonify
from flask import Flask
from flask import request
from flask_cors import CORS
import string
import random

app = Flask(__name__)
CORS(app)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

def generate_ID():
   letters = string.ascii_lowercase
   numbers = string.digits
   ID1 = ''.join(random.choice(letters) for i in range(3))
   ID2 = ''.join(random.choice(numbers) for i in range(3))
   ID = ID1 + ID2
   return ID

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = generate_ID()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      resp.status_code = 201
      return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])

def get_user(id):
   if request.method == 'GET':
      if id :
         for user in users['users_list']:
            if user['id'] == id:
               return user
            return ({})
      return users
   elif request.method == 'DELETE':
      resp = jsonify(success=False)
      resp.status_code = 404;
      if id :
         found = 0;
         for i, user in enumerate(users['users_list']):
            if user['id'] == id:
               users['users_list'].pop(i);
               resp = jsonify(success=True)
               resp.status_code = 200
      return resp
