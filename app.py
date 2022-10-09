# modules to make this work, flask for api end point, dbhelpers for connection, json for data in json
from flask import Flask, request, make_response
import dbhelpers as dh
import json
import apihelper as a

app = Flask(__name__)

@app.get('/api/inventory')
# return id, name, description, stock, created_at
def inventory_list():
    result = dh.run_statement('CALL inventory_list()')
    if(type(result) == list):
        return make_response(json.dumps(result, default=str), 200)
        # inventory_json = json.dumps(result, default=str)
        # return inventory_json
    else:
        return make_response(json.dumps(result, default=str), 400)
        # print('error, error, error ')

# needs 3 argument(name, description, quantity) to add new item to db and returns the item's id as json
@app.post('/api/add_new_item')
# inserts new item into db, only requires 3 input name, description, stock
def add_new_item():
    name_input = request.json.get('name')
    description_input = request.json.get('description')
    stock_input = request.json.get('stock')
    result = dh.run_statement('CALL add_new_item(?,?,?)', [name_input, description_input, stock_input])
    if(type(result) == list):
        # using make response to make it easier for me to debug
        return make_response(json.dumps(result, default=str), 200)
        # client_json = json.dumps(result, default=str)
        # return client_json
    else:
        return make_response(json.dumps(result, default=str), 400)
        # print('error, error, error ')

#add and update current item in database and returns the value at the end
@app.patch('/api/update_inventory_item')
def add_and_update_item():
    id_input = request.json.get('id')
    quantity_added = request.json.get('add_qt')
    result = dh.run_statement('CALL add_and_update_item(?,?)', [id_input, quantity_added])
    if(type(result) == list):
        return make_response(json.dumps(result, default=str), 200)

    else:
        return make_response(json.dumps(result, default=str), 400)




app.run(debug=True)