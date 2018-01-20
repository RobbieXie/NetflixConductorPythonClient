from __future__ import print_function

from time import sleep

from conductor.ConductorWorker import ConductorWorker
import requests

def execute_code(task):
    print('exec code function')
    inputString = task['inputData']['inputString']
    url = 'http://10.60.38.176:8080/code?id=' + inputString
    res = requests.get(url)
    return {'status': 'COMPLETED', 'output': {'code': res.text}, 'logs': ['one','two']}

def execute_register(task):
    print('exec register function')
    code = task['inputData']['code']
    url = 'http://10.60.38.176:8080/register/' + code
    res = requests.get(url)
    return {'status': 'COMPLETED', 'output': {'status': res.text}, 'logs': ['one','two']}

def execute_deregister(task):
    print('exec deregister function')
    sleep(10)
    code = task['inputData']['code']
    url = 'http://10.60.38.176:8080/deregister/' + code
    res = requests.get(url)
    return {'status': 'COMPLETED', 'output': {'status': res.text}, 'logs': ['one','two']}

def main():
    print('Starting tinadi-demo workflows')
    cc = ConductorWorker('http://10.60.38.173:18080/api', 1, 2)
    cc.start('tiandi_code_task', execute_code, False)
    cc.start('tiandi_register_task', execute_register, False)
    cc.start('tiandi_deregister_task', execute_deregister, True)

if __name__ == '__main__':
    main()