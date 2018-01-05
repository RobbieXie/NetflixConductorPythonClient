from __future__ import print_function

from time import sleep

from conductor.ConductorWorker import ConductorWorker
import requests


def execute_health_check(task):
    print('exec health check function')
    url = 'http://10.60.38.176:8080/health'
    res = requests.get(url)
    return {'status': 'COMPLETED', 'output': {'status': res.text}, 'logs': ['one', 'two']}


def execute_a(task):
    print('exec a function')
    url = 'http://10.60.38.176:8080/a'
    res = requests.get(url)
    return {'status': 'COMPLETED', 'output': {'result': res.text}, 'logs': ['one', 'two']}


def execute_b(task):
    print('exec b function')
    url = 'http://10.60.38.176:8080/b'
    res = requests.get(url)
    return {'status': 'COMPLETED', 'output': {'result': res.text}, 'logs': ['one', 'two']}


def execute_c(task):
    print('exec c function')
    url = 'http://10.60.38.176:8080/c'
    res = requests.get(url)
    return {'status': 'COMPLETED', 'output': {'result': res.text}, 'logs': ['one', 'two']}


def main():
    print('Starting tinadi-demo workflows')
    cc = ConductorWorker('http://202.120.167.198:8080/api', 1, 2)
    cc.start('tiandi_health_check_task', execute_health_check, False)
    cc.start('tiandi_a', execute_a, False)
    cc.start('tiandi_b', execute_b, False)
    cc.start('tiandi_c', execute_c, True)
cc = ConductorWorker('http://202.120.167.198:8080/api', 1, 2)

def task_handler(task,url, ):
    print('exec c function')
    res = requests.get(url)
    return {'status': 'COMPLETED', 'output': {'result': res.text}, 'logs': ['one', 'two']}
@http('/task/reg','POST')
def task_reg(name,parms):
    cc.start(NAME, task_handler,parms, False)
