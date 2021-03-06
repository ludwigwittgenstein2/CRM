import requests

def _url(path):
    return 'https://todo.example.com' + path

def get_tasks():
    return requests.get(_url('/tasks/'))

def describe_task(task_id):
    return requests.get(_url('/tasks/{:d}/'.format(task_id)))

def add_task(summary, description=""):
    return requests.post(_url('/tasks/'),json={'summary':summary,'description':description,})

def update_task(task_id, summary, description):
    url = _url('/tasks/{:d}/'.format(task_id))
    return requests.put(url, json={'summary':summary,'descripton':description,})
