# modules to make this work, flask for api end point, dbhelpers for connection, json for data in json
from flask import Flask, request
import dbhelpers as dh
import json

app = Flask(__name__)

@app.get('/api/inventory')
# return id, name, description, stock, created_at
def inventory_list():
    result = dh.run_statement('CALL inventory_list()')
    if(type(result) == list):
        inventory_json = json.dumps(result, default=str)
        return inventory_json
    else:
        print('error, error, error ')

# needs 3 argument(name, description, quantity) to add new item to db and returns the item's id as json
@app.post('/api/add_new_item')

def add_new_item():
    result = dh.run_statement('CALL add_new_item()')
    name_input = request.args.get('name')
    description_input = request.args.get('description')
    stock_input = request.args.get('stock')
    if(type(result) == list):
        client_json = json.dumps(result, default=str)
        return client_json
    else:
        print('error, error, error ')



app.run(debug=True)