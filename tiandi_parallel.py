from __future__ import print_function


from conductor import conductor
from conductor.ConductorWorker import ConductorWorker
import requests


def execute_health_check(task):
    print('exec health check function')
    url = 'http://10.60.38.176:8080/health'
    res = requests.get(url)
    return {'status': 'COMPLETED', 'output': {'status': res.text}, 'logs': ['one','two']}

def execute_a(task):
    print('exec a function')
    url = 'http://10.60.38.176:8080/a'
    res = requests.get(url)
    return {'status': 'COMPLETED', 'output': {'result': res.text}, 'logs': ['one','two']}

def execute_b(task):
    print('exec b function')
    url = 'http://10.60.38.176:8080/b'
    res = requests.get(url)
    return {'status': 'COMPLETED', 'output': {'result': res.text}, 'logs': ['one','two']}

def execute_c(task):
    print('exec c function')
    url = 'http://10.60.38.176:8080/c'
    res = requests.get(url)
    return {'status': 'COMPLETED', 'output': {'result': res.text}, 'logs': ['one','two']}

def main():
    print('Starting tinadi-demo workflows')
    metadataClient = conductor.MetadataClient('http://202.120.167.198:8080/api')
    # metadataClient.unRegisterTaskDef('tiandi_c');
    cc = ConductorWorker('http://10.60.38.173:8080/api', 1, 2)
    cc.start('tiandi_health_check_task', execute_health_check, False)
    cc.start('tiandi_a', execute_a, False)
    cc.start('tiandi_b', execute_b, False)
    cc.start('tiandi_c', execute_c, True)

if __name__ == '__main__':
    main()