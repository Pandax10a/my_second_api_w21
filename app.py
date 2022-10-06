from flask import Flask, request
import dbhelpers as dh
import json

app = Flask(__name__)

@app.get('/api/inventory')

def inventory_list():
    result = dh.run_statement('CALL inventory_list()')
    if(type(result) == list):
        inventory_json = json.dumps(result, default=str)
        return inventory_json
    else:
        print('error, error, error ')



app.run(debug=True)