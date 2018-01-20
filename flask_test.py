from flask import Flask
from flask import request
from flask import make_response,Response
from flask import abort
import consul
import json
import requests
from tiandiPythonClient import tiandiPythonClient

c = consul.Consul('202.120.167.198',8500)
tiandiPythonClient = tiandiPythonClient
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/services')
def get_services():
    services = c.agent.services()
    checks = c.agent.checks()
    available_services = []

    for (k,v) in checks.items():
        if v['Status'] == 'passing':
            service_id = v['ServiceID']
            service_name = v['ServiceName']
            address = services[service_id]['Address']
            port = services[service_id]['Port']
            # get test services from request
            if port!=None:
                address = address + ':' + str(port)
            test_services = requests.get(address+'/services')
            for item in json.loads(test_services.text):
                item['path'] = address + item['path']
                if item not in available_services:
                    available_services.append(item)


    j = json.dumps(available_services)
    print(j)
    return response_header(j)

@app.route('/metadata',methods=['GET','POST','PUT'])
def metadata():
    if request.method == 'GET':
        args = request.args
        if args.get('name') != None:
            resp = json.dumps(tiandiPythonClient.getMetadata(args.get('name')))
        else:
            resp = json.dumps(tiandiPythonClient.getMetadata())
        return response_header(resp)
    elif request.method == 'POST':
        json_payload = request.json
        try:
            tiandiPythonClient.createMetadata(json_payload)
            return response_header(json.dumps(tiandiPythonClient.getMetadata(json_payload['name'])))
        except Exception as err:
            abort(409)
            resp = make_response(err)
            return resp
    elif request.method == 'PUT':
        json_payload = request.json
        try:
            tiandiPythonClient.updateMetadata(json_payload)
            return make_response()
        except Exception as err:
            abort(409)
            resp = make_response(err)
            return resp

@app.route('/task',methods=['GET','POST','PUT','DELETE'])
def task():
    if request.method == 'GET':
        args = request.args
        if args.get('name') != None:
            resp = json.dumps(tiandiPythonClient.getTask(args.get('name')))
        else:
            resp = json.dumps(tiandiPythonClient.getTask())
        return response_header(resp)
    elif request.method == 'POST':
        json_payload = request.json
        try:
            tiandiPythonClient.registerTask(json_payload)
            return make_response()
        except Exception as err:
            abort(500)
            resp = make_response(err)
            return resp
    elif request.method == 'PUT':
        json_payload = request.json
        try:
            tiandiPythonClient.updateTask(json_payload)
            return make_response()
        except Exception as err:
            abort(500)
            resp = make_response(err)
            return resp
    elif request.method == 'DELETE':
        name = request.args.get('name')
        if name != None:
            try:
                tiandiPythonClient.unregisterTask(name)
                return make_response()
            except Exception as err:
                abort(500)
                resp = make_response(err)
                return resp
        else:
            return make_response()

@app.route('/startWorkflow',methods=['POST'])
def startWorkflow():
    name = request.args.get('name')
    inputjson = request.json
    if name != None:
        return tiandiPythonClient.startWorkflow(name,inputjson)
    else:
        abort(500)
        return make_response('error')

def response_header(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'text/json; charset=utf-8'
    return resp

if __name__ == '__main__':
    app.run()