# modules to make this work, flask for api end point, dbhelpers for connection, json for data in json
from unittest import result
from flask import Flask, request, make_response
import dbhelpers as dh
import json
import apihelper as a

app = Flask(__name__)

@app.get('/api/item')
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
@app.post('/api/item')
# inserts new item into db, only requires 3 input name, description, stock
def add_new_item():
    name_input = request.json.get('name')
    description_input = request.json.get('description')
    stock_input = request.json.get('stock')

    valid_check = a.check_endpoint_info(request.json, ['name', 'description', 'stock'])
    if(type(valid_check) == str):
        return valid_check

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
@app.patch('/api/item')
def add_and_update_item():
    id_input = request.json.get('id')
    quantity_added = request.json.get('add_qt')
    # check to see if the value enter is valid(string)
    valid_check = a.check_endpoint_info(request.json, ['id', 'add_qt'])
    if(type(valid_check) == str):
        return valid_check

    result = dh.run_statement('CALL add_and_update_item(?,?)', [id_input, quantity_added])
    if(type(result) == list):
        # http response 200 for success, 400 for fail
        return make_response(json.dumps(result, default=str), 200)

    else:
        return make_response(json.dumps(result, default=str), 400)

#give id and delete item from db
@app.delete('/api/item')
def remove_item():
    item_id = request.json.get('id')
    valid_check = a.check_endpoint_info(request.json, ['id'])
    if(type(valid_check) == str):
        return valid_check
    result = dh.run_statement('CALL delete_inventory_item(?)', [item_id])
    if(type(result) == list):

        return make_response(json.dumps(result, default=str), 200)

    else:
        return make_response(json.dumps(result, default=str), 400)


@app.get('/api/employee')
# input an id, to return employee name, position, hired_at, hourly wage from db
def search_employee_by_id():
    emp_id = request.args.get('id')
    valid_check = a.check_endpoint_info(request.args, ['id'])
    if(type(valid_check) == str):
        return valid_check 
    result = dh.run_statement('CALL employee_search(?)', [emp_id])
    if(type(result) == list):
        return make_response(json.dumps(result, default=str), 200)
       
    else:
        return make_response(json.dumps(result, default=str), 400)

@app.post('/api/employee')
def new_employee():
    name = request.json.get('name')
    position = request.json.get('position')
    wage = request.json.get('wage')
    valid_check = a.check_endpoint_info(request.json, ['name', 'position', 'wage'])
    if(type(valid_check) == str):
        return valid_check
    result = dh.run_statement('CALL add_employee(?,?,?)', [name, position, wage])
    if(type(result) == list):
        return make_response(json.dumps(result, default=str), 200)
       
    else:
        return make_response(json.dumps(result, default=str), 400)





app.run(debug=True)

